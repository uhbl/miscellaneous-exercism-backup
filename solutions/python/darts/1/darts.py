def score(x, y):
    hypotenuse = (x**2 + y**2)**(1/2)
    if hypotenuse > 10:
        return 0
    elif 5 < hypotenuse <= 10:
        return 1
    elif 1 < hypotenuse <= 5:
        return 5
    elif hypotenuse <= 1:
        return 10