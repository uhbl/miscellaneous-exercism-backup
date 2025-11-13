def value(colors):
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    decoder = {k: i for i, k in enumerate(colors_list)}
    resistance = ""
    for i in colors[:2:]:
        resistance += str(decoder[i])
    return int(resistance)