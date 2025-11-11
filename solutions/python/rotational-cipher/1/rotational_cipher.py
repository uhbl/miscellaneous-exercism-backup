def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = alphabet[(key):] + alphabet[:(key)]
    cipher_dict = dict(zip(alphabet, cipher))
    encrypted = []
    for i in text:
        if i.isupper():
            encrypted.append(cipher_dict[i.lower()].upper())
        elif i.islower():
            encrypted.append(cipher_dict[i])
        else:
            encrypted.append(i)
    return "".join(encrypted)