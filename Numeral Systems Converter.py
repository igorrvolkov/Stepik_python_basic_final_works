# ОПИСАНИЕ ПРОЕКТА
#
# Простенький калькулятор систем счисления, который позволяет переводить числа из десятичной с.с. в с.с. с выбранным
# основанием и наоборот. Работает с натуральными целыми числами Основание системы счисления (как исходной,
# так и выходной) не может быть больше 16.


# Функция конвертации в десятичную систему счисления
def to_dec(number, base):
    positions = len(number)
    pos = positions - 1
    new_number = 0

    if base <= 10:

        for i in number:
            new_number += int(i) * base ** pos
            pos -= 1

    else:
        for i in number:
            if i == 'A':
                i = 10
            elif i == 'B':
                i = 11
            elif i == 'C':
                i = 12
            elif i == 'D':
                i = 13
            elif i == 'E':
                i = 14
            elif i == 'F':
                i = 15
            else:
                i = int(i)

            new_number += i * base ** pos
            pos -= 1

    return new_number

# Функция конвертации из десятичной системы счисления
def from_dec(number, base):
    number = int(number)
    new_num = ''

    if base <= 10:
        while number // base != 0:
            mod = number % base
            new_num += str(mod)
            number //= base

    else:
        while number // base != 0:
            mod = number % base
            if mod == 10:
                mod = 'A'
            elif mod == 11:
                mod = 'B'
            elif mod == 12:
                mod = 'C'
            elif mod == 13:
                mod = 'D'
            elif mod == 14:
                mod = 'E'
            elif mod == 15:
                mod = 'F'
            else:
                mod = str(mod)
            new_num += mod
            number //= base

    new_num += str(number)
    new_num = new_num[::-1]
    return new_num

def main_menu():
    print('Добро пожаловать в калькулятор систем счисления. '
          '\nЭтот калькулятор может работать с натуральными целыми числами и системами счисления с основанием не больше 16.')

    # Выбор направления работы программы
    print()
    while True:
        mode = input('Введите режим: '
                     '\n0 - конвертировать из десятичной системы счисления, 1 - конвертировать в десятичную систему счисления: ')
        if mode not in ['0', '1']:
            print('Ошибка ввода')
        else:
            break

    # Выбор основания системы счисления
    print()
    if mode == '0':
        request_base = 'Введите основание системы счисления, в которую требуется конвертация: '
    else:
        request_base = 'Введите основание исходной системы счисления, в которой представлено число: '
    while True:
        base = input(request_base)
        if not base.isdigit():
            print('Ошибка ввода')
        elif int(base) == 0:
            print('Основанием системы счисления не может быть 0')
        elif 10 < int(base) <= 16 and mode == '0':
            print('Для представления чисел в системах счисления с основанием от 11 до 16 будут использованы буквенные обозначения:'
                  '\n10 = A, 11 = B, 11 = C, 13 = D, 14 = E, 15 = F')
            break
        elif int(base) > 16:
            print('Эта программа пока не может работать с системами счисления с основанием больше 16')
            break
        else:
            break
    base = int(base)

    # Определение словаря используемых цифр для последующей проверки корректности введенного числа
    digits = ''
    if mode == '0':
        digits = '0123456789'
    else:
        if 0 < int(base) <= 10:
            for i in range(base):
                digits += str(i)
        else:
            if base == 11:
                digits = '0123456789Aa'
            if base == 12:
                digits = '0123456789AaBb'
            if base == 13:
                digits = '0123456789AaBbCc'
            if base == 14:
                digits = '0123456789AaBbCcDd'
            if base == 15:
                digits = '0123456789AaBbCcDdEe'
            if base == 16:
                digits = '0123456789AaBbCcDdEeFf'

    # Ввод числа для конвертации
    print()
    if mode == '0':
        request_number = 'Введите число в десятичной системе счисления: '
    else:
        request_number = f'Введите число, записанное в системе счисления с основанием {base}: '
    while True:
        number = input(request_number)
        flag = True

        for i in number:
            if i not in digits:
                print('Ошибка ввода')
                flag = False
                break

        if flag:
            break

    return int(mode), base, number

# MAIN

mode, base, number = main_menu()

if mode == 0:
    new_number = from_dec(number, base)
else:
    new_number = to_dec(number, base)

print()
print('Результат:', new_number)

