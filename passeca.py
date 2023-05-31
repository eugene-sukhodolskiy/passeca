#!/usr/bin/env python3

import pyperclip
import funcs

xorKey = 42;
xorMark = "xor42\n"

args = funcs.make_script_args()

def create_keyfile(args):
	global xorKey, xorMark

	if not args.keyfile:
		print("!Set --keyfile option")
		exit()

	if not args.keystring:
		print("!Set --keystring option")
		exit()

	with open(args.keyfile, "w") as file:
		file.write(xorMark + str(funcs.xor_crypt(args.keystring, xorKey)))

	print(f"\nKeystring saved to file {args.keyfile}")

def make_params_for_password(args):
	global xorKey, xorMark
	
	if args.keyfile:
		try:
			with open(args.keyfile, "r") as file:
				keystring = file.read();
		except:
			print("!Keyfile not found");
			exit()
		if xorMark in keystring:
			keystring = funcs.xor_crypt(keystring.split(xorMark)[1], xorKey)
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

	salt = args.salt

	return keystring, salt, login

if args.create:
	create_keyfile(args)
else:
	keystring, salt, login = make_params_for_password(args)
	password = funcs.gen_password(keystring, salt, login)

	if args.show:
		print(f"\n{password}")
	else:
		pyperclip.copy(password)
		print("\nPassword copied to clipboard")


