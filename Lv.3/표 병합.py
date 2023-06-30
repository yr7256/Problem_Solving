def solution(commands):
    answer = []
    table = [[0]*51 for _ in range(51)]
    roots = [[[i, j] for j in range(51)] for i in range(51)]

    def find_root(r, c):
        if roots[r][c] != [r, c]:
            r1, c1 = roots[r][c]
            roots[r][c] = find_root(r1, c1)
        return roots[r][c]

    def UPDATE1(r, c, value):
        target = find_root(r, c)
        for i in range(1, 51):
            for j in range(1, 51):
                if find_root(i, j) == target:
                    table[i][j] = value

    def UPDATE2(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j] == value1:
                    table[i][j] = value2

    def MERGE(r1, c1, r2, c2):
        r1, c1 = find_root(r1, c1)
        r2, c2 = find_root(r2, c2)
        roots[r2][c2] = [r1, c1]
        if table[r1][c1]:
            UPDATE1(r2, c2, table[r1][c1])
        else:
            UPDATE1(r1, c1, table[r2][c2])

    def UNMERGE(r, c):
        target = find_root(r, c)
        value = table[r][c]
        for i in range(1, 51):
            for j in range(1, 51):
                if find_root(i, j) == target:
                    roots[i][j] = [i, j]
                    table[i][j] = 0
        table[r][c] = value

    def PRINT(r, c):
        value = table[r][c]
        if value:
            answer.append(value)
        else:
            answer.append('EMPTY')

    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            if len(command) == 4:
                UPDATE1(int(command[1]), int(command[2]), command[3])
            else:
                UPDATE2(command[1], command[2])
        elif command[0] == 'MERGE':
            MERGE(int(command[1]), int(command[2]),
                  int(command[3]), int(command[4]))
        elif command[0] == 'UNMERGE':
            UNMERGE(int(command[1]), int(command[2]))
        else:
            PRINT(int(command[1]), int(command[2]))

    return answer