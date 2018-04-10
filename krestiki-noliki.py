#Игра крестики-нолики

# глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    #Выыодит на экран инструкцию
    print("""Добро пожаловать в игру Крустики-нолики.
    Чтобы сделать ход, введите число от 0 до 8.
    Числа соответстыкют полям как показано ниже:
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
    """)

def ask_yes_no(question):
    #Задает вопрос
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    # Просит ввести число из диапозона
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    #Определяет кто ходит первым
    go_first = ask_yes_no("Будешь ходить первым? (y/n): ")
    if go_first == "y":
        print("\nХорошо, Ходи первым.")
        human = X
        computer = O
    else:
        print("\nНу что же, перавым буду ходить я")
        computer = X
        human = O
    return computer, human

def new_board():
    #Создает новую доску
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    # Отображает игровую доску на экране
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    # Создает список доступных ходов
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    #Определяет победителя в игре
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    #Ход человека
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход, выьери одну клетку (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭта клетка уже занята. Выбери другую.\n")
    print("Отлично...")
    return move


def computer_move(board, computer, human):
    # Ход компьютера
    # Создадим копию доски, потомц что функция будет менять значения
    board = board[:]
    # Лучшие позиции
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")

    # если компьютер победит, то делать ход
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # выполнив проверку, отмечаем изменения
        board[move] = EMPTY

    # если человек победит, то делать ход
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # выполнив проверку, отмечаем изменения
        board[move] = EMPTY

    # так как никто не побеждает, то делаем лучший ход
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Переход хода"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "победил!\n")
    else:
        print("Ничья!\n")

    if the_winner == computer:
        print("Ну что же, победа моя. Иди тренеруйся")

    elif the_winner == human:
        print("Поздравляю, ты победил!")

    elif the_winner == TIE:
        print("Ничья, так ничья.")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# start the program
main()
input("\n\nEnter для выхода")