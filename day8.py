
dataRaw = open('input/day8.txt').read().split('\n')
testData = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')

print(testData)
commands = [{"command":item.split(' ')[0],"value":item.split(' ')[1]} for item in dataRaw]
print(commands)
def run(commands, index = 0, accumulation = 0, breadcrum = []):
    if index in breadcrum:
        print(accumulation)
        return accumulation
    breadcrum.append(index)
    command_obj = commands[index]
    command = command_obj['command']
    value = command_obj['value']
    direction = value[0]
    count = int(value[1:])
    if command == "nop":
        run(commands, index +1,accumulation, breadcrum)
    if command == 'acc':
        if direction == "+":
            accumulation = accumulation + count
        else:
            accumulation = accumulation - count
        run(commands, index + 1, accumulation, breadcrum)
    if command == "jmp":
        if direction == "+":
            run(commands,index + count, accumulation, breadcrum)
        else:
            run(commands, index - count, accumulation, breadcrum)
        
print(run(commands))

