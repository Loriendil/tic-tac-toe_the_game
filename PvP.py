import utility_funcs as uf

def play_with_computer():

    while True:
        print('Вы выбрали бросить вызов компьютеру!')
        print('Какой желаете размер поля для игры? [введите целое натуральное число]')
        board_size = input()
        if board_size.strip().isdigit():  # убираем пробелы до и после ввода
            board_size = int(board_size)
            if board_size >= 0:
                board_size = board_size
                print(board_size)
                print(type(board_size))
                break
        else:
            continue
    board = uf.create_board(board_size)

    # представим бесконечный цикл, где по очереди ходят игроки
    moves = 0
    player = 1
    while True:
        if player == 1:
            print('Player 1 acts!')
            player_x_input = uf.player_choose_place(board_size)
            board[player_x_input[0]][player_x_input[1]] = 1
            moves += 1
            player = -1

        if player == -1:
            print('Computer acts!')
            import random
            board_map = uf.count_nulls(board)
            index = random.randrange(start = 0, stop = len(board_map))
            player_o_input = board_map.pop(index)
            board[player_o_input[0]][player_o_input[1]] = -1
            moves += 1
            player = 1

        if moves > 4:
            for elem in range(0, len(board)):
                for e_type in range(1, 4):
                    vic = uf.check_victory(board, e_type, elem)
                    if vic == 1:
                        print('Winner is X-player!')
                        break
                    elif vic == -1:
                        print('Winner is O-player!')
                        break