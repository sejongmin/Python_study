import sys
read = sys.stdin.readline

cube = [
    [['w'] * 3 for _ in range(3)], #위
    [['y'] * 3 for _ in range(3)], #아래
    [['r'] * 3 for _ in range(3)], #앞
    [['o'] * 3 for _ in range(3)], #뒤
    [['g'] * 3 for _ in range(3)], #왼
    [['b'] * 3 for _ in range(3)]  #오른
]


def play(n, order):
    cube_copy = [item[:] for item in cube]
    # 위 0, 아래 1, 앞 2, 뒤 3, 왼 4, 오른 5
    # 위 0, 아래 2, 왼쪽 1, 오른쪽 3
    for s in range(n):
        if order[s][0] == 'U':
            arr = [[2, 0], [5, 0], [3, 0], [4, 0], 0]
        elif order[s][0] == 'D':
            arr = [[2, 2], [4, 2], [3, 2], [5, 2], 1]
        elif order[s][0] == 'F':
            arr = [[0, 2], [5, 1], [1, 0], [4, 3], 2]
        elif order[s][0] == 'B':
            arr = [[0, 0], [4, 1], [1, 2], [5, 3], 3]
        elif order[s][0] == 'L':
            arr = [[0, 1], [2, 1], [1, 1], [3, 1], 4]
        elif order[s][0] == 'R':
            arr = [[0, 3], [3, 3], [1, 3], [2, 3], 5]

        tmp = [[] for _ in range(4)]
        for i in range(4):
            if arr[i][1] == 0:
                tmp[i].append(cube_copy[arr[i][0]][arr[i][1]][0])
                tmp[i].append(cube_copy[arr[i][0]][arr[i][1]][1])
                tmp[i].append(cube_copy[arr[i][0]][arr[i][1]][2])
            elif arr[i][1] == 1:
                tmp[i].append(cube_copy[arr[i][0]][2][0])
                tmp[i].append(cube_copy[arr[i][0]][1][0])
                tmp[i].append(cube_copy[arr[i][0]][0][0])
            elif arr[i][1] == 2:
                tmp[i].append(cube_copy[arr[i][0]][arr[i][1]][2])
                tmp[i].append(cube_copy[arr[i][0]][arr[i][1]][1])
                tmp[i].append(cube_copy[arr[i][0]][arr[i][1]][0])
            elif arr[i][1] == 3:
                tmp[i].append(cube_copy[arr[i][0]][0][2])
                tmp[i].append(cube_copy[arr[i][0]][1][2])
                tmp[i].append(cube_copy[arr[i][0]][2][2])

        for i in range(0, 4):
            if order[s][1] == '+':
                k = i - 1 if i > 0 else 3
            else:
                k = i + 1 if i < 3 else 0

            if arr[i][1] == 0:
                cube_copy[arr[i][0]][arr[i][1]][0] = tmp[k][0]
                cube_copy[arr[i][0]][arr[i][1]][1] = tmp[k][1]
                cube_copy[arr[i][0]][arr[i][1]][2] = tmp[k][2]
            elif arr[i][1] == 1:
                cube_copy[arr[i][0]][2][0] = tmp[k][0]
                cube_copy[arr[i][0]][1][0] = tmp[k][1]
                cube_copy[arr[i][0]][0][0] = tmp[k][2]
            elif arr[i][1] == 2:
                cube_copy[arr[i][0]][arr[i][1]][2] = tmp[k][0]
                cube_copy[arr[i][0]][arr[i][1]][1] = tmp[k][1]
                cube_copy[arr[i][0]][arr[i][1]][0] = tmp[k][2]
            elif arr[i][1] == 3:
                cube_copy[arr[i][0]][0][2] = tmp[k][0]
                cube_copy[arr[i][0]][1][2] = tmp[k][1]
                cube_copy[arr[i][0]][2][2] = tmp[k][2]

        temp = []
        temp.append(cube_copy[arr[4]][2][0])
        temp.append(cube_copy[arr[4]][1][0])
        temp.append(cube_copy[arr[4]][0][0])
        if order[s][1] == '+':
            cube_copy[arr[4]][2][0] = cube_copy[arr[4]][2][2]
            cube_copy[arr[4]][1][0] = cube_copy[arr[4]][2][1]
            cube_copy[arr[4]][0][0] = cube_copy[arr[4]][2][1]

            cube_copy[arr[4]][2][2] = cube_copy[arr[4]][0][2]
            cube_copy[arr[4]][2][1] = cube_copy[arr[4]][1][2]
            cube_copy[arr[4]][2][1] = cube_copy[arr[4]][2][2]

            cube_copy[arr[4]][0][2] = cube_copy[arr[4]][0][0]
            cube_copy[arr[4]][1][2] = cube_copy[arr[4]][0][1]
            cube_copy[arr[4]][2][2] = cube_copy[arr[4]][0][2]

            cube_copy[arr[4]][0][0] = temp[0]
            cube_copy[arr[4]][0][1] = temp[1]
            cube_copy[arr[4]][0][2] = temp[2]
        else:
            cube_copy[arr[4]][2][0] = cube_copy[arr[4]][0][0]
            cube_copy[arr[4]][1][0] = cube_copy[arr[4]][0][1]
            cube_copy[arr[4]][0][0] = cube_copy[arr[4]][0][1]

            cube_copy[arr[4]][0][0] = cube_copy[arr[4]][0][2]
            cube_copy[arr[4]][0][1] = cube_copy[arr[4]][1][2]
            cube_copy[arr[4]][0][2] = cube_copy[arr[4]][2][2]

            cube_copy[arr[4]][0][2] = cube_copy[arr[4]][2][2]
            cube_copy[arr[4]][1][2] = cube_copy[arr[4]][2][1]
            cube_copy[arr[4]][2][2] = cube_copy[arr[4]][2][0]

            cube_copy[arr[4]][2][2] = temp[0]
            cube_copy[arr[4]][2][1] = temp[1]
            cube_copy[arr[4]][2][0] = temp[2]

    print(cube_copy[0])
    print()

T = int(read().strip())
for _ in range(T):
    N = int(read().strip())
    order = list(read().split())
    play(N, order)