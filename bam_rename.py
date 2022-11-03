# Bilgenur Baloglu
# rename names bam files
\
import numpy as np
import pandas as pd

import glob
import argparse
import json

def get_sample_name(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    # list samples
    data = data['experimentAnalysisSettings']
    data = data['barcodedSamples']
    print(data)

def main():
    parser = argparse.ArgumentParser(description='Script to rename bam files based on sample name', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', dest='infile', type=str, help='input folder')
    parser.add_argument('-o', dest='outfile', type=str, help='destination folder')

    args = parser.parse_args()
    print(args)
    get_sample_name(args.infile)

if __name__ == "__main__":
    main()

