# ОПИСАНИЕ ПРОЕКТА
#
# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря,
# при этом сдвиг шифрования для каждого слова разный и равен длине этого слова.
# Строчные буквы при этом остаются строчными, а прописные – прописными.
# Символы, не являющиеся английскими буквами, не изменяются.

# Например:
# Sample Input 1:
# Day, mice. "Year" is a mistake!

# Sample Output 1:
# Gdb, qmgi. "Ciev" ku b tpzahrl!

# Sample Input 2:
# my name is Python!

# Sample Output 2:
# oa reqi ku Veznut!

alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_full = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
card = 26


def word_length(word):
    length = 0

    for sym in word:
        if sym in alphabet_full:
            length += 1

    return length


def caesar(word, shift):
    new_word = ''

    for i in word:
        if not i.isalpha():
            new_i = i

        else:
            if i.isupper():
                index = alphabet_upper.find(i)
                new_index = (index + shift) % card
                new_i = alphabet_upper[new_index]
            else:
                index = alphabet_lower.find(i)
                new_index = (index + shift) % card
                new_i = alphabet_lower[new_index]

        new_word += new_i

    return new_word


# MAIN:

text = input()

word_list = text.split()
new_word_list = []

for word in word_list:
    shift = word_length(word)
    new_word = caesar(word, shift)
    new_word_list.append(new_word)

new_text = ' '.join(new_word_list)
print(new_text)
