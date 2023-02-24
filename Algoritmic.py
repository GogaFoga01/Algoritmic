# И
x = 5
y = 6
z = x & y
print('x = ', x)
print('y = ', y)
print('z = ', z)

# Или
x = 5
y = 6
z = x ^ y
print('x = ', x)
print('y = ', y)
print('z = ', z)

# Чет и Нечет
a = 34560

even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print("Even: %d, odd: %d" % (even, odd))

# Рандом
l = []

for i in range(5):
    l.append(int(input()))

maximum = max(l)
minimum = min(l)

for i in range(len(l)):
    if l[i] == maximum:
        l[i] = minimum
    elif l[i] == minimum:
        l[i] = maximum

print(l)

# Пузырек

import random
import statistics

li = []
for i in range(44):
    li.append(random.randint(-100, 100))
print(li)


def buble(list):
    n = 1
    while n < len(li):
        for i in range(len(li) - n):
            if li[i] < li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1


buble(li)
print(li)

# Слияние

li = []

for i in range(44):
    li.append(random.randint(0, 50))
print(li)


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

mergeSort(li)
print(li)

# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


my_string = input('Введите строку для сжатия: ')
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(my_string, codes)
print('Сжатая строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)

if my_string == decoding_str:
    print('Успешно!')
else:
    print('Ошибка!')