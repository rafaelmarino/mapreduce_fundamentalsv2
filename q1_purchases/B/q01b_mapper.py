# Question 1. Answer B. Mapper. 

import sys

def read_input(file):
    for line in file:
        yield line.split('\t')  # split line into words
        # final generator object is a list of lists
        

def main():
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)  # entire line
    # print(type(data))
    for row in data:
        print(row[2], row[3], row[4], sep='\t')  # store, prod_cat, sales

if __name__ == "__main__":
    main()
