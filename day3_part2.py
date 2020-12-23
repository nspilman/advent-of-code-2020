import csv

dataRaw = csv.reader(open('input/day3.csv'))
data = [list(item[0]) for item in dataRaw]

first_row = data[0]
max_x_coodinate = len(first_row)

slopes = [[1,1], [3,1], [5,1],[7,1],[1,2]]

def getTreeEncounters(slope):
    x_coodinate = 0
    tree_count = 0 
    tree = "#"
    x,y = slope
    for i in range(len(data)):
        if i % y == 0:
            row = data[i]
            if row[x_coodinate] == tree:
                tree_count = tree_count + 1
            x_coodinate = x_coodinate + x
            if(x_coodinate >= max_x_coodinate):
                x_coodinate = x_coodinate - max_x_coodinate
    return tree_count

output = 1
for slope in slopes:
    output = output * getTreeEncounters(slope)

print(output)