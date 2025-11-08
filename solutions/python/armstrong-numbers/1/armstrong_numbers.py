def is_armstrong_number(number):
    numlist = [int(i) for i in str(number)]
    length = len(str(number))
    armstrong = 0
    for i in numlist:
        armstrong += i ** length
    if armstrong == number:
        return True
    else:
        return False