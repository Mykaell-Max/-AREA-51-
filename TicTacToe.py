from random import *
from DEFS.numbers import lint

playagain = 'Y'
turns = pvictory = cvictory = 0
# 1=cpu #2=player
whoplays = 2
maxturns = 9
vict = 'n'
game = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def screen():
    global game
    global turns
    print('\033[35m=\033[m' * 14)
    print('   \033[36;4m0\033[m   \033[36;4m1\033[m   \033[36;4m2\033[m')
    print(f'\033[36m0|\033[m \033[31m{game[0][0]}\033[m \033[32m|\033[m \033[31m{game[0][1]}\033[m \033[32m|\033[m \033[31m{game[0][2]}\033[m ')
    print('   \033[32m----------\033[m')
    print(f'\033[36m1|\033[m \033[31m{game[1][0]}\033[m \033[32m|\033[m \033[31m{game[1][1]}\033[m \033[32m|\033[m \033[31m{game[1][2]}\033[m ')
    print('   \033[32m----------\033[m')
    print(f'\033[36m2|\033[m \033[31m{game[2][0]}\033[m \033[32m|\033[m \033[31m{game[2][1]}\033[m \033[32m|\033[m \033[31m{game[2][2]}\033[m ')
    print('\033[35m=\033[m'*14)
    print(f'\033[34mTurn:\033[m \033[33m{turns}\033[m')


def player():
    global turns
    global whoplays
    global vict
    global maxturns
    if whoplays == 2 and turns < maxturns:
        l = lint('\033[1;33mLine: ')
        c = lint('Column:\033[m ')
        try:
            while game[l][c] != ' ':
                print('\033[31mInvalid place\033[m')
                l = lint('\033[1;33mLine: ')
                c = lint('Column:\033[m ')
            game[l][c] = 'X'
            whoplays = 1
            turns += 1
        except:
            print('\033[31mInvalid line or column!\033[m')


def computer():
    global turns
    global whoplays
    global vict
    global maxturns
    if whoplays == 1 and turns < maxturns:
        l = randint(0, 2)
        c = randint(0, 2)
        while game[l][c] != ' ':
            l = randint(0, 2)
            c = randint(0, 2)
        game[l][c] = 'O'
        whoplays = 2
        turns += 1


def verifyvict():
    global game
    victory = 'n'
    symbols = ['X', 'O']
    for s in symbols:
        victory = 'n'
        # line----------------
        il = ic = 0
        while il < 3:
            sum = 0
            ic = 0
            while ic < 3:
                if game[il][ic] == s:
                    sum += 1
                ic += 1
            if sum == 3:
                victory = s
                break
            il += 1
        if victory != 'n':
            break
        # column---------------
        il = ic = 0
        while ic < 3:
            sum = 0
            il = 0
            while il < 3:
                if game[il][ic] == s:
                    sum += 1
                il += 1
            if sum == 3:
                victory = s
                break
            ic += 1
        if victory != 'n':
            break
        # diagonal 1--------------
        sum = 0
        idiag = 0
        while idiag < 3:
            if game[idiag][idiag] == s:
                sum += 1
            idiag += 1
        if sum == 3:
            victory = s
            break
        # diagonal 2--------------
        sum = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if game[idiagl][idiagc] == s:
                sum += 1
            idiagl += 1
            idiagc -= 1
        if sum == 3:
            victory = s
            break
    return victory


def reset():
    global game
    global turns
    global whoplays
    global maxturns
    global vict
    turns = 0
    whoplays = 2
    maxturns = 9
    vict = 'n'
    game = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]


while playagain == 'Y':
    while True:
        screen()
        player()
        vict = verifyvict()
        if vict != 'n' or turns >= maxturns:
            break
        computer()
        vict = verifyvict()
        if vict != 'n' or turns >= maxturns:
            break
    print('\033[35m=\033[m' * 14)
    screen()
    print('\033[1;36mResult:\033[m')
    if vict == 'X':
        print('\033[1;31mPlayer won!\033[m')
        pvictory += 1
    if vict == 'O':
        print('\033[1;33mComputer won!\033[m')
        cvictory += 1
    if vict != 'X' and vict != 'O':
        print('\033[1;34mIts a tie!\033[m')
    print('\033[35m=\033[m' * 14)
    playagain = input('\033[1;34mPlay again? [Yes/No]:\033[m ').strip().upper()[0]
    reset()
print('\033[35m=\033[m' * 14)
print('\033[31m=STATISTICS=\033[m')
print(f'\033[1;36mPlayers victories: \033[1;31m{pvictory}\033[m')
print(f'\033[1;36mComputers victories: \033[1;31m{cvictory}\033[m')
print('\033[35m=\033[m' * 14)
print(f'\033[1;31;40mEND\033[m')
