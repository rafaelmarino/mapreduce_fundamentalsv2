# Question 3. Answer A. Mapper. 

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')
    # input comes from STDIN (standard input)
    next(reader)  # flush first row
    for row in reader:
        # test cases '100000066' '100071170'
        # if row[3] != '100000066':
        #     continue
        if len(row) == 19:  # assert the proper length
            date_time = row[8]
            # mapper output: student id, post hour
            print(row[3], date_time[date_time.find(':')-2:date_time.find(':')]   , sep='\t')


if __name__ == "__main__":
    main()


# container = ["id", "random_element"]
# for x in container:
#     if x == 'id':
#         continue
#     print(x)