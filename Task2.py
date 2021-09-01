"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

if __name__ == '__main__':
    phone_dict = {}
    for i in range(len(calls)): 

        #calling
        if calls[i][0] not in phone_dict.keys():
            phone_dict[calls[i][0]] = int(calls[i][3])
        else: 
            phone_dict[calls[i][0]] = phone_dict[calls[i][0]] + int(calls[i][3])
        #receiving
        if calls[i][1] not in phone_dict.keys():
            phone_dict[calls[i][1]] = int(calls[i][3])
        else: 
            phone_dict[calls[i][1]] = phone_dict[calls[i][1]] + int(calls[i][3])
    #find key with the longest accumlated duration
    longest_phone_num = max(phone_dict, key=phone_dict.get)
    longest_duration = phone_dict[longest_phone_num]

    print( longest_phone_num,"spent the longest time,", longest_duration,"seconds, on the phone during September 2016.")
