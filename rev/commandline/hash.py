import argparse

from rev.strings import Str
from rev.commandline import common

parser = common.parser_commands.add_parser(
    "hash",
    help = "Do hash to input string"
)

parser.add_argument("--raw",
    default = False,
    action = "store_true",
    help = "Print in raw")

parser.add_argument("--delim", 
    default = " ",
    help = "Delimiter")

parser.add_argument("-a", "--algo",
    default = "md5",
    help= "Hash algorithm to use")

parser.add_argument("data", nargs="*",
    help = "Data to be hashed")

def main(args):
    if not args.data:
        parser.print_usage()
    else:
        res = []
        for d in args.data:
            res.append(Str(d).hash(args.algo))
        print(args.delim.join(res))