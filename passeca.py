#!/usr/bin/env python3

import argparse
import hashlib
import random
import pyperclip

parser = argparse.ArgumentParser(description="Simple password generator")

parser.add_argument("-k", "--keystring", type=str, help="The passphrase on the basis of which the password will be generated")
parser.add_argument("-f", "--keyfile", type=str, help="The path to the file on the basis of which the password will be generated. This is an alternative to the --keystring option")
parser.add_argument("-s", "--salt", type=str, help="The required parameter is salt. For example, the site domain or program name")
parser.add_argument("-l", "--login", type=str, help="User login, if needed")
parser.add_argument("-o", "--show", action="store_true", help="Show password without copied to clipboard")

args = parser.parse_args()

# Set keystring
if args.keyfile:
	try:
		with open(args.keyfile, "r") as file:
			keystring = file.read();
	except:
		print("!Keyfile not found");
		exit()
elif args.keystring:
	keystring = args.keystring
else: 
	print("!No key string")
	exit()

if not args.salt:
	print("!Salt undefined")
	exit()

login = ""
if args.login:
	login = args.login

keystring = str(keystring).strip().lower()
src_password = hashlib.scrypt(bytes(keystring.encode("utf-8")), salt=bytes((args.salt + login).encode("utf-8")), n=16384, r=8, p=1, dklen=15)
src_password = src_password.hex()

# add random spec symbol
special_chars = "!@#$%^&*()"
random.seed(keystring + args.salt + login)
index = random.randint(0, len(src_password))
src_password = src_password[:index] + random.choice(special_chars) + src_password[index:]

password = src_password.upper()
if args.show:
	print(f"\n{password}")
else:
	pyperclip.copy(password)
	print("\nPassword copied to clipboard")


