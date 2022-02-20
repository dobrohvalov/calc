import random

width = 3
height = 3
quantity = 3


def create_board(width, height):
    board = []
    for i in range(height):
        boardline = []
        for n in range(width):
            boardline.append(0)
        board.append(boardline)
    return board


def draw_board(board):
    for i in board:
        print(i)


def firstPlayer(playerFirst, playerSecond):
    # Определяем, кто первый начинает
    if random.randint(0, 1) == 0:
        return playerFirst
    else:
        return playerSecond


def check_win(board):
    # Определяем, есть ли выиграшные комбинации и кто выиграл
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    # for each in win_coord:
    #     if board[each[0]] == board[each[1]] == board[each[2]]:
    #         return board[each[0]]
    return False


def choice(board, token):
    # Проверяем наличие свободных мест
    empty = False
    for i in board:
        for n in i:
            if n == 0:
                empty = True
    # Сначала ищем подряд идущие элементы противника,
    if token == 1:
        for i in board:
            counter = 0
            for n in i:
                if n ==
    # Проверяем наличие ходов,
    # Проверяем есть ли рядом свободные места
    # Проверяем центр
    # Проверяем углы

    player_answer = 4
    return player_answer


def take_input(player_token, board):
    # Делаем ход.
    occupied = False
    token = 0
    # choice(board)
    if player_token == 'X':
        token = 1
    elif player_token == '0':
        token = 2
    choice(board, token) = token
    return board
    # occupied = True


def play(width, height, quantity):
    # Осноная фунция игры
    request = []
    PlayerX = 'X'
    Player0 = '0'
    playerFirst = 1
    playerSecond = 2

    if firstPlayer(playerFirst, playerSecond) == 1:
        playerFirst = PlayerX
        playerSecond = Player0
    else:
        playerSecond = PlayerX
        playerFirst = Player0
    counter = 0
    board = create_board(width, height)
    win = False
    while not win:
        if counter % 2 == 0:
            board = take_input(PlayerX, board)
        else:
            board = take_input(Player0, board)
        counter += 1
        if counter > quantity*2-1:
            tmp = check_win(board)
            if tmp:
                request = {"Выиграл игрок 1"}
                win = True
        if counter == width*height:
            request = 'Ничья'
            break
    return draw_board(board), request


play(width, height, quantity)
