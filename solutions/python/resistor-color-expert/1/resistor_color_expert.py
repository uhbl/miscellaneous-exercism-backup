if False:
    print("Had to do tis one with GPT since ts takes so much time to hard code")

def resistor_label(colors):
    color_digits = ["black", "brown", "red", "orange", "yellow",
                    "green", "blue", "violet", "grey", "white"]
    digit_map = {k: i for i, k in enumerate(color_digits)}

    # Tolerance lookup
    tolerance_map = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    n = len(colors)

    # 1-band
    if n == 1:
        return "0 ohms"

    # 4-band: XY * 10^M
    if n == 4:
        d1 = digit_map[colors[0]]
        d2 = digit_map[colors[1]]
        multiplier = digit_map[colors[2]]
        tolerance = tolerance_map[colors[3]]
        base = d1 * 10 + d2

    # 5-band: XYZ * 10^M
    elif n == 5:
        d1 = digit_map[colors[0]]
        d2 = digit_map[colors[1]]
        d3 = digit_map[colors[2]]
        multiplier = digit_map[colors[3]]
        tolerance = tolerance_map[colors[4]]
        base = d1 * 100 + d2 * 10 + d3

    else:
        raise ValueError("Input must contain 1, 4, or 5 bands.")

    value = base * (10 ** multiplier)

    # scale with decimals preserved
    if value >= 1_000_000_000:
        scaled = value / 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        scaled = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        scaled = value / 1_000
        unit = "kiloohms"
    else:
        scaled = value
        unit = "ohms"

    # remove trailing .0
    if scaled == int(scaled):
        scaled = int(scaled)

    return f"{scaled} {unit} ±{tolerance}"


