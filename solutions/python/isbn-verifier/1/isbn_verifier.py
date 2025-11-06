def is_valid(isbn):

    # Set the variables
    allowed = set("0123456789-X")
    multiplier = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    new_isbn = []

    # False if char is not in allowed and char is X but not last
    for i, k in enumerate(isbn):
        if k in allowed:
            if k == "X" and i != len(isbn)-1:
                return False
            new_isbn += k
        else:
            return False

    # Creates new list containing only valid chars and checks the length
    new_list = [i for i in new_isbn if i.isdigit() or i == "X"]
    if len(new_list) != 10:
        return False

    # Creates final list where everything is converted to a number
    final_list = []
    for i in new_list:
        if i.isdigit():
            final_list.append(int(i))
        elif i == "X":
            final_list.append(10)

    # Calculating the value and determining the validity
    value = 0
    for i, k in enumerate(final_list):
        value += k * multiplier[i]
    if value % 11 == 0:
        return True
    else:
        return False
