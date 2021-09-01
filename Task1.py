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
phone_num_list = []

def phone_num_adder(phone_num_list, all_records):
    num_records = len(all_records)
    #print('current number of records is',num_records)
    for i in range(num_records):
        if all_records[i][0] not in phone_num_list:
            phone_num_list.append(all_records[i][0])
    
    return phone_num_list

if __name__ == '__main__':
    phone_num_list1 = phone_num_adder(phone_num_list, texts)
    phone_num_list2 = phone_num_adder(phone_num_list1, calls)

    count = len(phone_num_list1) + len(phone_num_list2)

    print("There are", count, "different telephone numbers in the records.")
