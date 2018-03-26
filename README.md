# unicodeTools contains scripts for converting files to utf-8 based text
### Copyright 2018 by Shawn Rupp

## Download 

	git clone https://github.com/icwells/unicodeTools.git

## toUTF8 converts files into utf-8 encoded files of the same format
in progress...

## excelToText will convert xlsx files to tsv or csv. 
### Please note that this script will only extract text. It is not meant to extract hyperlinks, pictures, special formatting, etc.


	python excelToText.py {--tsv} -i path_to_input_file_or_directory -o path_to_output_directory

Input can either be a single xlsx file or a directory of them. Each sheet of each file will be converted into a seperate output file. 
By default, output will be in csv format (comma seperated), but specifying the --tsv flag will will produce tab seperated output. 
If an input file has only one sheet, the corresponding output will have the same name with a new extension. 
If a file has multiple sheets, the output files will have the name of the sheet they were extrated from. 
