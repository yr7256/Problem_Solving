import sys
input = sys.stdin.readline
commands = []
eof = False
while not eof:
    first_input = input().strip()
    if first_input:
        commands.append(first_input)
    else:
        eof = True
        break
    for _ in range(31):
        commands.append(input().strip())
    idx = 0
    adder = 0
    while True:
        try:
            command = commands[idx][:3]
            value = commands[idx][3:]
            idx += 1
            if idx == 32:
                idx = 0
            if command == '000':
                commands[int(value, 2)] = str(bin(adder)[2:])
            elif command == '001':
                adder = int(commands[int(value, 2)], 2)
            elif command == '010':
                if adder == 0:
                    idx = int(value, 2)
            elif command == '011':
                pass
            elif command == '100':
                adder -= 1
                if adder == -1:
                    adder = 255
            elif command == '101':
                adder += 1
                if adder == 256:
                    adder = 0
            elif command == '110':
                idx = int(value, 2)
            elif command == '111':
                break
        except:
            break
    answer = bin(adder)[2:]
    print((8-len(answer))*'0' + answer)
    commands = []
