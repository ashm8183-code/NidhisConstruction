n = int(input())

commands = []

for i in range(n):
    a, b, direction = input().split()
    commands.append((int(a), int(b), direction))

commands.sort()

position = {}
position[1] = (0, 0)

board = {}
board[(0, 0)] = 1

for a, b, direction in commands:

    row, col = position[a]

    if direction == "top":
        row = row - 1
    elif direction == "down":
        row = row + 1
    elif direction == "left":
        col = col - 1
    elif direction == "right":
        col = col + 1

    if (row, col) in board:
        old_cube = board[(row, col)]
        del position[old_cube]

    position[b] = (row, col)
    board[(row, col)] = b

target = int(input())

row, col = position[target]

up = board.get((row - 1, col), -1)
down = board.get((row + 1, col), -1)
left = board.get((row, col - 1), -1)
right = board.get((row, col + 1), -1)

print(up, down, left, right)
