import gzip, random
def get_randomQual(minQual, maxQual, length):
    result = []
    for idx in range(length):
        qual = chr(random.randrange(minQual, maxQual + 1))
        result += [qual]
    return ''.join(result)


    




prefix = 'SRR10121034_subreads.chQual'

fin  = gzip.open(prefix + '.fastq.gz', 'rt')
fout = gzip.open(prefix + '.chQual.fastq.gz', 'wt')

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