import argparse

from rev.strings import Str
from rev.commandline import common

parser = common.parser_commands.add_parser(
    'hex',
    help = 'Hexlify input string'
)

parser.add_argument('--delim', 
    default = " ",
    help = 'Delimiter')

parser.add_argument('data', nargs='*',
    help = 'Data to be encoded')

def main(args):
    if not args.data:
        parser.print_usage()
    else:
        res = []
        for d in args.data:
            res.append(Str(d).hex())
        print(args.delim.join(res))

