# Question 3. Answer C. Reducer.  

import sys

current_key = None
current_count = 0
key = None
tag_count_pairs = []

text_file = open("q03c_answers.txt", "w")  # text with answers

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()  # remove leading and trailing whitespace
    key = line  # no need to split, single string parsed
    # print(key)
    if not key:
        continue

    if current_key == key:
        current_count += 1
    else:
        if current_key:
            # flushing routine
            tag_count_pairs.append([current_key, current_count])
            # text_file.write(current_key + '\t' + str(q_len) + '\t' + str(mean_len) + '\n')
        # reset all statuses after flushing
        current_key = key
        current_count = 1  # the count begins from 1 again with the new key

# always remember to flush the final line with the same routine
if current_key == key:
    # flushing routine
    tag_count_pairs.append([current_key, current_count])

# choosing top10
top_10 = sorted(tag_count_pairs, key=lambda x: x[1], reverse=True)[0:10]
for _ in top_10:
    # print(_[0], _[1], sep='\t')
    text_file.write(_[0] + '\t' + str(_[1]) + '\n')
    
text_file.close()