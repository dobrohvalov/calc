import random


class crosszero:
    def __init__(self, width, height, quantity):
        self.width = width
        self.height = height
        self.quantity = quantity

    # Проверяем, что бы не крестик или нолик, за рамками поля

    def check(self, i, n):
        if 0 <= i <= self.height and 0 <= n <= self.width:
            return True

    # Делаем выбор куда пойти
    @staticmethod
    def enumeration(board, width, height, quantity, t):
        flag = False
        while not flag:
            print(board)
            if board[0][0] == t and board[1][1] == t and board[2][2] == t:
                flag = True
            elif board[0][2] == t and board[1][1] == t and board[2][0] == t:
                flag = True
            else:
                # Проверяем строки
                for i in range(0, height):
                    counter = 0
                    for n in range(0, width):
                        if board[i][n] == t:
                            counter += 1
                        if counter == quantity:
                            flag = True
                            break
                # Проверяем столбцы
                for i in range(0, width):
                    counter = 0
                    for n in range(0, height):
                        if board[n][i] == t:
                            counter += 1
                        if counter == quantity:
                            flag = True
                            break
                if not flag:
                    break
        return flag

    # Проверка на пустые ячейки
    @staticmethod
    def empty(board):
        for i in board:
            for n in i:
                if n == 0:
                    return True

    # Определяем, кто первый начинает
    @staticmethod
    def firstPlayer():
        if random.randint(0, 1) == 0:
            return 0
        else:
            return 1

    # Создаем доску
    @staticmethod
    def create_board(width, height):
        board = []
        for i in range(height):
            boardline = []
            for n in range(width):
                boardline.append(0)
            board.append(boardline)
        return board

    # Рисуем доску
    @staticmethod
    def draw_board(board):
        b = []
        for i in board:
            b.append(i)
        return b

    # Проверяем есть ли у нас ходы, и ставим рядом
    def choice(self, board, token, width, height):
        motion = False
        if self.empty(board):
            # Проверяем ходили мы раньше
            for i in range(0, height - 1):
                for n in range(0, width - 1):
                    if board[i][n] == token:
                        # ставим рядом со своими ходами
                        if 0 <= (i + 1) <= height:
                            if board[i + 1][n] == 0:
                                board[i + 1][n] = token
                                motion = True
                                break
                            if self.check(i + 1, n + 1):
                                if board[i + 1][n + 1] == 0:
                                    board[i + 1][n + 1] = token
                                    motion = True
                                    break
                            if self.check(i + 1, n - 1):
                                if not board[i + 1][n - 1]:
                                    board[i + 1][n - 1] = token
                                    motion = True
                                    break
                        elif 0 <= (i - 1) <= height:
                            if not board[i - 1][n]:
                                board[i - 1][n] = token
                                motion = True
                                break
                            if self.check(i - 1, n - 1):
                                if not board[i - 1][n - 1]:
                                    board[i - 1][n - 1] = token
                                    motion = True
                                    break
                            if self.check(i - 1, n + 1):
                                if not board[i - 1][n + 1]:
                                    board[i - 1][n + 1] = token
                                    motion = True
                                    break
                        elif 0 <= i <= height:
                            if self.check(i, n + 1):
                                if not board[i][n + 1]:
                                    board[i][n + 1] = token
                                    motion = True
                                    break
                            if self.check(i, n - 1):
                                if not board[i][n - 1] and self.check(i, n - 1):
                                    board[i][n - 1] = token
                                    motion = True
                                    break

            # Ищем свободные места
            for i in range(0, height - 1):
                while not motion:
                    for n in range(0, width - 1):
                        # Проверяем центр
                        if board[1][1] == 0:
                            board[1][1] = token
                            motion = True
                            break
                        else:
                            # Проверяем углы
                            if board[i][0] == 0:
                                board[i][0] = token
                                motion = True
                                break
                            elif board[i][width - 1] == 0:
                                board[i][width - 1] = token
                                motion = True
                                break
                            elif board[height - 1][0] == 0:
                                board[height - 1][0] = token
                                motion = True
                                break
                            elif board[height - 1][width - 1] == 0:
                                board[height - 1][width - 1] = token
                                motion = True
                                break
                            else:
                                # Проверяем свободные места
                                board[i][n] = token
                                motion = True
                                break
        return board

    # Делаем ход
    def take_input(self, player_token: str, board: [], width: int, height: int) -> []:
        board = self.choice(board, player_token, width, height)
        return board

    # Проверяем на победу
    def check_win(self, board, width, height, quantity):
        if self.enumeration(board, width, height, quantity, "X"):
            return "X"
        elif self.enumeration(board, width, height, quantity, "0"):
            return "0"
        return False

    @property
    def play(self):
        # Основная функция игры
        request = []
        PlayerX = 'X'
        Player0 = '0'

        if self.firstPlayer() == 1:
            playerFirst = "X"
            playerSecond = '0'
        else:
            playerSecond = "X"
            playerFirst = '0'
        counter = 0
        board = self.create_board(self.width, self.height)
        win = False
        while not win:
            if counter % 2 == 0:
                board = self.take_input(PlayerX, board, self.width, self.height)
            else:
                board = self.take_input(Player0, board, self.width, self.height)
            counter += 1
            if counter > self.quantity * 2 - 1:
                result = self.check_win(board, self.width, self.height, self.quantity)
                if result == "X":
                    if playerFirst == "X":
                        request = {"Выиграл игрок 1"}
                        win = True
                    else:
                        request = {"Выиграл игрок 2"}
                        win = True
                elif result == '0':
                    if playerFirst == "0":
                        request = {"Выиграл игрок 1"}
                        win = True
                    else:
                        request = {"Выиграл игрок 2"}
                        win = True
            if counter == self.width * self.height:
                request = 'Ничья'
                win = True
        return self.draw_board(board), request
