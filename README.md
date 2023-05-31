### Install
For ubuntu:

`git clone https://github.com/eugene-sukhodolskiy/passeca.git`

`cd passeca`

`pip install -r requirements.txt`

`sudo chmod +x passeca.py`

`cp passeca.py ~/.local/bin`

`export PATH="$HOME/.local/bin:$PATH"`

### Usage
`passeca.py [-h] [-k KEYSTRING] [-f KEYFILE] [-s SALT] [-l LOGIN]`

Options:
-  `-h, --help`                           Show this help message and exit
-  `-k KEYSTRING, --keystring KEYSTRING`  The passphrase on the basis of which the password will be generated
-  `-f KEYFILE, --keyfile KEYFILE`        The path to the file on the basis of which the password will be generated. This is an alternative to the --keystring option
-  `-s SALT, --salt SALT`                 The required parameter is salt. For example, the site domain or program name
-  `-l LOGIN, --login LOGIN`              User login, if needed
-  `-o, --show`                           Show password without copied to clipboard