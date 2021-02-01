def vigenere(phrase, key):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cript = ''
    for n, l in enumerate(phrase):
        p = n % len(key)
        nl = (alph.index(l) + alph.index(key[p])) % 26
        cript += alph[nl]
    return cript
