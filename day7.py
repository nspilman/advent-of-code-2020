
dataRaw = open('input/day7.txt').read().replace("bags.",'').replace("bags",'').replace("bag",'').split("\n")

test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".replace("bags.",'').replace("bags",'').replace("bag",'').split("\n")

recordsRaw = [record.split('contain') for record in dataRaw]
records = []
for record in recordsRaw:
    record_object = {}
    record_object['key'] = record[0].strip()
    values = []
    for value in record[1].split(','):
        output = value[2:].replace('.','').strip()
        values.append(output)
    record_object['values'] = values
    records.append(record_object)

goal = "shiny gold"
def find_bags(goal, counted_bags = []):
    found = [record for record in records if goal in record['values']]
    if len(found) == 0:
        return []
    found_keys = [record['key'] for record in found if record['key'] not in counted_bags]
    counted_bags = counted_bags + found_keys
    output = found_keys
    for key in found_keys:
        output = output + find_bags(key, counted_bags)
    return output

answer = len(set(find_bags(goal)))
print(answer)
