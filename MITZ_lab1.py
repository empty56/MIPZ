import sys

lines = 19
file_name = "input1.txt"


def check_winner(board):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Right, Down, Diagonal, Anti-Diagonal
    for i in range(lines):
        for j in range(lines):
            if board[i][j] == 0:
                continue

            for dx, dy in directions:
                consecutive_forward = count_consecutive(board, i, j, dx, dy)
                consecutive_backward = count_consecutive(board, i, j, -dx, -dy)
                total_consecutive = consecutive_forward + consecutive_backward - 1
                if total_consecutive == 5 and (dx != 1 or dy != -1):
                    return board[i][j], i + 1, j + 1
                if total_consecutive == 5 and dx == 1 and dy == -1:
                    return board[i][j], i + 5, j - 3
    return 0, 0, 0


def count_consecutive(board, row, col, dx, dy):
    consecutive = 0
    x, y = row, col

    while 0 <= x < lines and 0 <= y < lines and board[x][y] == board[row][col]:
        consecutive += 1
        x += dx
        y += dy

    return consecutive


def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count


with open(file_name, "r") as file:
    test_cases = int(file.readline().strip())
    line_count = count_lines(file_name)
    if (line_count - 1) % lines != 0:
        print("Wrong number of lines")
        sys.exit()
    for _ in range(test_cases):
        board = []
        for _ in range(lines):
            row = list(map(int, file.readline().split()))
            board.append(row)

        winner, row, col = check_winner(board)

        if winner == 0:
            print(0)
        else:
            print(winner)
            print(row, col)
