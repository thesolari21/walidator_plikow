import os
import re

# sprawdza pliki oraz foldery z tej samej lokalizacji co jest odpalany skrypt
# zwraca liste niedopasowana do wzorca
def check():
    list = []

    print('Skrypt odpalany z lokalizacji: ', os.getcwd())
    print('Sprawdzam pliki dla lokalizacji: ', os.getcwd(), end='\n\n')

    for file in os.listdir(os.getcwd()):

        # walidacja za pomoca wyrazenia regularnego. Edytuj tutaj aby zmienic wzorzec.
        valid_file = re.fullmatch("[a-zA-Z0-9._-]+", file)
        if valid_file is None:
            list.append(file)

    print('Niezgodnych elementów:', len(list))
    print('\n{:20s} {:10s}'.format('Nazwa', 'Typ'))
    print('-------------------------')

    # sprawdzenie czy plik/katalog. Dalej wyswietl w tabelce
    for file in list:
        if os.path.isfile(os.getcwd() + '/' + file):
            type = 'plik'
        else:
            type = 'katalog'
        print('{:20s} {:10s}'.format(file, type))

    answer = input('\nCzy naprawic pliki? [tak - jesli jestes pewien]: ')
    answer = answer.lower().strip()

    return list, answer

def repair(to_rapair):
    print("tu beda naprawiane pliki")
    print(to_rapair)

##################### główny program ########################

to_rapair, answer = check()

if answer == 'tak':

    # na wszelki wypadek - gdyby nazwa samego skryptu naprawiajacego byla niepoprawna
    # wtedy wyklucz z listy
    if os.path.basename(__file__) in to_rapair:
        to_rapair.remove(os.path.basename(__file__))

    repair(to_rapair)
else:
    print('Dziękuję. Do zobaczenia.')




