import argparse
from getpass import getpass

from rev.android import apk
from rev.commandline import common

parser = common.parser_commands.add_parser(
    "apk",
    help = "Apk tools"
)

parser.add_argument("-d", "--download_apk",
    help = "Download apk file",
    default = None
)

def main(args):
    if args.download_apk != None:
        print(
            ("[Credential]\n"),
            ("FYI, don't use your important account!\n"),
            ("It's powered by `gplaycli`. Of course it would be safe.\n"),
            ("But I won't guarantee. :)\n")
        )
        gmail = input("Gmail address: ")
        pw = getpass("Password: ")

        apk.download_apk(args.download_apk, gmail, pw)

