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
    value_array = [char for char in passwordObject['password']]
    expected = passwordObject['value']
    lower = passwordObject['lower'] -1
    upper = passwordObject['upper'] -1
    print(value_array[lower])
    if (value_array[lower] == expected and value_array[upper] == expected):
        return False
    return (value_array[lower] == expected or value_array[upper] == expected)

passwordObjects = [createPasswordObject(password) for password in data]
answer = 0
for password in passwordObjects:
    if isPasswordValid(password) == True:
        answer = answer + 1

print(answer)
    