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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
count = 0
phone_num_set = set()

def phone_num_adder(all_records):
    num_records = len(all_records)
    #print('current number of records is',num_records)
    for i in range(num_records):
        phone_num_set.add(all_records[i][0])
        phone_num_set.add(all_records[i][1])
    
    #return phone_num_set

if __name__ == '__main__':
    phone_num_adder(texts)
    phone_num_adder(calls)

    count = len(phone_num_set)

    print("There are", count, "different telephone numbers in the records.")
