# Описание проекта: программа генерирует случайное число в диапазоне от 11 до 100100 и просит пользователя угадать
# это число. Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много,
# попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало,
# попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы
# угадали, поздравляем!'.

from random import *


def is_valid(guess, right_border):
    return guess.isdigit() == True and 1 <= int(guess) <= right_border


def input_guess(right_border):
    while True:
        guess = input(f'Введите целое число от 1 до {right_border}: ')
        if is_valid(guess, right_border):
            return int(guess)
        else:
            print(f'А может быть всё-таки введем целое число от 1 до {right_border}?')


def comparison(quiz, right_border):
    counter = 1
    while True:
        guess = input_guess(right_border)
        if guess < quiz:
            print('Ваше число меньше загаданного, попробуйте еще разок!\n')
            counter += 1
        elif guess > quiz:
            print('Ваше число больше загаданного, попробуйте еще разок!\n')
            counter += 1
        else:
            print('Вы угадали, поздравляем!\n')
            print(f'Сделано попыток: {counter}\n')
            break


def exit_menu():
    while True:
        choice = input('Хотите продолжить? 1 - продолжить, 0 - выйти:  ')
        if choice != '1' and choice != '0':
            print('Ошибка ввода.\n')
        else:
            break
    if choice == '1':
        print()
        new_game()
    else:
        print('\nСпасибо, что играли в числовую угадайку. Ещё увидимся...')


def new_game():
    right_border = int(input('В каком диапазоне будем угадывать числа? Задайте интервал от 1 до N; N = '))
    print()
    quiz = randint(1, right_border)
    comparison(quiz, right_border)
    exit_menu()


print('Добро пожаловать в числовую угадайку!')
new_game()
