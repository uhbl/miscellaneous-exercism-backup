def color_code(color):
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    decoder = {k: i for i, k in enumerate(colors)}
    return decoder[color]


def colors():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]