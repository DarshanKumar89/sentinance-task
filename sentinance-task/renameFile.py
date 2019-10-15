import os
import shutil
from os import path

def main():
	# make a duplicate of an existing file if required
    if path.exists("sample.txt"):
	# get the path of file in the current directory
        src = path.realpath("new.txt");
		
	# rename the original file
        os.rename('job.txt','career.txt') 
		
if __name__ == "__main__    ":
    main()