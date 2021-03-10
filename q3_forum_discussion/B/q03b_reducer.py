# Question 3. Answer B. Reducer.  

import sys

current_key = None
# current_count = 0
key = None


text_file = open("q03b_answers.txt", "w")  # text with answers

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()  # remove leading and trailing whitespace
    key, post_type, post_len = line.split('\t', 2)  # split on tabulation, 2 splits

    # print(key, post_type, post_len)

    if current_key == key:
        if post_type == 'answer':
            answer_lengths.append(int(post_len))
        if post_type == 'question':
            q_len = post_len
    else:
        if current_key:
            # flushing routine
            # calculating the mean
            if answer_lengths:
                mean_len = round(sum(answer_lengths)/len(answer_lengths), 2)
            else:
                mean_len = "No answers"
            # print(current_key, q_len, mean_len, sep='\t')
            text_file.write(current_key + '\t' + str(q_len) + '\t' + str(mean_len) + '\n')
            
        # reset all statuses after flushing with print
        current_key = key
        answer_lengths = []
        if post_type == 'answer':
            answer_lengths.append(int(post_len))
        if post_type == 'question':
            q_len = post_len


# always remember to flush the final line with the same routine
if current_key == key:
    # flushing routine
    # calculating the mean
    if answer_lengths:
        mean_len = round(sum(answer_lengths)/len(answer_lengths), 2)
    else:
        mean_len = "No answers"
    # print(current_key, q_len, mean_len, sep='\t')
    text_file.write(current_key + '\t' + str(q_len) + '\t' + str(mean_len) + '\n')
    
text_file.close()