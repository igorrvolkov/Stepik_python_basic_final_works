# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.

from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def int_answer(question):
    while True:
        answer = input(question)
        if not answer.isdigit() or answer == '0':
            print('Ошибка ввода.')
        else:
            return int(answer)


def bool_answer(question):
    while True:
        answer = input(question)
        if answer == '1':
            return True
        elif answer == '0':
            return False
        else:
            print('Ошибка ввода. Выберите 1 или 0.')


def define_content():
    chars = ''
    while True:
        type_counter = 0
        password_draft = ''

        question = 'Включать ли цифры? 1 - да, 0 - нет: '
        if bool_answer(question):
            type_counter += 1
            password_draft += choice(digits)
            chars += digits
        question = 'Включать ли прописные буквы? 1 - да, 0 - нет: '
        if bool_answer(question):
            type_counter += 1
            password_draft += choice(uppercase_letters)
            chars += uppercase_letters
        question = 'Включать ли строчные буквы? 1 - да, 0 - нет: '
        if bool_answer(question):
            type_counter += 1
            password_draft += choice(lowercase_letters)
            chars += lowercase_letters
        question = 'Включать ли символы? 1 - да, 0 - нет: '
        if bool_answer(question):
            type_counter += 1
            password_draft += choice(punctuation)
            chars += punctuation

        if type_counter == 0:
            print('Все ответы не могут быть отрицательными. Пожалуйста, введите данные ещё раз.')
        else:
            return password_draft, chars, type_counter
            break


def generate_password(password_draft, length, type_counter, chars):
    if length == type_counter:
        password = list(password_draft)
        shuffle(password)
        password = ''.join(password)
        return password

    elif length < type_counter:
        password = list(password_draft)
        shuffle(password)
        password = ''.join(password)
        password = password[:length]
        return password

    else:
        password = list(password_draft)
        shuffle(password)
        password = ''.join(password)

        for _ in range(length - type_counter):
            password += choice(chars)

        return password


def replace_similars(password, digits, lowercase_letters, uppercase_letters):
    counter_1 = 0
    counter_0 = 0

    for i in password:
        if i in 'il1L':
            counter_1 += 1
            if counter_1 > 1:
                if i == 'i' or i == 'l':
                    lowercase_letters = lowercase_letters.replace('i', '')
                    lowercase_letters = lowercase_letters.replace('l', '')
                    password = password.replace(i, choice(lowercase_letters))
                if i == '1':
                    digits = digits.replace('1', '')
                    password = password.replace(i, choice(digits))
                if i == 'L':
                    uppercase_letters = uppercase_letters.replace('L', '')
                    password = password.replace(i, choice(uppercase_letters))

        if i in 'oO0':
            counter_0 += 1
            if counter_0 > 1:
                if i == 'o':
                    lowercase_letters = lowercase_letters.replace('o', '')
                    password = password.replace(i, choice(lowercase_letters))
                if i == '0':
                    digits = digits.replace('0', '')
                    password = password.replace(i, choice(digits))
                if i == 'O':
                    uppercase_letters = uppercase_letters.replace('O', '')
                    password = password.replace(i, choice(uppercase_letters))

    return password


# MAIN BLOCK

question = 'Cколько паролей нужно сгенерировать? '
count = int_answer(question)

question = 'Введите длину одного пароля: '
length = int_answer(question)

password_draft, chars, type_counter = define_content()

question = 'Исключать ли неоднозначные символы il1Lo0O? 1 - да, 0 - нет: '
is_replace_similars = bool_answer(question)

if count == 1:
    print('\nВаш пароль: ')
else:
    print('\nВаши пароли: ')

if not is_replace_similars:
    for _ in range(count):
        print(generate_password(password_draft, length, type_counter, chars))

else:
    for _ in range(count):
        password = generate_password(password_draft, length, type_counter, chars)
        print(replace_similars(password, digits, lowercase_letters, uppercase_letters))
