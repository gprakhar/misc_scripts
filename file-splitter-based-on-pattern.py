#Script to split a file based on some string
#Date: 29 July 2015 IST
#Author: Prakhar Gaur

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', metavar='f', help='name text outputfile, with multiple entries, which should be split')
parser.add_argument('pattern', metavar='p', help='string pattern which is to act as delimeter for splitting')

args = parser.parse_args()
inputfileName = str(args.filename)
patternString = str(args.pattern)

def files():
    n = 0
    while True:
        n += 1
        yield open('%d.part' % n, 'w')


fs = files()
outfile = next(fs) 
flag = 1

with open(inputfileName) as infile:
    for line in infile:
        if patternString not in line:
            outfile.write(line)
        else:
            items = line.split(patternString)
	    outfile.write(patternString)
	    outfile = next(fs)
	    flag += 1

##Add code to delete the | '%d.part' % flag | file.
#since this the last file and is empty and useless
