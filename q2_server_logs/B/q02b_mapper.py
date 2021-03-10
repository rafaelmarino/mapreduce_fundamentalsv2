# Question 1. Answer B. Mapper. 

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
        row = row[:row.find('-')].strip()
        print(row)

if __name__ == "__main__":
    main()
