from .yeet import parse_args, read_file, yeet, output_formatted


def main():
    args = parse_args()
    req = read_file(args.requestfile)
    res = yeet(req)
    output_formatted(res)
