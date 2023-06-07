#!/usr/bin/python
# # -*- coding: utf-8 -*-

"""
@Authors Jerry Gao & HB
"""
# Usage
# python clean_up_solutions.py solutions_dir number_of_top_candidate_retained
# Write a file for the best fit correlation for each domain as a summary

import sys,os
import pandas as pd

def print_usage ():
    print("usage: python clean_up_solutions.py solutions_dir number_of_top_candidate_retained")
    print("eg: python clean_up_solutions.py solutions_density1 10")
    sys.exit()
    
def execute(cmd):
    print(f'start {cmd}', datetime.now())
    return subprocess.call(cmd,shell=True)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print_usage()

    # Check operating system
    useMacOs = 0
    print("Platform: " + sys.platform)

    if sys.platform == 'darwin': #MacOS
        useMacOs = 1
    
    sol_dir = sys.argv[1]
    noRemain = int(sys.argv[2])
	
	
    df = pd.read_csv(sol_dir + '/fit_logs_revised.csv', skiprows=range(1, noRemain))
    delete_names = df['Domain'].tolist()
    delete_file_names = [filename + suffix for filename in delete_names for suffix in ["_bestfit.pdb", "_pvalues.csv", ".csv"]]

    for filename in delete_file_names:
        file_path = os.path.join(sol_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)