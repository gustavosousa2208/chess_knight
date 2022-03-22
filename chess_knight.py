# board = [[0, 0, 0, 0, "x"],
#          [0, 0, 1, 0, 0],
#          [0, 0, 0, 2, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0]]

# added comment
# board = [[1, 4, 7, 10], [12, 9, 2, 5], [3, 6, 11, 8]]
board = []


def create_board(row, col, x, y):
    for a in range(row):
        board.append([])
        for _ in range(col):
            board[a].append(0)

    board[len(board) - y][x - 1] = 1


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
        print_board()
        if solve():
            return True
        board[move[0]][move[1]] = 0

    if not zero_in_board():
        return True


create_board(3, 4, 1, 3)
solve()