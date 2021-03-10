# Question 3. Answer C. Mapper. 

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')
    # input comes from STDIN (standard input)
    next(reader)  # skip first row
    for row in reader:
        # assert the proper length
        if len(row) == 19:  
            if row[5] == 'question':  # work only with questions
                # print(row[2])
                tag_list = row[2].split()
                for tag in tag_list:
                    # output from the mapper: single tag
                    print(tag, sep='\t')


if __name__ == "__main__":
    main()
