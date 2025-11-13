def label(colors):
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    decoder = {k: i for i, k in enumerate(colors_list)}

    base = int(str(decoder[colors[0]]) + str(decoder[colors[1]]))
    multiplier = decoder[colors[2]]
    value = base * (10 ** multiplier)

    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000:
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"
