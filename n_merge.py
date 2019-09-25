import sys
import os
import glob
import pandas as pd
a = sys.argv[1]
b = sys.argv[2]
def concatenate(indir , outfile):
    c=0
    os.chdir(indir)
    filelist =glob.glob("*.xlsx")
    dflist = []
    for filename  in filelist:
        c+=1
        print(c)
        df = pd.read_excel(filename)
        dflist.append(df)      
    concatdf = pd.concat(dflist , axis= 0)
    concatdf.to_csv(outfile,  encoding = 'utf-8')
    
    print("total files read " + str(c))
    print("--**Data Is Merged**--")
    
concatenate(a,b)
