# Question 1. Answer D. Reducer.  

import sys

current_key = None
current_value = 0
current_count = 0
key = None


text_file = open("q01d_answers.txt", "w")  # text with answers

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()  # remove leading and trailing whitespace
    key, value = line.split('\t', 1)  # split on tabulation, 1 split

    try:
        value = float(value)  # convert to string
    except ValueError:
        # ignore if count is not a number
        continue

    # this IF-switch works because Hadoop sorts map output by key
    if current_key == key:  # current_key either None or prev key
        current_value += value  # take the max between prev and current
        current_count += 1  # add 1 if the key is equal to prev key
    else:  # there is a change
        if current_key:
            # print(current_key, round(current_value, 2), 
            # current_count, sep='\t')
            text_file.write(current_key + '\t' + str(round(current_value, 2)) +
            '\t' + str(current_count) + '\n')
        current_key = key
        current_value = value
        current_count = 1  # begin counter of new word with 1

# the first iteration doesn't print anything. Loop is shifted by 1
# do not forget to output the last word if needed!
if current_key == key:
    # print(current_key, round(current_value, 2), current_count, sep='\t')
    text_file.write(current_key + '\t' + str(round(current_value, 2)) +
    '\t' + str(current_count) + '\n')

text_file.close()
