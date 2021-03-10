# Question 2. Answer A. Reducer.  

import sys

current_key = None
current_count = 0
# key = None  # no need to initialize first in Python


text_file = open("q02a_answers.txt", "w")  # text with answers 

# input comes from STDIN
for line in sys.stdin:
    key = line.strip()  # remove leading and trailing whitespace
    # key, value = line.split()  # split on tabulation, 1 split

    # try:
    #     value = float(value)  # convert to string
    # except ValueError:
    #     # ignore if count is not a number
    #     continue

    # this IF-switch works because Hadoop sorts map output by key
    if current_key == key:  # current_key either None or prev key
        current_count += 1
    else:  # there is a change
        if current_key:                        
            # print(current_key, current_count, sep='\t')  # python3 fix
            text_file.write(current_key + '\t' + str(current_count) + '\n')
        current_key = key
        current_count = 1

# the first iteration doesn't print anything. Loop is shifted by 1
# do not forget to output the last word if needed!
if current_key == key:
    # print(current_key, current_count, sep='\t')  # python3 fix
    text_file.write(current_key + '\t' + str(current_count) + '\n')

# text_file.close()
