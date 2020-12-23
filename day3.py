import csv

dataRaw = csv.reader(open('input/day3.csv'))
data = [list(item[0]) for item in dataRaw]

first_row = data[0]
max_x_coodinate = len(first_row)
x_coodinate = 0
tree_count = 0 
tree = "#"

for row in data:
    if row[x_coodinate] == tree:
        tree_count = tree_count + 1
    x_coodinate = x_coodinate + 3
    if(x_coodinate >= max_x_coodinate):
        x_coodinate = x_coodinate - max_x_coodinate

print(tree_count)