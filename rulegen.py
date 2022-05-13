#!/usr/bin/python
# -c: 0 = Append words, 1 = Prepend words, 2 = Append and Prepend words
# -f: Plain document with words that is going to be generated.
# -o: Output rule file that is going to be created when finished.
# ---------
# Example: python3 ./rulegen -c 0 -f file.txt -o myrule.rule
# ---------

import string
import argparse


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTIONS]...",
        description="Make append or prepend of words"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.1"
    )
    parser.add_argument(
        "-c", "--convert", dest="conv", type=int, required=True
    )
    parser.add_argument(
        "-f", "--infile", dest="file", required=True
    )
    parser.add_argument(
        "-o", "--outfile", dest="outfile", required=True
    )
    return parser


def ruleappend(text):
    alphanum = string.ascii_letters + string.digits
    multi = ""
    for chars in text:
        if chars not in alphanum:
            multi += "$\\x" + format(ord(chars), "x") + " "
        else:
            multi += "$" + chars + " "
    return multi[-len(multi):-1]


def ruleprepend(text):
    alphanum = string.ascii_letters + string.digits
    multi = ""
    text = text[::-1]
    for chars in text:
        if chars not in alphanum:
            multi += " ^\\x" + format(ord(chars), "x")
        else:
            multi += " ^" + chars
    return multi[-len(multi) + 1::]


if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()
    if args.conv >= 0 or args.conv <= 2:
        try:
            with open(args.file, "r", encoding="utf-8") as _input:
                lines = _input.read().splitlines()
                for line in lines:
                    with open(args.outfile, "a", encoding="utf-8") as _output:
                        if args.conv == 0:
                           _output.write(ruleappend(line) + "\n")
                        if args.conv == 1:
                            _output.write(ruleprepend(line) + "\n")
                        if args.conv == 2:
                            _output.write(ruleprepend(line) + "\n")
                            _output.write(ruleappend(line) + "\n")
                print("The progress is successful!")
        except FileNotFoundError as err:
            print("{}: {}".format(err.strerror, args.file))
    else:
        print("Error: Couldn't find the correct number for converting.")