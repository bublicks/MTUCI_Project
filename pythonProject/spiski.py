names=['cat','dog','cow','horse']
print(names)
#индексы с нуля и до предпоследнего
print(names[0])
print(names[-1])

names.append('goat')
for i in names:# название переменной не имеет смысла
    print(i)

print(len(names))

names.pop()#удаление последнего
print(names)

i = names.index('dog')
print(i)
