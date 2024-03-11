from PIL import Image

CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", "!", ",", ".",]

def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)   

def grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def to_ascii(image):
    pixels = image.getdata()
    characters = "".join(CHARS[pixel//25] for pixel in pixels)
    return(characters)

def main(new_width=100):
    path = input('Please type the path to the photo: ')
    try:
        image = Image.open(path)
    except:
        print('Invalid pathname')

    new_image_data = to_ascii(grayscale(resize(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()