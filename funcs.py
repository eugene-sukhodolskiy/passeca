import argparse
import random
import hashlib

def xor_crypt(text, key):
	crypted_text = ""
	for char in text:
		crypted_char = chr(ord(char) ^ key)
		crypted_text += crypted_char
	return crypted_text

def make_script_args():
	parser = argparse.ArgumentParser(description="Simple password generator")

	parser.add_argument("-k", "--keystring", type=str, help="The passphrase on the basis of which the password will be generated")
	parser.add_argument("-f", "--keyfile", type=str, help="The path to the file on the basis of which the password will be generated. This is an alternative to the --keystring option")
	parser.add_argument("-s", "--salt", type=str, help="The required parameter is salt. For example, the site domain or program name")
	parser.add_argument("-l", "--login", type=str, help="User login, if needed")
	parser.add_argument("-o", "--show", action="store_true", help="Show password without copied to clipboard")
	parser.add_argument("-c", "--create", action="store_true", help="Create file with key string")

	return parser.parse_args()

def gen_password(keystring, salt, login):
	keystring = str(keystring).strip().lower()
	src_password = hashlib.scrypt(bytes(keystring.encode("utf-8")), salt=bytes((salt + login).encode("utf-8")), n=16384, r=8, p=1, dklen=15)
	src_password = src_password.hex()

	# add random spec symbol
	special_chars = "!@#$%^&*()"
	random.seed(keystring + salt + login)
	index = random.randint(0, len(src_password))
	src_password = src_password[:index] + random.choice(special_chars) + src_password[index:]

	password = src_password.upper()
	return password