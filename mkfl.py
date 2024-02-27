import csv
import logging
import os
from optparse import OptionParser

colon = ':'
tab = '\t'
underscore = '_'
allowedoverflow = 1.40
userpathmappingfilename = 'userpathmappingfile.txt'
projectname = 'anncor'
zero = '0'
fl_extension = '.fl'

class FileList:
    def __init__(self, basename, annotator, cntr, flist):
        self.basename = basename
        self.annotator = annotator
        self.cntr = cntr
        self.flist = flist

def initialisation():
    userpathmap = {}
    pathusermap = {}
    with open(userpathmappingfilename, 'r', encoding='utf8') as userpathmappingfile:
        myreader = csv.reader(userpathmappingfile, delimiter=tab,)
        for row in myreader:
            userpathmap[row[0]] = row[1]
            pathusermap[row[1]] = row[0]

    return userpathmap, pathusermap

def pathsplit(astr):
    lcastr = astr.lower()
    cutoff = lcastr.find(projectname) + len(projectname)
    (head, tail) = (astr[:cutoff], astr[cutoff+1:])
    return (head, tail)


def fl_assign(apath, annotatorhead):
    (_, tail) = pathsplit(apath)
    result = os.path.join(annotatorhead, tail)
    return result

def printfilelist(fl,userpathmap):
    filelistname = underscore.join([fl.basename, fl.annotator, str(fl.cntr).rjust(2, zero)])
    filename = filelistname + fl_extension
    with open(filename, 'w', encoding='utf8') as outfile:
        print(filelistname, file=outfile)
        for apath in fl.flist:
            newpath = fl_assign(apath, userpathmap[fl.annotator])
            print(newpath, file=outfile)



def getfilesperannotator(inlist, annotators, countsperannotator):
    results = {}
    start = 1
    for (annotator, count) in zip(annotators, countsperannotator):
        end = min(start + count, len(inlist))
        results[annotator] = inlist[start:end]
        start = end
    return results

def getfilelists(filesperannotator, inlistname, filesperfilelist):
    fls = []
    for annotator in filesperannotator:
        curfiles = filesperannotator[annotator]
        curcount = len(curfiles)
        firstline = 0
        annotatorfilecounter = 0
        while curcount > allowedoverflow * filesperfilelist:
            thisfilecount = filesperfilelist
            lastline = firstline + thisfilecount 
            annotatorfilecounter += 1
            # make a filelist for annotator with thisfilecount entries
            newfl = FileList(inlistname, annotator, annotatorfilecounter, curfiles[firstline:lastline])
            fls.append(newfl)
            curcount -= filesperfilelist
            firstline = lastline
        #make filelist for annotator with curcount entries
        #lastline = firstline + curcount + 1
        annotatorfilecounter += 1
        newfl = FileList(inlistname, annotator, annotatorfilecounter, curfiles[firstline:])
        fls.append(newfl)
    return fls


def make_filelists(inlist, annotators, proportions=None, filesperfilelist=100):
    if inlist is None or inlist == []:
        logging.error('No or empty input filelist')
        exit(-1)
    elif annotators is None or annotators == []:
        logging.error('No list or empty list of annotators to assign filelists to')
        exit(-1)
    elif proportions is None:
            proportions = [1 for _ in range(len(annotators))]
    elif len(proportions) != len(annotators):
        logging.error('Annotators and proportions do not match: {} v. {}'.format(len(annotators), len(proportions)))
        exit(-1)
    #sum the proportions
    partscount = sum(proportions)
    inlistname = inlist[0]
    linlist = len(inlist) - 1
    unit = (linlist // partscount) + 1
    countsperannotator = [unit * prop for prop in proportions]
    fls = []
    firstline = 1
    filesperannotator = getfilesperannotator(inlist, annotators, countsperannotator)
    fls = getfilelists(filesperannotator, inlistname, filesperfilelist)
    return fls

def getinlist(infilename):
    inlist = []
    with open(infilename, 'r', encoding='utf8') as infile:
        for line in infile:
            inlist.append(line[:-1])
    return inlist


def test():
    inlistfilename = 'testerrors.fl'
    inlist = getinlist(inlistfilename)
    annotators = ['jan', 'max', 'lieke']
    filelists = make_filelists(inlist, annotators, proportions=[2,1,2])
    for fl in filelists:
        printfilelist(fl, userpathmap)
    print('Done!')

def isempty(astr):
    result = astr is None or astr == ''
    return result

userpathmap, pathusermap = initialisation()

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="inlistfilename",
                      help="filename of the input filelist")
    parser.add_option("-a", "--ann", dest="annotators",
                      help="annotator names separated by :,e.g. max:lieke")
    parser.add_option("-p", "--prop", dest="proportions",
                      help="proportion per annotator separated by :,e.g. 1:2")
    parser.add_option("-l", "--len", dest="filesperfilelist",
                      help="default length of filelists", default='100')
    (options, args) = parser.parse_args()

    if isempty(options.inlistfilename):
        print('please specify an input filelist (-f)')
        exit(-1)
    else:
        inlistfilename = options.inlistfilename
    if isempty(options.annotators):
        print('please specify one or more annotators separated by :')
        exit(-1)
    else:
        annotators = options.annotators.split(colon)
    if isempty(options.proportions):
        print('Distribution will be according to equal proportions')
        proportions = None
    else:
        proportionsstrlist = options.proportions.split(colon)
        proportions = list(map(int, proportionsstrlist))
    filesperfilelist = int(options.filesperfilelist)

    inlist = getinlist(inlistfilename)
    filelists = make_filelists(inlist, annotators, proportions=proportions, filesperfilelist=filesperfilelist)
    for fl in filelists:
        printfilelist(fl, userpathmap)
    print('Done!')




if __name__ == '__main__':
    #test()
    main()