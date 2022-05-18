import os
import re

# sprawdza pliki oraz foldery z tej samej lokalizacji co jest odpalany skrypt
# zwraca liste plików niedopasowana do wzorca
def check(REGEX):
    list = []

    print('Skrypt odpalany z lokalizacji: ', os.getcwd())
    print('Sprawdzam pliki dla lokalizacji: ', os.getcwd(), end='\n\n')

    for file in os.listdir(os.getcwd()):

        valid_file = re.fullmatch(REGEX, file)
        if valid_file is None:
            list.append(file)

    return list

# zwraca listę z poprawnymi nazwami plików
def translate(to_rapair, DICT_TRANSLATE, REGEX):
    translated = []

    for file in to_rapair:
        result = ''
        for char in file:
            # jesli litera jest w słowniku - podmien ją
            if char in DICT_TRANSLATE:
                result += DICT_TRANSLATE[char]

            # jesli znaku nie ma w słowniku, a nie jest zgodny z regex - usun go
            elif re.fullmatch(REGEX, char) is None:
                result += ''
            else:
                result += char
        translated.append(result)

    print('Niezgodnych elementów:', len(to_rapair))
    print('\n{:30s} {:30s} {:30s}'.format('Nazwa', 'Nowa nazwa', 'Typ'))
    print('------------------------------------------------------------')

    # sprawdz czy plik/katalog. Dalej wyswietl w tabelce
    for file, trans in zip(to_rapair, translated):
        if os.path.isfile(os.getcwd() + '/' + file):
            type = 'plik'
        else:
            type = 'katalog'
        print('{:30s} {:30s} {:30s}'.format(file, trans, type))

    return translated

# zmienia nazwy plikow korzystajac z list to_repair, translated
def repair(to_repair, translated):

    for file, trans in zip(to_repair, translated):
        os.rename(file,trans)
    print('Zrobione!')

##################### główny program ########################

# wyrażenie regularne na podstawie którego są sprawdzane pliki
REGEX = '[a-zA-Z0-9._-]+'

# słownik translacji
DICT_TRANSLATE = {'ą' : 'a', 'Ą' : 'A',
             'ę' : 'e', 'Ę' : 'E',
             'ć' : 'c', 'Ć' : 'C',
             'ó' : 'o', 'Ó' : 'O',
             'ł' : 'l', 'Ł' : 'L',
             'ń' : 'n', 'Ń' : 'N',
             'ż' : 'z', 'Ż' : 'Z',
             'ź' : 'z', 'Ź' : 'Z',
             'ś' : 's', 'Ś' : 'S',' ' : '_' }

# 1. sprawdź pliki
to_rapair = check(REGEX)

# na wszelki wypadek - gdyby nazwa samego skryptu naprawiajacego byla niepoprawna
# wtedy wyklucz z listy
if os.path.basename(__file__) in to_rapair:
    to_rapair.remove(os.path.basename(__file__))

# 2. utwórz nowe, poprawne nazwy
translated = translate(to_rapair, DICT_TRANSLATE, REGEX)

answer = input('\nCzy naprawic pliki? [tak - jesli jestes pewien]: ')
answer = answer.lower().strip()
if answer == 'tak':

    # 3. napraw pliki
    repair(to_rapair,translated)
else:
    print('Dziękuję. Do zobaczenia.')
