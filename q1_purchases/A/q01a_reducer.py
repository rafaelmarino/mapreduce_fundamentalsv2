# Question 1. Answer A. Reducer.  

import sys

current_key = None
current_value = 0
key = None


text_file = open("q01a_answers.txt", "w")  # text with answers 

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
        current_value += value
    else:  # there is a change
        if current_key:            
            # print '%s\t%s' % (current_key, current_value)
            # print(current_key, round(current_value, 2), sep='\t')  # python3 fix
            text_file.write(current_key + '\t' + str(round(current_value, 2)) + '\n')
        current_key = key
        current_value = value

# the first iteration doesn't print anything. Loop is shifted by 1
# do not forget to output the last word if needed!
if current_key == key:
    # print(current_key, round(current_value, 2), sep='\t')  # python3 fix
    text_file.write(current_key + '\t' + str(round(current_value, 2)) + '\n')

text_file.close()
