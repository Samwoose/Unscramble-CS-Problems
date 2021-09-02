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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

if __name__ == '__main__':
    outgoingCalls = set()
    incomingCallsNOutgoingNIncomingTexts = set()
    #collect numbers in records
    for i in range(len(calls)):
        outgoingCalls.add(calls[i][0])
        incomingCallsNOutgoingNIncomingTexts.add(calls[i][1])
    for i in range(len(texts)):
        incomingCallsNOutgoingNIncomingTexts.add(texts[i][0])
        incomingCallsNOutgoingNIncomingTexts.add(texts[i][1])
    
    #subtracting to find the possible telemarketers
    telemarketSet = outgoingCalls.difference(incomingCallsNOutgoingNIncomingTexts)
    
    telemarketList = list(telemarketSet)
    telemarketList.sort()
    print("These numbers could be telemarketers: ")
    for number in telemarketList:
        print(number)