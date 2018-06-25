'''This script will convert an input file's encoding to utf-8'''

import os
import codecs
import chardet
from datetime import datetime
from argparse import ArgumentParser

def recode(infile, outfile):
	# Writes contents of infile to outfile in UTF-8. Encoding is determined line-by-line
	passes = 0
	total = 0
	print(("\n\tDetermining encoding for each line in {}...").format(os.path.split(infile)[1]))
	print(("\tWriting UTF-8 encoded data to {}...").format(os.path.split(outfile)[1]))
	with codecs.open(outfile, "w", encoding="utf-8") as output:
		with open(infile, "rb") as f:
			for line in f:
				total += 1
				try:
					enc = chardet.detect(line)
					s = codecs.decode(line, enc["encoding"])
					output.write(s)
					passes += 1
				except UnicodeDecodeError:
					pass
	return passes, total

def convert(infile, outfile, enc):
	# Writes contents of infile to outfile in UTF-8 usning single input encoding
	passes = 0
	total = 0
	print(("\n\tReading {} with {} encoding...").format(os.path.split(args.i)[1], args.e))
	print(("\tWriting UTF-8 encoded data to {}...").format(os.path.split(outfile)[1]))
	with codecs.open(outfile, "w", encoding="utf-8") as output:
		with codecs.open(infile, "r", encoding=enc) as f:
			for line in f:
				total += 1
				try:
					output.write(line[:-1] + "\r\n")
					passes += 1
				except UnicodeDecodeError:
					pass
	return passes, total

def main():
	start = datetime.now()
	parser = ArgumentParser("This script will convert an input file's \
encoding to utf-8. All other formatting will remain unchanged.")
	parser.add_argument("-e", 
help = "Encoding of input file if known (otherwise encoding is determined on the fly).")
	parser.add_argument("i", 
help = "Path to input file. Output will be written in the same directory.")
	args = parser.parse_args()
	# Check infile and get outfile
	if not os.path.isfile(args.i):
		print(("\n\t[Error] Cannot find {}. Exiting.").format(args.i))
		quit()
	outfile = ("{}.UTF{}").format(args.i[:args.i.find(".")], args.i[args.i.rfind("."):])
	if args.e:
		p, t = convert(args.i, outfile)
	else:
		p, t = recode(args.i, outfile)
	print(("\tConverted {} out of {} total lines.").format(p, t))
	print(("\tFinished. Runtime: {}\n").format(datetime.now()-start))

if __name__ == "__main__":
	main()
