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
    longest_duration = -1
    temp_phone_num = ""
    for i in range(len(calls)):
        temp_duration_int = int(calls[i][3]) 
        if longest_duration < temp_duration_int:
            #3 is where the corresponding phone call's duration is stored.
            longest_duration = temp_duration_int
            temp_phone_num = calls[i][0]
    
    print( temp_phone_num,"spent the longest time,", longest_duration,"seconds, on the phone during September 2016.")
