
dataRaw = open('input/day8.txt').read().split('\n')
import thread

testData = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')

instruction = [{"command":item.split(' ')[0],"value":item.split(' ')[1]} for item in testData]
def run(commands, index = 0, accumulation = 0, breadcrum = []):
    if index in breadcrum:
        return accumulation
    breadcrum.append(index)
    try:
        command_obj = commands[index]
        command = command_obj['command']
        value = command_obj['value']
    except:
        print('oor!')
        return accumulation
    direction = value[0]
    count = int(value[1:])
    if command == "nop":
        return run(commands, index +1,accumulation, breadcrum)
    if command == 'acc':
        if direction == "+":
            accumulation = accumulation + count
        else:
            accumulation = accumulation - count
        return run(commands, index + 1, accumulation, breadcrum)
    if command == "jmp":
        if direction == "+":
            return run(commands,index + count, accumulation, breadcrum)
        else:
            return run(commands, index - count, accumulation, breadcrum)

indexes_to_change = [i for i, x in enumerate(instruction) if x['command'] in ['jmp','nop']]

def get_modified_instruction(commands,i):
    output = commands[:]
    if output[i]['command'] == 'nop':
        new_command = {'command':'jmp',"value":commands[i]['value']}
        output[i] = new_command
    elif output[i]['command'] == 'jmp':
        new_command = {'command':'nop',"value":commands[i]['value']}
        output[i] = new_command
    return output

modified_instructions_list = [get_modified_instruction(instruction[:],i) for i in indexes_to_change]
for commands in modified_instructions_list:
    output = run(commands)
    print(output)

#USING TEST DATA
# output = run(modified_instructions_list[3])
# print(output)
