import argparse

from rev.electron import asar
from rev.commandline import common
from ..log import logger

parser = common.parser_commands.add_parser(
    "elec",
    help = "Electron tools"
)

parser.add_argument("-e", "--extract_asar",
    const = "resources/app.asar",
    default = None,
    dest = "asar",
    help = "Extract asar",
    metavar = "ASAR",
    nargs = "?"
)

parser.add_argument("-d", "--dest",
    default = "./app.asar.extracted",
    dest = "dest",
    help = "Destination directory",
    metavar = "DIR"
)

def main(args):
    if args.asar != None:
        logger.info(
            "Extract '{asar}' => '{dest}'"
            .format(asar=args.asar, dest=args.dest)
        )
        asar.extract_asar(args.asar, args.dest)
    else:
        parser.print_usage()
    