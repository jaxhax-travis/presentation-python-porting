import sys
import argparse

parser = argparse.ArgumentParser(description="Check if a file exist")
parser.add_argument("file", type=argparse.FileType('r'),
		help="check if file is valid.")

if len(sys.argv) == 1:
	parser.print_help(sys.stderr)
	sys.exit(1)

args = parser.parse_args()

print(type(args.file))
print("Seems to exist!")
