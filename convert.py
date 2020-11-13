def convert(hex_code):
    if len(hex_code.split('#')) != 2 or len(hex_code.split("#")[1]) != 6:
        return
    hex_code = hex_code.lstrip("#")
    color_tuple = tuple(int(hex_code[x: x+2], 16) for x in (0, 2, 4))
    return color_tuple


if __name__ == "__main__":
    rgb = convert("#ffffff") # passing in the hex value -> white
    print(rgb) # printing the result -> (255, 255, 255)