#! /usr/bin/env python
"""
Get all coverage spectrum and numbers of reads with that spectrum across samples

% scripts/count_spectrum_freq_multiple_files.py <comb list file> <output file>

Use '-h' for parameter help.

For each sample, there is a .comb file with all the reads and the corresponding
coverage across samples. This script will generate all the coverage spectrums
and the number of reads in different samples with that specific coverage 
spectrums.

The order of the .comb files in <comb list file> will determine the order
of samples in each line in <output file>.


.comb file list example: (as the only input)

[qingpeng@dev-intel14 Ecoli_Alpha]$ more comb.list 
e.coli_150x_0.01e_100.fa.comb
e.coli_50x_0.00e_100.fa.comb
e.coli_50x_0.01e_100.fa.comb
e.coli_50x_0.02e_100.fa.comb

.comb file example: (generated by other script, like "get_comb_muti.py".)

read0 96 36 25 28
read1 98 31 39 26
read2 94 41 35 28
read3 104 46 41 34
read4 97 44 28 33
read5 286 115 98 87
read6 117 40 41 32
read7 110 40 33 29
read8 105 45 32 32
read9 96 40 36 35
read10 83 34 25 22
output file example:

0-0-0-1 0 0 0 87943
0-0-0-2 0 0 0 24609
0-0-0-3 0 0 0 1578
0-0-0-4 0 0 0 75
0-0-0-5 0 0 0 4
1-0-0-0 27040 0 0 0
1-0-0-1 10326 0 0 58349
1-0-0-2 765 0 0 33028
1-0-0-3 38 0 0 3167
1-0-0-4 4 0 0 217
1-0-0-5 0 0 0 14
1-0-0-6 0 0 0 3
1-0-1-0 13115 0 13115 0
1-0-1-1 5367 0 5367 22585
1-0-1-2 495 0 495 13636
1-0-1-3 33 0 33 1383
1-0-1-4 0 0 0 118
1-0-1-5 1 0 1 8
1-0-1-6 0 0 0 3
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('comb_list')
parser.add_argument('output')

args = parser.parse_args()


str_sets = set()

def read_file(file_in,str_set):
    file_in_obj = open(file_in, 'r')
    count = {}
    for line in file_in_obj:
        
        line = line.rstrip()
        fields = line.split()

        key = '-'.join(fields[1:])
        
        
        str_set.add(key)
        
        if key in count:
            count[key] = count[key] + 1
        else:
            count[key] = 1
        
    return count,str_set
    
    
        
file_list_obj = open(args.comb_list,'r')

file_out_obj = open(args.output,'w')


count_list = []
n = 0
for line in file_list_obj:
    line = line.rstrip()
    count, str_sets = read_file(line, str_sets)
    print line+' done!'
    count_list.append(count)
    n = n+1

sorted_str = sorted(list(str_sets))
#print sorted_str

for spetr in sorted_str:
    to_print = spetr 
    for i in range(n):
        if spetr not in count_list[i]:
            fre = 0
        else:
            fre = count_list[i][spetr]
            
        to_print = to_print + ' ' + str(fre)

    file_out_obj.write(to_print+'\n')


            
            
            
            
            
            
            
