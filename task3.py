# Заполним массив arr строками из файла
with open('24_3.txt') as file:
    arr = [line for line in file]

# maxLen минимальное, т.к. мы ищем макс. длину
# prevString максимальное, т.к. при вычитании индексов,
# мы ищем макс. длину
maxLen = float('-inf')
prevString = float('inf')

# Перебираем каждую строку массива
for i in range(len(arr)):

    # Если в строке есть EGE и нет VUZ,
    # то строчка подходит. Искомое расстояние -
    # разница между текущим индексом строки и предыдущим
    if (arr[i].count('EGE') > 0 and
        arr[i].count('VUZ') == 0):
        maxLen = max(maxLen, i - prevString)
        prevString = i
        
print(maxLen)
