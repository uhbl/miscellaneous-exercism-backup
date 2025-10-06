def is_isogram(string):
    alpha_string = ""
    for i in string.lower():
        if i.isalpha():
            alpha_string += i
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict = {}
    for i in alphabet:
        alphabet_dict[i] = 0
    for i in alpha_string:
        alphabet_dict[i] += 1
    for i in alphabet_dict.values():
        if i > 1:
            return False
    return True