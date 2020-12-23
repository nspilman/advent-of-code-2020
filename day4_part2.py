import csv
import re

dataRaw = open('input/day4.txt')
# data = [item for item in dataRaw]
dataString = ''
for line in dataRaw:
    dataString = dataString + line

records_strings = dataString.split("\n\n")
records = [record.replace("\n"," ").split(" ") for record in records_strings]

def isFieldValid(key,value):
    if key == "byr":
        try:
            return 1920 <= int(value) <= 2002
        except:
            return False
    
    if key == "iyr":
        try:
            return 2010 <= int(value) <= 2020
        except:
            return False
    
    if key == "eyr":
        try:
            return 2020 <= int(value) <= 2030
        except:
            return False
    
    if key == "hgt":
        try:
            if value.endswith('cm'):
                digits = value.split('cm')[0]
                return 150 <= int(digits) <= 193
            elif value.endswith('in'):
                digits = value.split('in')[0]

                return 59 <= int(digits) <= 76
            return False
        except:
            return False
    
    if key == "hcl":
        if value[0] != '#' or len(value) != 7:
            return False

        valid_char_list = ['a','b','c','d','e','f']

        for char in value[1:]:
            try:
                _ = int(char)
            except:
                if char not in valid_char_list:
                    return False
        return True
    
    if key == 'ecl':
        allowed_eye_colors = ["amb","blu","brn", "gry", "grn", "hzl", "oth"]
        return value in allowed_eye_colors
    
    if key == 'pid':
        if len(value) != 9:
            return False
        
        try:
            _ = int(value)
            return True
        except:
            return False
    
    if key == 'cid':
        return True
            


requiredFields = ["ecl", "pid","eyr","hcl","byr","iyr","hgt"]
def isRecordStringValid(recordString):
    records = [field.split(':') for field in recordString]
    for field in requiredFields:
        if(field not in [record[0] for record in records]):
            return False
    
    for record in records:
        if isFieldValid(*record) == False:
            return False
    
    return True

output = 0
for record in records:
    if isRecordStringValid(record) == True:
        output = output + 1

print(output)




