'''This script will convert xls and xlsx files to csv.'''

import argparse
import xlrd
import os
from datetime import datetime
from glob import glob
from sys import stdout

def excelToCSV(infile, outdir, tsv):
	# Converts excel file to csv
	ext = ".csv"
	delim = ","
	if tsv == True:
		ext = ".tsv"
		delim = "\t"
	wb = xlrd.open_workbook(infile)
	sheets = wb.sheet_names()
	for i in sheets:
		ws = wb.sheet_by_name(i)
		if len(sheets) > 1:
			# Get file names from sheets
			outfile = outdir + i + ext
		else:
			# Get file name form input file
			outfile = outdir + infile[infile.rfind("/")+1:infile.rfind(".")] + ext
		with open(outfile, "w") as output:
			for rownum in range(ws.nrows):
				output.write(delim.join([str(x) for x in ws.row_values(rownum)]) + "\n")

def getFiles(indir, outdir, tsv):
	# Iterates over all excel files in directory
	files = glob(indir + "*.xls*")
	ext = "csv"
	if tsv == True:
		ext = "tsv"
	print(("\n\tConverting Excel files to {}...").format(ext))
	for idx,f in enumerate(files):
		stdout.write(("\r\tConverting file {} of {}...").format(idx+1, len(files)))
		excelToCSV(f, outdir, tsv)

def main():
	starttime = datetime.now()
	parser = argparse.ArgumentParser(description="This script will convert xls and xlsx files to csv.")
	parser.add_argument("--tsv", action = "store_true", default = False,
help = "Converts xlsx files to tab seperated text files (converts to csv by default).")
	parser.add_argument("-i", 
help = "Path to input file or directory (all xls(x) files in given directory will be converted).")
	parser.add_argument("-o", default = "",
help = "Path to output directory (Leave blank if current directory).")
	args = parser.parse_args()
	# Check output directory
	if args.o[-1] != "/":
		args.o += "/"
	if not os.path.isdir(args.o):
		os.mkdir(args.o)
	if os.path.isdir(args.i):
		if args.i[-1] != "/":
			args.i += "/"
		getFiles(args.i, args.o, args.tsv)
	elif ".xls" in args.i:
		print(("\n\tConverting {} to csv...").format(args.i))
		excelToCSV(args.i, args.o, args.tsv)
	else:
		print("\n\t[Error] Please specify valid xls/xlsx file or directory. Exiting.")
		quit()
	print(("\n\tFinished. Runtime: {}\n").format(datetime.now()-starttime))	

if __name__ == "__main__":
	main()
