"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:


var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:


3 5
"""
var1 = '5 5' # количество элементов первого и второго множества
var2 = '10 20 30 40 50' # элементы первого множества через пробел
var3 = '10 20 30 40 50' # элементы второго множества через пробел

var4 = var2.split()
var5 = var3.split()
var6 = [int(item) for item in var4]
var7 = [int(item) for item in var5]
var8 = set(var6)
var9 = set(var7)

lst = list()
for el in var8:
    for elem in var9:
        if el == elem:
            lst.append(elem)

lst.sort()
print(*lst)



"""
mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')

"""
