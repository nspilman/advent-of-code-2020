
data = open('input/day5.txt').read().split("\n")

rows = [i for i in range(0,128)]
columns = [i for i in range(8)]
grid = {"rows":rows, "columns":columns}

def find_seat(instructions, grid):
    current_rows = grid['rows']
    current_columns = grid['columns']

    for instruction in instructions:
        middle_point_x = int(round(len(current_rows) / 2))
        middle_point_y = int(round(len(current_columns) / 2))
        if instruction == 'F':
            # Keep Lower Half
            current_rows = current_rows[0:middle_point_x]
        elif instruction == "B":
            # Keep Upper Half
            current_rows = current_rows[middle_point_x:]
        elif instruction == "L":
            current_columns = current_columns[0:middle_point_y]
        elif instruction == "R":
            current_columns = current_columns[middle_point_y:]
    return (current_rows[0], current_columns[0])

def gen_seat_id(row,column, multiplier = 8):
    return row * multiplier + column

seat_ids = []
for instruction_record in data:
    seat = find_seat(instruction_record, grid)
    seat_id = gen_seat_id(*seat)
    seat_ids.append(seat_id)

seat_ids.sort()
print(len(seat_ids))
all_seats = ["*" for i in range(seat_ids[-1])]
for seat in seat_ids:
    print(seat)
    all_seats[seat-1] = seat

print(all_seats)


