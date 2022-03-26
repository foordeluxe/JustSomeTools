#!/usr/bin/env python3
# This tool is creating from emaildomain.com, to rules.
# Usage: ./dconvert.py -f inputfile.txt -o outputfile.rule

import argparse

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTIONS]...",
        description="Transform domains to rules"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument(
        "-f", "--infile", dest="file", required=True
    )
    parser.add_argument(
        "-o", "--outfile", dest="outfile", required=True
    )
    return parser

if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as _input:
            domains = _input.read().splitlines()
            for line in domains:
                value = ""
                incr = 0
                for char in line.rstrip():
                    if incr == 0 and char != '@':
                        value = "$@" + char
                    else:
                        value += "$" + char
                    incr += 1
                if len(value) < 31:
                    with open(args.outfile, "a", encoding="utf-8") as _output:
                        _output.write(value + "\n")
            print("The progress is successful!")
    except (FileNotFoundError) as err:
        print("{}: {}".format(err.strerror, args.file))
