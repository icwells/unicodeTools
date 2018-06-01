'''This script will convert a given text file to utf-8 encoded csv file'''

import os
import codecs
from datetime import datetime
from argparse import ArgumentParser

def convert(infile, outfile, delim):
	# Writes contents of infile to outfile in UTF-8 usning single input encoding
	print(("\n\tWriting {} to csv...").format(infile))
	with codecs.open(outfile, "w", encoding="utf-8") as output:
		with open(infile, "r") as f:
			for line in f:
				try:
					line = line.replace(",", ";")
					line = line.replace(delim, ",")
					output.write(line)
				except UnicodeDecodeError:
					pass

def main():
	start = datetime.now()
	parser = ArgumentParser("This script will convert a given text file to utf-8 encoded csv file.")
	parser.add_argument("-d", 
help = "Delimeter of input file if known (otherwise it will be automatically determined).")
	parser.add_argument("i", 
help = "Path to input file (must be utf-8 encoded). Output will be written in the same directory.")
	args = parser.parse_args()
	# Check infile and get outfile
	if not os.path.isfile(args.i):
		print(("\n\t[Error] Cannot find {}. Exiting.\n").format(args.i))
		quit()
	if args.i[args.i.rfind("."):] == "csv":
		print("\n\t[Error] Make sure input file is not comma seperated. Exiting.\n")
		quit()
	outfile = ("{}.csv").format(args.i[:args.i.rfind(".")])
	convert(args.i, outfile, args.d)
	print(("\tFinished. Runtime: {}\n").format(datetime.now()-start))

if __name__ == "__main__":
	main()
