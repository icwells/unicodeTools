'''This script will convert an input file's encoding to utf-8'''

import os
import codecs
import chardet
from datetime import datetime
from argparse import ArgumentParser

def getDelim(line):
	# Returns delimiter
	for i in ["\t", ",", " "]:
		if i in line:
			return i
	print("\n\t[Error] Cannot determine delimeter. Check file formatting. Exiting.\n")
	quit()

def reformat(line, delim, csv):
	# Converts input line to csv/tsv
	if csv == True:
		sep = ","
		rep = ";"
	else:
		sep = "\t"
		rep = " "
	# Replace existing seperators (use illogical seperator to avoid adding columns)
	line = line.replace(sep, "~")
	line = sep.join(line.split(delim))
	return line.replace("~", rep)

def convert(infile, outfile, csv, tsv):
	# Writes contents of infile to outfile in UTF-8. Encoding is determined line-by-line
	passes = 0
	total = 0
	first = True
	print(("\n\tDetermining encoding for each line in {}...").format(os.path.split(infile)[1]))
	print(("\tWriting UTF-8 encoded data to {}...").format(os.path.split(outfile)[1]))
	with codecs.open(outfile, "w", encoding="utf-8") as output:
		with open(infile, "rb") as f:
			for line in f:
				total += 1
				try:
					enc = chardet.detect(line)
					s = codecs.decode(line, enc["encoding"])
					if csv == True or tsv == True:
						if first == True:
							delim = getDelim(s)
							first = False
						s = reformat(s, delim, csv)
					output.write(s)
					passes += 1
				except UnicodeDecodeError:
					pass
	return passes, total

def checkArgs(args):
	# Checks input arguments for errors
	if args.tsv and args.csv:
		print("\n\t[Error] Please specify no more than one of csv/tsv. Exiting.")
		quit()		
	if not os.path.isfile(args.i):
		print(("\n\t[Error] Cannot find {}. Exiting.").format(args.i))
		quit()
	path = args.i[:args.i.find(".")]
	ext = args.i[args.i.rfind("."):]
	if args.csv == True:
		ext = ".csv"
	elif args.tsv == True:
		ext = ".tsv"
	return args, ("{}.UTF8{}").format(path, ext)

def main():
	start = datetime.now()
	parser = ArgumentParser("This script will convert an input file's \
encoding to utf-8.")
	parser.add_argument("--csv", action = "store_true", default = False,
help = "Optionally convert to comma seperated text files.")
	parser.add_argument("--tsv", action = "store_true", default = False,
help = "Optionally convert to tab seperated text files.")
	parser.add_argument("i", 
help = "Path to input file. Output will be written in the same directory.")
	args, outfile = checkArgs(parser.parse_args())
	p, t = convert(args.i, outfile, args.csv, args.tsv)
	print(("\tConverted {} out of {} total lines.").format(p, t))
	print(("\tFinished. Runtime: {}\n").format(datetime.now()-start))

if __name__ == "__main__":
	main()
