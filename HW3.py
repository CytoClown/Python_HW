
# 1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
print(f'{my_list[2][0]}, {my_list[2][1]}, {my_list[2][2]}')

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'


list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
n = len(list_1)
sm = 0
char = 'a'
for i in range(n):
    if type(list_1[i]) == int:
        sm += list_1[i]
    else:
        t = str(list_1[i])
        if char in t:
            print(t)
print(sm)

lst2 = [x for x in list_1 if isinstance(x, int)]
print(sum(lst2))


# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
list3 = ['cat', 'dog', 'horse', 'cow']
print(tuple(list3))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом.
# Если состав одинаковый, print("Equal')

family1 = input()
family2 = input()
t = family1.split()
t1 = family2.split()
string = ''
if len(t) > len(t1):
    print(', '.join(t))
elif len(t1) > len(t):
    print(', '.join(t1))
else:
    print('Equal')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

film = {
    'title': 'Round bread',
    'director': 'Pavlova',
    'year': 1930,
    'budget': 'IT',
    'main_actor': 'Kolobok',
    'slogan': 'В лесу родилась елочка'
    }
print(film.keys())
print(film.items())
print(film.values())

# 3.6. Найдите сумму всех значений в словаре my_dictionary = \
#     {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
dict = {'num1': 375,
        'num2': 567,
        'num3': -37,
        'num4': 21
        }
s = 0
for i in dict:
    s += dict.get(i)
print(s)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
a = set([1, 2, 3, 4, 5, 3, 2, 1])
print(a)


# 3.8. Даны два множества: set1 = ({'a', 'z', 1, 5, 9, 12, 100, 'b'},
#                                  set2) = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
if set1 in set2:
    print('Set1 - подмножество Set2')
elif set2 in set1:
    print('Set2 - подмножество Set1')
else:
    print('Set1 и Set2 не являются подмножествами')
set3 = list(set1)
set4 = list(set2)
eq = ''
noeq = ''
for i in range(len(set3)):
    if set3[i] in set4:
        eq += ' ' + str(set3[i])
    elif set3[i] not in set4:
        noeq += ' ' + str(set3[i])

print('Совпадающие значения: ', eq)
print('Уникальные значения: ', noeq)



