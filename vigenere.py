def vigenere(phrase, key):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    crypt = ''
    for n, l in enumerate(phrase):
        p = n % len(key)
        nl = (alph.index(l) + alph.index(key[p])) % 26
        crypt += alph[nl]
    return crypt


def reverse_vigenere(encrypted, key):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decrypt = ''
    for n, l in enumerate(encrypted):
        p = n % len(key)
        nl = (alph.index(l) - alph.index(key[p]) + 26) % 26
        decrypt += alph[nl]
    return decrypt
