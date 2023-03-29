from PIL import Image


def decrypt_image(img_path):
    img = Image.open(img_path)
    pixels = img.load()
    res_string = ""
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pixels[x, y] == (0, 0, 0):
                res_string += chr(y)
    return res_string


decrypt_image("code.png")

