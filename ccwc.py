
import argparse
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description="A simple wc clone")
parser.add_argument("-c", action="store_true", help="Print the byte count")
parser.add_argument("filename", nargs="?", help="File to process")
parser.add_argument("-l", action="store_true", help="Print the line count")
parser.add_argument("-w", action="store_true", help="Print the word count")

args = parser.parse_args()

if args.filename:
    file_path=Path(args.filename)
    data = file_path.read_bytes()
else:
    data = sys.stdin.buffer.read()

if args.c:
    print(f"{len(data)} {args.filename}")
if args.l:
    lines = data.split(b'\n')
    print(f"{len(lines) - 1} {args.filename}")
if args.w:
    words = data.split()
    print(f"{len(words)} {args.filename}")
if args.c == False and args.l == False and args.w == False:
    lines = data.split(b'\n')
    words = data.split()
    print(f"{len(lines) - 1} {len(words)} {len(data)} {args.filename}")