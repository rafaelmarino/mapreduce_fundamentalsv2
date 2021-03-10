# Question 1. Answer B. Reducer.  

import sys

current_key = None
current_count = 0
key = None


text_file = open("q01b_answers.txt", "w")  # text with answers

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()  # remove leading and trailing whitespace
    key0, key1, count = line.split('\t', 2)  # split on tabulation, 2 splits
    # print(key0, key1, count, sep='\t')
    key = key0 + '\t' + key1  # new key is comprised of store + product
    # print(key)

    try:
        count = float(count)  # convert to string
    except ValueError:
        # ignore if count is not a number
        continue

    # this IF-switch works because Hadoop sorts map output by key
    if current_key == key:  # current_key either None or prev key
        current_count += count
    else:  # there is a change
        if current_key:            
            # uncomment below print if you also want to see results in the terminal
            # print(current_key, round(current_count, 2), sep='\t')
            text_file.write(current_key + '\t' + str(round(current_count, 2)) + '\n')
        current_key = key
        current_count = count

# the first iteration doesn't print anything. Loop is shifted by 1
# do not forget to output the last word if needed!
if current_key == key:
    # uncomment below print if you also want to see results in the terminal
    # print(current_key, round(current_count, 2), sep='\t')  # python3 fix
    text_file.write(current_key + '\t' + str(round(current_count, 2)) + '\n')

text_file.close()
