# Question 3. Answer B. Mapper. 

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')
    # input comes from STDIN (standard input)
    next(reader)  # skip first row
    for row in reader:
        # assert the proper length
        if len(row) == 19:  
            if row[5] == 'comment':  # ignore comments
                continue
            # if answer switch post id for abs_parent_id
            if row[5] == 'answer':  
                row[0] = row[7] 

            # output from the mapper: abs_parent_id, post type (Q or A), post length
            print(row[0], row[5], len(row[4]), sep='\t')


if __name__ == "__main__":
    main()
