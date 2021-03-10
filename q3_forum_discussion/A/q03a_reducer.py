# Question 3. Answer A. Reducer.  

import sys

current_key0 = None  # outermost key layer, ie student id
current_key = None
# current_count = 0
# key = None


text_file = open("q03a_answers.txt", "w")  # text with answers

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()  # remove leading and trailing whitespace
    key0, key1 = line.split('\t', 1)  # split on tabulation, 2 splits
    # print(key0, key1, count, sep='\t')
    # key = key0 + '\t' + key1  # new key is comprised of store + product
    # print(key)

    if current_key0 == key0:  # same student id
        hour_vec[int(key1.replace("0", "", 1))] += 1  # add the extra record
    else:  # change in student id or initial status (None vs first key)
        if current_key0:
            # extract keys with highest count and pad leading 0 if required
            max_hours_vec = [k for k, v in enumerate(hour_vec) if v == max(hour_vec)]
            max_hours_pad = ["0"+str(_) if len(str(_))==1 else str(_) 
                for _ in max_hours_vec]
            for hour in max_hours_pad:
                # print(current_key0, hour, sep='\t')
                text_file.write(current_key0 + '\t' + str(hour) + '\n')
        # initialize a 24h vector right after printing
        hour_vec = [0] * 24
        hour_vec[int(key1.replace("0", "", 1))] += 1  # add the extra record
        current_key0 = key0


    # # this IF-switch works because Hadoop sorts map output by key
    # if current_key == key:  # current_key either None or prev key
    #     current_count += 1
    # else:  # there is a change
    #     if current_key:            
    #         print(current_key, round(current_count, 2), sep='\t')
    #         # text_file.write(current_key + '\t' + str(round(current_count, 2)) + '\n')
    #     # start counting from 1    
    #     current_key = key
    #     current_count = 1

# always remember to flush the final line with the same routine
if current_key0 == key0:
    # extract keys with highest count and pad leading 0 if required
    max_hours_vec = [k for k, v in enumerate(hour_vec) if v == max(hour_vec)]
    max_hours_pad = ["0"+str(_) if len(str(_))==1 else str(_) 
        for _ in max_hours_vec]    
    for hour in max_hours_pad:
        # print(current_key0, hour, sep='\t')
        text_file.write(current_key0 + '\t' + str(hour) + '\n')
    
text_file.close()