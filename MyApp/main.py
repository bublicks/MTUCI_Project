sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]# это список
sides = sorted(sides, reverse=True)# мы его сортируем от большего к меньшему
smax = 0# наибольшее значение запишем в переменную
# print(len(sides)) 12
for i in range(len(sides)):# перебираем элементы массива
    for j in range(i + 1, len(sides)):#
        for k in range(j + 1, len(sides)):#
            a = sides[i]#
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if s > smax:
                    smax = s
print("Максимальная площадь треугольника", smax)