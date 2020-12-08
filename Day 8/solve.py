import copy
with open("input.txt", "r") as f:
    program = f.read().split("\n")
    program = [i.split() for i in program]
    for i in program:
        i[1] = int(i[1])
        i.append(False)
def Run(program):
    pos = 0
    accumulator = 0
    repeated = False
    while True:
        if program[pos][2] == True:
            repeated = True
            break
        elif pos > int(len(program))-1:
            break
        if program[pos][0] == "nop":
            program[pos][2] = True
            pos+=1
            if pos > int(len(program))-1:
                break
        elif program[pos][0] == "acc":
            program[pos][2] = True
            accumulator += program[pos][1]
            pos+=1
            if pos > int(len(program))-1:
                break
        elif program[pos][0] == "jmp":
            program[pos][2] = True
            pos+=program[pos][1]
            if pos > int(len(program))-1:
                break
    return (accumulator, repeated)
def Fix(x, y):
    global program
    if i[0] == x:
        programCopy = copy.deepcopy(program)
        programCopy[programCopy.index(i)][0] = y
        result = Run(programCopy)
        if result[1] == False:
            print(result)
for i in program:
    if i[0] == "nop":
        Fix("nop", "jmp")
    elif i[0] == "jmp":
        Fix("jmp", "nop")
