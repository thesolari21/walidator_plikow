import os
import re


def check(REGEX):
    """
    Check files and folders from the same location as the script is run.
    Return a list of file not matching with pattern.
    :param REGEX: str
    :return: list
    """

    wrong_names = []

    print('Skrypt odpalany z lokalizacji: ', os.getcwd())
    print('Sprawdzam pliki dla lokalizacji: ', os.getcwd(), end='\n\n')

    for check_file in os.listdir(os.getcwd()):
        valid_file = re.fullmatch(REGEX, check_file)
        if valid_file is None:
            wrong_names.append(check_file)

    return wrong_names


def translate(to_rapair, DICT_TRANSLATE, REGEX):
    """
    Return a list of numbers with calid names
    :param to_rapair: list[str]
    :param DICT_TRANSLATE: dict[str,str]
    :param REGEX: str
    :return: list[str]
    """
    translated = []

    for file in to_rapair:
        result = ''
        for char in file:
            if char in DICT_TRANSLATE:
                result += DICT_TRANSLATE[char]
            elif re.fullmatch(REGEX, char) is None:         # jesli znaku nie ma w słowniku, a nie jest zgodny z regex
                result += ''                                # usun go
            else:
                result += char
        translated.append(result)

    print('Niezgodnych elementów:', len(to_rapair))
    print('\n{:30s} {:30s} {:30s}'.format('Nazwa', 'Nowa nazwa', 'Typ'))
    print('------------------------------------------------------------')

    for file, trans in zip(to_rapair, translated):
        if os.path.isfile(os.getcwd() + '/' + file):
            file_type = 'plik'
        else:
            file_type = 'katalog'
        print('{:30s} {:30s} {:30s}'.format(file, trans, file_type))

    return translated

# zmienia nazwy plikow korzystajac z list to_repair, translated
def repair(to_repair, translated):
    """
    Change names of files.
    :param to_repair: list[str]
    :param translated: list[str]
    :return: None
    """

    for file, trans in zip(to_repair, translated):
        os.rename(file, trans)
    print('Zrobione!')


if __name__ == "__main__":
    REGEX = '[a-zA-Z0-9._-]+'
    DICT_TRANSLATE = {'ą': 'a', 'Ą': 'A',
                 'ę': 'e', 'Ę': 'E',
                 'ć': 'c', 'Ć': 'C',
                 'ó': 'o', 'Ó': 'O',
                 'ł': 'l', 'Ł': 'L',
                 'ń': 'n', 'Ń': 'N',
                 'ż': 'z', 'Ż': 'Z',
                 'ź': 'z', 'Ź': 'Z',
                 'ś': 's', 'Ś': 'S', ' ': '_'}

    to_rapair = check(REGEX)

    if os.path.basename(__file__) in to_rapair:         # gdyby nazwa samego skryptu naprawiajacego byla niepoprawna
        to_rapair.remove(os.path.basename(__file__))    # wyklucz z listy

    translated = translate(to_rapair, DICT_TRANSLATE, REGEX)

    answer = input('\nCzy naprawic pliki? [tak - jesli jestes pewien]: ')
    answer = answer.lower().strip()
    if answer == 'tak':
        repair(to_rapair, translated)
    else:
        print('Dziękuję. Do zobaczenia.')
