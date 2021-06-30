from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.6
DEFAULT_FILE = 'image1.jpg'
DEFAULT_FILE_BACK ='normal.jpg'

def get_file():
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def get_file_back():
    filename_back = input("Enter image file : ")
    if filename_back == '':
        filename_back = DEFAULT_FILE_BACK
    return filename_back

def redscreen(filename, back_filename):
    front = SimpleImage(filename)
    back = SimpleImage(back_filename)
    for pixel in front:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * INTENSITY_THRESHOLD:
            x = pixel.x
            y = pixel.y
            front.set_pixel(x, y, back.get_pixel(x, y))
    return front

def darker(image):
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2 
        pixel.blue = pixel.blue // 2

def red_channel(filename):
    for pixel in filename:
        pixel.green = 0
        pixel.blue = 0
    return filename

def compute_luminosity(red, green, blue):
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def grayscale(filename):
    for pixel in filename:
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return filename

def mirror_hor(filename):
    width = filename.width
    height = filename.height
    mirror_hor = SimpleImage.blank(width*2, height)
    for x in range (width):
        for y in range (height):
            pixel = filename.get_pixel(x, y)
            mirror_hor.set_pixel(x, y, pixel)
            mirror_hor.set_pixel((width *2) - (x+1) ,y ,pixel)
    return mirror_hor

def mirror_ver(filename):
    width = filename.width
    height = filename.height
    mirror_ver = SimpleImage.blank(width , height*2)
    for x in range (width):
          for y in range (filename.height):
            pixel = filename.get_pixel(x, y)
            mirror_ver.set_pixel(x, y, pixel)
            mirror_ver.set_pixel(x,((filename.height)*2)-(y+1),pixel)
    return mirror_ver

def main():
    filename = get_file()

    x = input("Please enter your selection out of Grayscale, Red_Channel, Horizontal_Mirror, Vertical_Mirror or Darker: ")
   
    if x == str('Grayscale'):
        filename = SimpleImage(filename)
        filename.show()
        grayscale_filename = grayscale(filename)
        grayscale_filename.show()

    elif x == str('Red_Channel'):
        filename = SimpleImage(filename)
        filename.show()
        red_filename = red_channel(filename)
        red_filename.show()

    elif x == str('Horizontal_Mirror'):
        filename = SimpleImage(filename)
        filename.show()
        mirror_hor_filename = mirror_hor(filename)
        mirror_hor_filename.show()
    
    elif x == str('Vertical_Mirror'):
        filename = SimpleImage(filename)
        filename.show()
        mirror_ver_filename = mirror_ver(filename)
        mirror_ver_filename.show()

    elif x == str('Darker'):
        filename = SimpleImage(filename)
        filename.show()
        darker(filename)
        filename.show()

    else:
        filename = get_file()
        filename_back = get_file_back()
        original_front_image = SimpleImage(filename)
        original_front_image.show()
        original_back_image = SimpleImage(filename_back)
        original_back_image.show()
        replaced_image = redscreen(filename, filename_back)
        replaced_image.show()
        
if __name__ == '__main__':
    main()
