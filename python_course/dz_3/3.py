"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Пример:


k = 'ноутбук'
# 12

"""
dic = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1, 
'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 
'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10, 'а': 1, 'в': 1, 'е': 1, 'и': 1, 'о': 1, 'р': 1, 'с': 1,
 'т': 1, 'н': 1, 'л': 2, 'м': 2, 'д': 2, 'к': 2, 'п': 2, 'у': 2, 'ь': 3, 'г': 3, 'я': 3,
'б': 3, 'й': 4, 'ы': 4, 'ц': 5, 'х': 5, 'з': 5,'ж': 5,'ч': 5,'ю': 8, 'ш': 8, 'э': 8, 'ф': 10,
'щ': 10, 'ъ': 10 }
print('vvedite slovo')
k = input()
a = k.lower()

count = 0
for i in range(0, len(a)):
    for (j, v) in dic.items():
        if a[i] == j:
    
            count = count + v

print(count)


        
"""
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)
"""