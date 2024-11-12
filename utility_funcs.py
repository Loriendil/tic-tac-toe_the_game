def count_nulls(scroll):
    # Дана матрица N x N.
    # Посчитать все нули.
    # Возвратить кортеж с парами чисел, строка и столбец, в которых находятся нули матрицы.
    result = []
    for row in range(len(scroll)):
        for col in range(len(scroll[row])):
            if scroll[row][col] == 0:
                result.append((row, col))
    return result

def get_matrix_element(matrix, element, element_num):
    # Дана матрица N x N.
    # Дана переменная element, которая есть разновидность части матрицы (строка, столбец и т.д.).
    # Дана переменная element_num, которая есть порядковый номер части матрицы.
    result = []

    # Убеждаюсь в принадлежности element_num к допустимому диапазону.
    if element_num < 0 or element_num > len(matrix):
        print('Error: element_num is out of range. Function get_matrix_element()')
        return result

    match element:
        case 1:  # Столбец
            result = [row[element_num - 1] for row in matrix]
        case 2:  # Строка
            result = matrix[element_num - 1]
        case 3:  # Главная диагональ
            result = [matrix[i][i] for i in range(len(matrix))]
        case 4:  # Второстепенная диагональ
            result = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
        case _:  # Не верный вариант. Нужен в целом обработчик ошибок... по идеи ....
            print('Error: Invalid element type. Function get_matrix_element()')
    return result

def check_victory(matrix, e_type, e_num):
    # Вызову функцию и сохраню результат
    result = get_matrix_element(matrix, e_type, e_num)
    # Проверяем если функция возвращает либо 3, либо -3, то
    # по всему элементу матрицы одинаковые числа.
    if sum(result) == 3:
        return 1 # возвращаем в качестве победителя игрока за Х
    if sum(result) == -3 and all(result): # строка all(result) для памяти,
                                          # делает тоже что и sum(result)
                                          # но по другому: all() возвращает истину если все элементы истинны.
                                          # Такое логическое И только для списка.
        return -1 # возвращаем в качестве победителя игрока за О
    return 0

def create_board(board_size = 3):
    # создаём игровое поле N на N
    board = []
    # заполняем поле нулями, которые будут означать, что поле пустое.
    for i_tem in range(board_size):
        board_row = list()
        for j_tem in range(board_size):
            board_row.append(0)
        board.append(board_row)
    return board

def player_acts(board_field, place, player_id):
    # matrix - матрица представляющая игровое поле
    # place - кортеж с координатами места куда хочет сходить пользователь
    board_field[place[0]][place[1]] = player_id
    return board_field

def player_choose_place(board_size):
    while True:
        print(
            f'Введите номер столбца, а затем номер строки начиная с 1 до {board_size} через запятую.[введите целое натуральное число]')
        coordinates_string = input()
        separator = ','
        if separator in coordinates_string:
            coord_list = coordinates_string.split(separator)
            if coord_list[0].isnumeric() and coord_list[1].isnumeric():
                if (int(coord_list[0]) != 0) and (int(coord_list[1]) != 0):
                    return int(coord_list[0]) - 1, int(coord_list[1]) - 1
                else:
                    continue
            else:
                continue
        else:
            continue