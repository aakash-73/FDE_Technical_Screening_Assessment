def sort(width, height, length, mass):
    volume = width * height * length
    bulky = True if volume >= 1_000_000 or max(width, height, length) >= 150 else False
    heavy = True if mass >= 20 else False

    return (
        "REJECTED" if bulky and heavy
        else "SPECIAL" if bulky or heavy
        else "STANDARD"
    )
