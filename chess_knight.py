# board = [[0, 0, 0, 0, "x"],
#          [0, 0, 1, 0, 0],
#          [0, 0, 0, 2, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0]]

# added comment
# board = [[1, 4, 7, 10], [12, 9, 2, 5], [3, 6, 11, 8]]
board = []


def create_board(row, col, x, y):
    global cell_size
    for a in range(row):
        board.append([])
        for _ in range(col):
            board[a].append(0)

    board[len(board) - y][x - 1] = 1

    if x >= 4 or y >= 4:
        cell_size = 1
    elif x > 9 or y > 9:
        cell_size = 2
    else:
        cell_size = 0


def number_of_moves(x, y):
    positions = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
    moves = 0
    temp = 0

    for a in range(len(positions)):
        for b in range(2):
            positions[a][b] += [x, y][b]

    for z in positions:
        try:
            if z[0] < 0 or z[1] < 0:
                raise IndexError
            temp = board[z[0]][z[1]]
            moves += 1
        except IndexError:
            continue

    return moves


def possible_moves(x, y):
    positions = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
    moves_dict = {}
    moves = 0
    temp = 0

    last_index = 0

    for xc in range(len(board)):
        for yc in range(len(board[0])):
            if board[xc][yc] > last_index:
                last_index = board[xc][yc]

    if x == -1 and y == -1:
        pass

    for a in range(len(positions)):
        for b in range(2):
            positions[a][b] += [x, y][b]

    for z in positions:
        try:
            if z[0] < 0 or z[1] < 0:
                raise IndexError
            elif board[z[0]][z[1]] != 0:
                raise IndexError
            elif board[z[0]][z[1]] == 0:
                temp = board[z[0]][z[1]]
                moves_dict[tuple(z)] = 0
        except IndexError:
            continue

    for z in positions:
        try:
            if z[0] < 0 or z[1] < 0:
                raise IndexError
            temp = board[z[0]][z[1]]
            moves += 1
        except IndexError:
            continue

    for x in moves_dict.keys():
        moves_dict[x] = number_of_moves(x[0], x[1])

    return moves_dict


def next_title():
    for x in possible_moves(-1, -1):
        if board[x[0]][x[1]] == 0:
            return x[0], x[1]
        else:
            return None, None


def print_board():
    this_row = ""
    for x in board:
        for y in x:
            if y == 0:
                this_row += " __"
            elif y == "x":
                this_row += " _X"
            elif y == "O":
                this_row += " _O"
            else:
                this_row += " {}".format(y)
        print(this_row)
        this_row = ""
    print("\n")


def print_status():
    row_length = len(board)
    col_length = len(board[0])
    line_length = (col_length * (cell_size + 3)) + 3
    cell_str = [["_ ", "__ ", "___ "], ["X ", " X ", "  X "], ["{} ", " {} ", "  {} "]]
    cell_space = [" ", "  ", "   "]
    print(" " + "-" * line_length)

    for x in range(row_length):
        this_row = ""
        for y in board[x]:
            if y == 0:
                this_row += cell_str[0][cell_size]
            elif y == 'x':
                this_row += cell_str[1][cell_size]
            elif y == "*":
                this_row += cell_str[2][cell_size].format(y)
            elif type(y) == int:
                if len(str(y)) == 1:
                    this_row += " " + str(y) + " "
                elif len(str(y)) == 2:
                    this_row += str(y) + " "
        print(f"{row_length - x}| {this_row}|")

    columns = ''

    if cell_size > 0:
        columns = " "
        for x in range(col_length):
            columns += str(x + 1) + cell_space[cell_size]
    else:
        columns = " "
        for x in range(col_length):
            columns += str(x + 1) + "  "

    print(" " + "-" * line_length)
    print(f'   {columns}')


def zero_in_board():
    for row in board:
        if 0 in row:
            return True
    else:
        return False


def solve():
    global board
    last_index = 0

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] > last_index:
                last_index = board[x][y]
                xc, yc = x, y

    for move in possible_moves(xc, yc):
        if board[move[0]][move[1]] == 0:
            board[move[0]][move[1]] = last_index + 1
        if solve():
            return True
        board[move[0]][move[1]] = 0

    if zero_in_board():
        return False
    else:
        return True


create_board(8,8,1,1)
if solve():
    print_status()
else:
    print("0")
