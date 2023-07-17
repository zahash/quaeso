import argparse

from quaeso.yeet import Yeeter


def main():
    args = parse_args()
    yeeter = Yeeter(args.colorize)
    yeeter.yeet(args.filepath)


def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "-f",
        "--filepath",
        type=str,
        required=True,
        help="Request filepath in .json or .yaml or .yml format",
    )
    ap.add_argument(
        "-c",
        "--colorize",
        action='store_true',
        help="colorize stdout and stderr"
    )
    return ap.parse_args()
