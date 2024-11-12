# Игра крестики-нолики
# правила взяты из статьи на Хабре.
"""
1. Пустая доска n x n клеток.
2. Два игрока ходят по очереди, ставя свою фигуру в пустую ячейку
3. Любой горизонтальный, вертикальный или диагональный ряд,
заполненный фигурой игрока, приносит ему выигрыш и заканчивает игру
4. Когда больше нет свободных полей - игра тоже заканчивается, ничьей.
5. Для простоты отображения выберем заглавные X и O в качестве фигур игроков
и пробел для пустой ячейки
6. Пусть игрок за Х ходит первым.
"""
import PvP
import PvE
import utility_funcs as uf

def greetings(phrase):
    print(phrase)
    ans = input()
    if ans.upper() == 'Q':
        return -3
    else:
        if ans.upper() == 'F':
            PvE.play_with_friend()
            return 3
        elif ans.upper() == 'C':
            PvP.play_with_computer()
            return 3
        else:
            return -3

print('Hello! It is a tic-tac-toe game')
print('Rules are:')
print('1. An empty board of n x n cells.')
print('2. Two players take turns placing their piece in an empty cell')
print("3. Any horizontal, vertical or diagonal row filled with a player's piece brings him a win and ends the game")
print('4. When there are no more empty cells, the game also ends, in a draw.')
print("5. For simplicity of display, we choose capital X and O as the player's pieces")
print('and a space for an empty cell')
print('6. Let the player for X go first.')

count = 0
first_time = 'Do you want to play with your friend [F] or your computer [C]? (for exit press "Q")'
second_time = 'Do you want to play again with your friend [F] or your computer [C]? (for exit press "Q")'
while count >= 0:
    if count == 0:
        count = greetings(first_time)
    if count > 0:
        count = greetings(second_time)
print('Have a nice day, sir!')
