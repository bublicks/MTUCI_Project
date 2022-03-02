'''import os
# Возвращает путь к текущей рабочей папке
pth=os.getcwd()
print(pth)'''
import os
import fnmatch
# В цикле, с помощью os.listdir('.') получим список файлов
# в текущей директории (точка в скобках как раз ее и обозначает)
for fname in os.listdir('.'):
    # Если у текущего имени файла расширение .py, то печатаем его
    if fnmatch.fnmatch(fname, 'oc.py'):
        print(fname)