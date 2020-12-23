import csv

dataRaw = csv.reader(open('input/day2.csv'))
data = [item[0] for item in dataRaw]
def createPasswordObject(password_string):
    output = {}
    raw = password_string.split(' ')
    bounds = raw[0].split('-')
    output['lower'],output['upper'] = [int(bound) for bound in bounds]
    output['value'] = raw[1].split(':')[0]
    output['password'] = raw[2]
    return output

def isPasswordValid(passwordObject):
    value_array = [char for char in passwordObject['password'] if char == passwordObject['value']]
    print(value_array)
    return passwordObject['lower'] <= len(value_array) <= passwordObject['upper']

passwordObjects = [createPasswordObject(password) for password in data]
answer = 0
for password in passwordObjects:
    if isPasswordValid(password) == True:
        answer = answer + 1

print(answer)
    