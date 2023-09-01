# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом
# Цезаря. Она должна запрашивать у пользователя следующие данные: направление: шифрование или дешифрование; язык
# алфавита: русский или английский; шаг сдвига (со сдвигом вправо). Примечание 1. Считайте, что в русском языке 32
# буквы (буква ё отсутствует). Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
# Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию
# вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

const_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
card_ru = 32

const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const_lower_en = 'abcdefghijklmnopqrstuvwxyz'
card_en = 26


def input_menu():
    while True:
        choice = input('Выберите направление работы программы: 1 - шифровать, 2 - дешифровать: ')
        if choice not in ['1', '2']:
            print('Ошибка ввода')
        else:
            break

    if choice == '1':
        mode = 1
    else:
        mode = -1

    while True:
        choice = input('Выберите язык алфавита: 1 - русский, 2 - английский: ')
        if choice not in ['1', '2']:
            print('Ошибка ввода')
        else:
            break

    if choice == '1':
        alphabet_upper = const_upper_ru
        alphabet_lower = const_lower_ru
        card = card_ru
    else:
        alphabet_upper = const_upper_en
        alphabet_lower = const_lower_en
        card = card_en

    while True:
        choice = input('Введите положительный шаг сдвига: ')
        if not choice.isdigit() or int(choice) <= 0:
            print('Ошибка ввода')
        else:
            break

    shift = int(choice)

    text = input('Введите текст для обработки: ')

    return text, alphabet_upper, alphabet_lower, card, shift, mode


def caesar(text, alphabet_upper, alphabet_lower, card, shift, mode):
    text_new = ''

    for i in text:
        if not i.isalpha():
            i_new = i

        else:
            if i.isupper():
                index = alphabet_upper.find(i)
                new_index = (index + mode * shift) % card
                i_new = alphabet_upper[new_index]
            else:
                index = alphabet_lower.find(i)
                new_index = (index + mode * shift) % card
                i_new = alphabet_lower[new_index]

        text_new += i_new

    return text_new


text, alphabet_upper, alphabet_lower, card, shift, mode = input_menu()
print()
print(caesar(text, alphabet_upper, alphabet_lower, card, shift, mode))
