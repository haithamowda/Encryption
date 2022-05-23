import os
clear = lambda: os.system('cls')
piphashlib = lambda: os.system('pip install hashlib')
piphashlib()
clear()
pipcolorama = lambda: os.system('pip install colorama')
pipcolorama()
clear()
from hashing import hashtext
import time, sys
from time import sleep
from colorama import init, Fore, Back, Style

def _logo_():
    logo = '''

    ┌─┐┬    ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┬    ┬ ┬┌─┐┬┌┬┐┬ ┬┌─┐┌┬┐
    ├─┤│    │ ┬├┤ │││├┤ ├┬┘├─┤│    ├─┤├─┤│ │ ├─┤├─┤│││
    ┴ ┴┴─┘  └─┘└─┘┘└┘└─┘┴└─┴ ┴┴─┘  ┴ ┴┴ ┴┴ ┴ ┴ ┴┴ ┴┴ ┴
    '''
    exp = 'Telegram And Whatsapp +970597668158'
    for lo in logo:
        sleep(0.03)

        sys.stdout.write(Fore.BLUE + lo)
    for l in exp:
        sleep(0.02)
        sys.stdout.write(l)

    print('\n')
_logo_()

text = str(input ("plz your text > "))
hashtype = str(input("plz your hashtype > "))
while text == '':
    print("plz your text !!")
    text = str(input ("plz your text > "))


while hashtype == '':
    print("plz your hashtype !!")
    hashtype = str(input("plz your hashtype > "))

h = hashtext()
print(h.hashingtext (text,hashtype))
