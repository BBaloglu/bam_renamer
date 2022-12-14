# Bilgenur Baloglu

"""renames bam, bai, and sam file names from a selected run using sample names
moves them to the mounted hard drive"""

import glob
import json
import argparse
import subprocess
import os
import os.path
import shutil

def get_sample_name(fname):
    """extracts sample names from the json file"""
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

def rename_file(infolder, outfolder, sample_list):
    """renames files based on the names in the sample list"""
    # make output directory if it does not exist
    if os.path.exists(outfolder)==False:
        cmd = 'mkdir '+outfolder
        print(cmd)
        subprocess.call(cmd, shell=True)

    # iterate thru file list
    for f1, f2 in sample_list:
        print('working on', f1, f2)
        # get list of bam files
        blist = glob.glob(infolder+'/'+f2+'*.bam*')
        print(blist)
        # rename bam file and copy over
        for bfile in blist:
            outname = outfolder+'/'+f1+'_'+bfile.split('/')[-1]
            ## need to add a few other conditions to address any kind of file naming
            # if the filename contains spaces, replace with underscore
            if outname.find(" ")!=-1:
                outname = outname.replace(' ','_')
            else:
                pass
            cmd = 'touch '+outname
            print(cmd)
            subprocess.call(cmd, shell=True)
            cmd = 'cp '+bfile+' '+outname
            print(cmd)
            #subprocess.call(cmd, shell=True)

def main():
    parser = argparse.ArgumentParser(description='Script to rename bam files based on sample name', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-c', dest='run_params', type=str, help='file with run parameters')
    parser.add_argument('-i', dest='infile', type=str, help='input folder')
    parser.add_argument('-o', dest='outfile', type=str, help='destination folder')

    args = parser.parse_args()
    print(args)
    flist = get_sample_name(args.run_params)
    rename_file(args.infile, args.outfile, flist)

if __name__ == "__main__":
    main()

