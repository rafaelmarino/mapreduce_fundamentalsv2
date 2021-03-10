# Question 2. Answer A. Mapper. 

import sys
import re

def read_input(file):
    for line in file:
        # yield line.split('\t')  # split line into words
        yield line
        # final generator object is a list of lists
        

def main():
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)  # entire line
    # print(type(data))
    for row in data:
        row = row.replace('/', '$', 2)
        row = row[row.find('/') : row.find('HTTP')]
        row = row.strip()
        file_extensions = ['.css', '.js', '.jpg', '.jpeg', '.gif', '.txt', '.ico']
        # keep rows with files only (ie filter out non files)
        if any(extension in row for extension in file_extensions):
            print(row)

if __name__ == "__main__":
    main()
