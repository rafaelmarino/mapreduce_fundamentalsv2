# Question 3. Answer D. Mapper. 

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')
    # input comes from STDIN (standard input)
    next(reader)  # skip first row
    for row in reader:
        # assert the proper length
        if len(row) == 19:
            if row[5] in ['answer', 'comment']:
                question_id = row[7]  # the abs_parent_id becomes the question id
            else:
                question_id = row[0]                        

            # output from the mapper: question_id, author_id
            print(question_id, row[3], sep='\t')
        


if __name__ == "__main__":
    main()
