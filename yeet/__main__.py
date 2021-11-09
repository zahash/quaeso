import argparse

from yeet.yeet import Yeeter


def main():
    args = parse_args()
    yeeter = Yeeter()
    yeeter.yeet(args.requestfilepath)


def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "requestfilepath",
        type=str,
        help="Request filepath in .json or .yaml or .yml format",
    )
    return ap.parse_args()
