# Bilgenur Baloglu
# rename names bam files

import glob
import json
import argparse
import subprocess
import os
import os.path

def get_sample_name(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    # list samples
    data = data['experimentAnalysisSettings']
    data = data['barcodedSamples']
    out = []
    for i in data.keys():
        x = data[i]['barcodes']
        for j in x:
            out.append([i, j]) 
    return out

def rename_file(infile, outfolder):
    infile = get_sample_name(infile)

    if os.path.exists(outfolder)==False:
        cmd = 'mkdir '+outfolder
        print(cmd)
        subprocess.call(cmd, shell=True)

    for f1, f2 in infile:
        print('working on', f1, f2)
        outname = outfolder+'/'+f1+'_'+f2
        outname = outname.replace(' ','_')
        cmd = 'touch '+outname
        print(cmd)
        subprocess.call(cmd, shell=True)

def main():
    parser = argparse.ArgumentParser(description='Script to rename bam files based on sample name', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', dest='infile', type=str, help='input folder')
    parser.add_argument('-o', dest='outfile', type=str, help='destination folder')

    args = parser.parse_args()
    print(args)
    rename_file(args.infile, args.outfile)

if __name__ == "__main__":
    main()

