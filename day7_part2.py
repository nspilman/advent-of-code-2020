
dataRaw = open('input/day7.txt').read().replace("bags.",'').replace("bags",'').replace("bag",'').split("\n")

test_data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".replace("bags.",'').replace("bags",'').replace("bag",'').split("\n")

recordsRaw = [record.split('contain') for record in test_data]
records = []
for record in recordsRaw:
    record_object = {}
    record_object['key'] = record[0].strip()
    values = []
    for value in record[1].split(','):
        output = {}
        if value.strip() != 'no other':
            output['count'] = value.strip()[0]
            output['bag'] =  value[2:].replace('.','').strip()
            values.append(output)
    record_object['bags'] = values
    records.append(record_object)

def getBag(initial_key):
    bags_by_key = [record for record in records if record['key'] == initial_key]
    if len(bags_by_key) == 0:
        return {}
    if len(bags_by_key) > 1:
        print(f"whoaaaa,{initial_key} has more than one value")
        return {}

    return bags_by_key[0]

initial_key = "shiny gold"
def count_child_bags(initial_key, parent_count = 1):
    root_bag = getBag(initial_key)
    child_bags = root_bag['bags']
    answer = parent_count 
    for child in child_bags:
        count = int(child['count'])
        key = child['bag']
        answer = answer + parent_count * count_child_bags(key, count)
        print(count)
    return answer
    
#     found = [record for record in records if goal in record['values']]
#     if len(found) == 0:
#         return []
#     found_keys = [record['key'] for record in found if record['key'] not in counted_bags]
#     counted_bags = counted_bags + found_keys
#     output = found_keys
#     for key in found_keys:
#         output = output + find_bags(key, counted_bags)
#     return output

# answer = len(set(find_bags(goal)))
# print(answer)
# 

answer = count_child_bags(initial_key)
print(answer -1)