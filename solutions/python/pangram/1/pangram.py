def is_pangram(sentence):
    single_string_alphabet = "abcdefghijklmnopqrstuvwxyz"
    temp_dict = {}
    for i in single_string_alphabet:
        temp_dict[i] = 0
    for i in sentence.lower():
        if i in temp_dict:
            temp_dict[i] += 1
    for i in temp_dict.values():
        if i == 0:
            return False
    return True