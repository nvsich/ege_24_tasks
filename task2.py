# Заполним массив arr строками из файла
with open('24.txt') as file:
    arr = [line for line in file]

alph = 'VINODEL'
answer = 0

# Переберем каждую строку из массива
for i in range(len(arr)):
    
    # Число комбинаций в текущей строке
    currCount = 0

    # Перебираем символы из набора alph
    for j in alph:
        # .count('DG' + j + 'U') - подсчет количества
        # найденных комбинаций в строке
        if arr[i].count('DG' + j + 'U') > 0:
            currCount += 1

    # Если подходящие комбинации в строке есть (currCount > 0) и
    # номер строки не кратен 2,
    # то answer присваиваем i + 1, т.к. нумерация в Python
    # начинается с 0. Т.к. мы перебираем i по возрастанию,
    # answer будет наибольшим
    if currCount > 0:
        if (i + 1) % 2 != 0:
            answer = i + 1

print(answer)
