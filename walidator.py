import os
import re

print('Lokalizacja: ', os.getcwd(), end = '\n\n')
# print(os.listdir('./test'))

for file in os.listdir('./test'):
    valid_file = re.fullmatch("[a-zA-Z0-9._]+",file)
    if valid_file is None:
        print('Bledna nazwa:',file)

