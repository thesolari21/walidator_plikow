import os
import re

list = []
localization = 'C:/Users/barts/Desktop/python/v2/walidator_plikow/test'
# C:/Users/barts/Desktop/python/v2/walidator_plikow/test
# ./test

print('Skrypt odpalany z lokalizacji: ', os.getcwd())
print('Sprawdzam pliki dla lokalizacji: ', localization, end = '\n\n')

for file in os.listdir(localization):
    valid_file = re.fullmatch("[a-zA-Z0-9._]+",file)
    if valid_file is None:
        list.append(file)

print('Niezgodnych elementów:', len(list))
print('\n{:20s} {:10s}'.format('Nazwa' , 'Typ'))
print('-------------------------')

for file in list:
    if os.path.isfile(localization + '/' + file):
        type = 'plik'
    else:
        type = 'katalog'
    print('{:20s} {:10s}'.format(file , type) )
