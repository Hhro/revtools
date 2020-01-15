import sys

from rev.commandline import common
from rev.commandline import apk
from rev.commandline import hash
from rev.commandline import hex 
from rev.commandline.common import parser

commands = {
    "apk": apk.main,
    "hex": hex.main,
    "hash": hash.main
}

def main():
    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit()
    args = parser.parse_args() 
    commands[args.command](args)

if __name__ == '__main__':
    main()