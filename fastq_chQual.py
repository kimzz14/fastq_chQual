from optparse import OptionParser
import subprocess, sys, smtplib, time
import gzip, random

#option parser
parser = OptionParser(usage="""Run annotation.py \n Usage: %prog [options]""")
parser.add_option("-i","--input",action = 'store',type = 'string',dest = 'INPUT',help = "")
parser.add_option("-o","--output",action = 'store',type = 'string',dest = 'OUTPUT',help = "")
(opt, args) = parser.parse_args()
if opt.INPUT == None or opt.OUTPUT == None:
    print("Error! usage: fastq_chQual.py -i SRR10121034_subreads.fastq.gz -o SRR10121034_subreads.chQual.fastq.gz")
    sys.exit()


def get_randomQual(minQual, maxQual, length):
    result = []
    for idx in range(length):
        qual = chr(random.randrange(minQual, maxQual + 1))
        result += [qual]
    return ''.join(result)


infile = opt.INPUT
outfile = opt.OUTPUT

fin  = gzip.open(infile, 'rt')
fout = gzip.open(outfile, 'wt')

for lineIDX, line in enumerate(fin):
    if lineIDX%4 == 0:
        fout.write(line)
    elif lineIDX%4 == 1:
        fout.write(line)
    elif lineIDX%4 == 2:
        fout.write(line)
    elif lineIDX%4 == 3:
        fout.write(get_randomQual(121, 126, len(line.rstrip('\n'))) + '\n')
    else:
        print('bug')
fout.close()