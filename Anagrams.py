from random import *
from DEFS.numbers import factorial

letters = []
anagrams = []
verif = []
wrd = ''
count = 0
fac = 1

word = str(input('Word: ')).strip().lower()
anagrams.append(word)

for le in word:
		letters.append(le)
    if le not in verif:
        n = word.count(le)
        fac = fac * factorial(n)
        verif.append(le)

while count != ((factorial(len(letters)) / fac) - 1):
    shuffle(letters)
    for le in letters:
        wrd += le
    if wrd not in anagrams:
        anagrams.append(wrd)
        count += 1
    wrd = ''
print(anagrams)
