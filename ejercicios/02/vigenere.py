
from collections import Counter 

def sanitize(plaintext):
    sane: str = plaintext.encode('ascii', errors='ignore').decode().upper()
    return sane.translate({ord(i): None for i in ' .,;:!?'})

def encrypt(plaintext, key):
    """ Si la clave tiene una sola letra, es un césar """
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


def encrypt_file(filename, key, output, bs=512):
    """ Ojo: cifra línea a línea, no como un todo """
    with open(filename, newline='\n') as fin:
        with open(output, 'w', newline='\n') as fout:
            for l in fin:
                d = encrypt(sanitize(l.strip()), key)
                fout.write(d + '\n')


def decrypt_file(filename, key, output, bs=512):
    """ Ojo: descifra línea a línea, no como un todo """
    with open(filename) as fin:
        with open(output, 'w') as fout:
            for l in fin:
                d = decrypt(sanitize(l.strip()), key)
                fout.write(d + '\n')

if __name__ == '__main__':
    # plain = 'Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como estan de razon y conciencia, deben comportarse fraternalmente los unos con los otros.'
    plain = 'Reposa aquí Dulcinea'
    key = 'ABCDE'
    ciphered = encrypt(sanitize(plain), key)
    deciphered = decrypt(ciphered, key)

    print(ciphered)
    print(deciphered)
    print(Counter(ciphered))

    encrypt_file('el_quijote.txt', 'd', 'el_quijote.caesar')
    encrypt_file('el_quijote.txt', 'SESAMO', 'el_quijote.vigenere')
    decrypt_file('el_quijote.caesar', 'd', 'el_quijote.decrypt')
    decrypt_file('el_quijote.vigenere', 'SESAMO', 'el_quijote.decrypt2')
    
