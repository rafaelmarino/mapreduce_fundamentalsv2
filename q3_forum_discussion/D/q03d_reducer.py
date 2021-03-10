# Question 3. Answer D. Reducer.  

import sys

current_key = None
current_count = 0
key = None
user_list = []

text_file = open("q03d_answers.txt", "w")  # text with answers

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()  # remove leading and trailing whitespace
    key, user = line.split('\t', 1)  # no need to split, single string parsed
    # print(key)
    if not key:
        continue

    if current_key == key:
        user_list.append(user)
    else:
        if current_key:
            # flushing routine
            # print(current_key, user_list, sep='\t')
            text_file.write(current_key + '\t' + str(user_list) + '\n')
        # reset all statuses after flushing
        current_key = key
        user_list = []  # begin the list again from scratch if key changes
        user_list.append(user)

# always remember to flush the final line with the same routine
if current_key == key:
    # flushing routine
    # print(current_key, user_list, sep='\t')
    text_file.write(current_key + '\t' + str(user_list) + '\n')
    
text_file.close()