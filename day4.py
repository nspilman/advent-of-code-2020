import csv
import re

dataRaw = open('input/day4.txt')
# data = [item for item in dataRaw]
dataString = ''
for line in dataRaw:
    dataString = dataString + line

records_strings = dataString.split("\n\n")
records = [record.replace("\n"," ").split(" ") for record in records_strings]
print(records[0])

requiredFields = ["ecl", "pid","eyr","hcl","byr","iyr","hgt"]
def isRecordStringValid(recordString):
    keys = [field.split(':')[0] for field in recordString]
    for field in requiredFields:
        if(field not in keys):
            return False
    return True

output = 0
for record in records:
    if isRecordStringValid(record) == True:
        output = output + 1

print(output)




