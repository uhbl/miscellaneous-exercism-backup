def decode(string):
    num_list = []
    alpha_list = []
    temp = ""
    for i, k in enumerate(string):
        if k.isnumeric():
            if string[i + 1].isnumeric():
                temp += k
            else:
                temp += k
                num_list.append(temp)
                temp = ""
        else:
            try:
                if string[i + 1].isnumeric():
                    alpha_list.append(k)
                else:
                    alpha_list.append(k)
                    num_list.append("1")
            except IndexError:
                alpha_list.append(k)
                num_list.append("1")
    decoded = ""
    for i, k in enumerate(alpha_list):
        decoded += int(num_list[i]) * k
    return decoded

def encode(string):
    ltr = ""
    sc = 0
    enc = ""
    string += "+"
    for k, i in enumerate(string):
        if i != ltr:
            if sc == 1:
                enc += (str(ltr))
            else:
                enc += (str(sc) + str(ltr))
            ltr = i
            sc = 1
        elif k + 1 == len(string):
            if i == string[k - 1]:
                if sc == 1:
                    enc += (str(ltr))
                else:
                    enc += (str(sc) + str(ltr))
            else:
                enc += ("1" + i)
        else:
            sc += 1
    return enc[1::]