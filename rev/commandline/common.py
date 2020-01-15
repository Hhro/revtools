import argparse

parser = argparse.ArgumentParser(description = 'Reversing tools',
                                 prog = 'rev')

parser_commands = parser.add_subparsers(dest='command')