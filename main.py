# квадрат
# for i in range(10):
#     if i == 0 or i == 9:
#         for j in range(20):
#             print('*', end='')
#     else:
#         print('*', end='')
#         for j in range(1, 19):
#             print(' ', end='')
#         print('*', end='')
#     print()

# menu
lis = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 8, 9, 6, 7]

while True:
    a = '1.найти min число в листе'
    b = '2.удалить все одинаковые значения'
    c = '3.заменить каждое четвертое значение на "Х"'
    d = '4.вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа'
    e = '6.выход'
    menu = [a, b, c, d, e]
    x = print(a, b, c, d, e, sep='\n')
    inp = input('Сделайте свой выбор:')
    for i in inp:
        if inp == '1':
            print(lis, min(lis), sep='\n')
        elif inp == '2':
            print(lis, list(set(lis)))
        elif inp == '3':
            for i in range(3, len(lis), 4):
                lis[i] = 'X'
            print(lis)
        elif inp == '6':
            break

# таблица умножения
# for i in r nge(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='\t')
#     print()
#
# n = int(input('Enter number: '))
# i = 1
# j = 1
# while i <= n:
#     while j <= n:
#         print(i * j, end='\t')
#         j += 1
#     i += 1
#     j = 1
#     print()
