# Ace
Ace (Anncor Check Engine) is a tool to check Alpino syntactic structures.

The tool checks whether Alpino structures are correct, both formally and linguistically, and issues errors or warning of different degrees if this is not the case or likely not the case.

It generates a report with errors and warnings, as well as  filelists files compatible with the Tred tree editor.
The report is in MS Excel (.xlsx) format, since that is easiest to read and edit. The report can also be output as a tsv file.


## Usage

The most common usage is:

python anncor-checks.py -p PATH

issued on a command line in the folder where PATH is the path that contains the files to be checked. It will check all files in this path (and all its subfolders) that have a specific extension (default .xml).

It is best to run the program from the same location each time. Do not copy the program to other locations. If the files to be checked are not in the folder where the program resides indicate the location of the  files to be checked by the -p  parameter.

The following errors and warnings are distinguished:
- serious errors: errors caused by a violation of formal requirements on Alpino structures. If a serious erro is encountered, no further check on errors is possibe, so the serious erros in a file should be resoved first, and then ace should be run again.
- errors: configurations in the syntactic structure that ace considers incorrect, mostly for linguistic reasons
- likely errors: configurations in the syntactic structure that ace considers likely to be incorrect
- warnings: configurations in the syntactic structure that are below a certain threshold, based on statistics derived from the manually verified Lassy-Small and CGN treebanks  


Currently more than 55 different error types are distinguished.

The program first checks for serious errors. If any serious error is encountered, they are reported and no further checks are performed (other checks presuppose that the structure is formally correct). 

Errors have been identified on the basis of knowledge on the annotation conventions.  Likely errors and almost all warnings are based on statistics obtained from the LASSY and CGN  treebanks. 
If a certain phenomenon (e.g.  relation / cat combination, mother / child combination) encountered in the structure  does not occur in LASSY or CGN, an error is issued. If it occurs in LASSY or CGN but only very rarely (usually less than 10 times), a warning is issued. For many configurations that are well-formed despite a low freequency in tyhe mentiuoned treebanks, the threshoild has been manualy reset.


Output Table Format
The report generated is a table in an Excel worksheet in an Excel workbook and  the following columns:
•	User1: initially empty, see below for explanation
•	User2: initially empty, see below for explanation
•	Status: serious error, error, or warning
•	File: file where the error or warning was found
•	Mother:rel: relation of the mother node of the node that caused the error
•	Mother:cat: category of the mother node of the node that cause the error
•	ErrNr: an integer indicating the error number
•	Arg1: characterization of the node that caused the error
•	Message: error message
•	Arg2: other element in the tree that might be relevant for the error message
•	Remarks: for any remarks generated by the programme (so far always empty)
•	Path: path where the file was found
•	Annotator: User name of the annotator



## Marking exceptions to reported errors
Since many of the errors and warninghs are based on results from the past, which give no guarantees for the future, an  annotator may find that a particuar warning or error is not justified. The annotator can mark a reported error as incorrect so asto ignore it for this structure in the future (so, treat it as an exception). One can mark this by putting some comments in the fields user1 and user2 and saving the report under the name errors.xlsx. When re-run, these errors will still be reported, but with the comments of all annotators made in the past, so one can easily select the rows for which these fields are empty using the Excel autofilter selection to concentrate on the ones that still have to be investigated. If you check a completely new set of files, these messages will of course not appear, but when you later reinspect the original files, the messages will reappear, even if they have been made by a different annotator.

The .fl files only contain entries for errors not marked, so that there is a correpondence between the unmarked enties in the Excel report and the .fl file.


## Filelists

ACE generates multiple filelists, one for each error type, and a filelist with all errors and warnings. Seeparate filelists files are created because it  is usually wisest to first work on the serious errors reported, then on the errors, and only after that on the likely errors and warnings. 


## Options

This is the output of python anncor-checks.py -h:

```
Usage: anncor-checks.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILENAME, --file=FILENAME
                        Check the given file (default: None)
  -p PATH, --path=PATH  path of the files to be checked (default=.)
  -l FILELIST, --filelist=FILELIST
                        filelist: Check the files in the filelist
  --tsv                 Output in tsv format (default: False)
  --test                Check the testfolder (default: False)
  --outpath=OUTPATH     Output path (default=.)
  --outfile=OUTFILE     Filename of the file contain the warnings and errors
                        (default=errors)
  --permfile=PERMFILE   Filename of the permanently stored error annotations
                        (default=permannerrors)
  --permfilepath=PERMFILEPATH
                        Path for the Filename of the permanently stored error
                        annotations (default=temp
  --ext=EXT             Extension of the files to be checked (default= .xml)
  --verbose             show file being processed (default=False)
  --ini=INIFILE         Configuration file (default=<program_name>.ini)
  --reportevery=REPORTEVERY
                        Progress indication by number of files (default='' -no
                        reporting)
```

## Requirements

Ace makes use of some functions from the sastadev package. This package can be installed in the usual way 

pip install sastadev

and it makes use of several packages that are included in stadard python installations.

## History
This tool was developed and used in the Utrecht University AnnCor project in which the automatically generated Alpino syntactic structures were manually checked and if needed corrected.
The acronym Ace originall stood for "Anncor Check Engine", but since it can be used outside of the AnnCor project as welel, another appropriate expansion could be "Alpino structures Check Engine".

## Desirable extensions

It might be useful to turn this program into a web service called from the tree editor (Tred) so that each individual syntactic structure can be checked immediately after it has been edited.

## Author

This program was written by Jan Odijk
