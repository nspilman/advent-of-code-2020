import csv

dataRaw = csv.reader(open('input/day1.csv'))
data = [int(item[0]) for item in dataRaw]
# Sort the data to get the lowest value
goal_value = 2020
data.sort()
data_without_impossibly_high_values = [value for value in data if value + data[0] < goal_value]
for firstParam in data_without_impossibly_high_values:
    secondParams = [secondParam for secondParam in data_without_impossibly_high_values if firstParam + secondParam < goal_value]
    for second in secondParams:
        current = firstParam + second
        thirdParams = [thirdParams for thirdParams in secondParams if current + thirdParams == goal_value]
        if len(thirdParams) > 0:
            print(firstParam * second * thirdParams[0])
        # current = value + data_without_impossibly_high_values[i]
        # if(current == goal_value): 
        #     print(value * data_without_impossibly_high_values[index])
        # index = index-1
        

