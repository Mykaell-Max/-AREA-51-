# num > binary
def binary(num):
    b = ''
    while True:
        if num == 1 or num == 0:
            b += f'{str(num)} '
            break
        bi = num % 2
        num //= 2
        b += f'{str(bi)} '
    l = b.split()
    l.reverse()
    b = ''
    for n in l:
        b += f'{str(n)}'
    return b


#binary > num
def rbinary(bi):
    num = 0
    l = []
    bi = str(bi)
    for n in bi:
        l.append(n)
    l.reverse()
    for m, n in enumerate(l):
        num += int(n) * (2 ** m)
    return num
