function vigenere(phrase, key) {
    let alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let cript = ''
    for(let n = 0; n < phrase.length; n++) {
        let p = n % key.length
        let nl = (alph.indexOf(phrase[n]) + alph.indexOf(key[p])) % 26
        cript += alph[nl]
    }
    return cript
}
