### Install
For ubuntu:

`git clone https://github.com/eugene-sukhodolskiy/passeca.git`

`cd passeca`

`sudo chmod +x passeca.py`

`cp passeca.py ~/.local/bin`

`export PATH="$HOME/.local/bin:$PATH"`

### Usage
`passeca.py [-h] [--keystring KEYSTRING] [--keyfile KEYFILE] [--salt SALT] [--login LOGIN]`

Options:
-  `-h, --help`            Show this help message and exit
-  `--keystring KEYSTRING` The passphrase on the basis of which the password will be generated
-  `--keyfile KEYFILE`     The path to the file on the basis of which the password will be generated. This is an alternative to the --keystring option
-  `--salt SALT`           The required parameter is salt. For example, the site domain or program name
-  `--login LOGIN`         User login, if needed
