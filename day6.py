
dataRaw = open('input/day6.txt').read().split("\n\n")
response_groups = [record.split('\n') for record in dataRaw]

def get_group_yes_count(group):
    flattened_group = []
    for record in group:
        flattened_group.extend(record)
    unique_yes_answers = set(flattened_group)
    # group_yes_count = 0 
    # for possible_answer in unique_yes_answers:
    #     possible_answer_not_in_record = None
    #     for record in group:
    #         if possible_answer not in [char for char in record]: 
    #             possible_answer_not_in_record = True
    #     if possible_answer_not_in_record == None:
    #         group_yes_count = group_yes_count + 1
    return len(unique_yes_answers)



answer = 0
for group in response_groups:
    answer = answer + get_group_yes_count(group)
# answer = get_group_yes_count(response_groups[1])
# print(response_groups[1])
print(answer)
