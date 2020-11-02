#Создаем матрицу 1
n = 3
m = 4
a = [[1] * m for i in range(n)]
print(a)

#Создаем матрицу 2
n = 3
m = 4
b = [[2] * m for i in range(n)]
print(b)

#Создаем нулевую матрицу
n = 3
m = 4
c = [[0] * m for i in range(n)]

#Обработка и вывод списка
for i in range(len(a)): #Цикл для перебора номера строки

    for j in range(len(a[0])): #Цикл для перебора элементов в строке
        c[i][j] = a[i][j] + b[i][j] #Складываем матрицы

for d in c:  #Сортировка элементов
 print(d)