"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

if __name__ == '__main__':
    #Print out the first record of texts
    first_incoming_num = texts[0][0]
    first_answering_num = texts[0][1]
    first_time = texts[0][2]
    print("First record of texts,", first_incoming_num,  "texts", first_answering_num, "at time", first_time)

    #print out the last record of calls
    num_of_calls = len(calls)
    last_incoming_num = calls[num_of_calls-1][0]
    last_answering_num = calls[num_of_calls-1][1]
    last_time = calls[num_of_calls-1][2]
    last_duration = calls[num_of_calls-1][3]
    print("Last record of calls,", last_incoming_num, "calls", last_answering_num, "at time", last_time, "lasting", last_duration, "seconds")