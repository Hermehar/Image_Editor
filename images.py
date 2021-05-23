from simpleimage import SimpleImage
INTENSITY_THRESHOLD = 1.6
DEFAULT_FILE = '  ' #enter your default file name

def get_file():
    filename = input('Enter image file (or press enter for default): ')                       """user imput"""
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def redscreen(main_filename, back_filename):                                                     """used for redscreen"""
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * INTENSITY_THRESHOLD:                                   
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image

def darker(image):                                                                      """gets you the darker version of the image"""
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2                                                
        pixel.blue = pixel.blue // 2

def red_channel(filename):                                                         """converts the image into red color"""
    for pixel in filename:
        pixel.green = 0
        pixel.blue = 0                                                             
    return filename

def compute_luminosity(red, green, blue):
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def grayscale(filename):                                                           """gets you the black and white version of the image"""
    for pixel in filename:
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return filename

def mirror_hor(filename):                                                           """gets you the horizontal mirror image of the image"""
    width = filename.width
    height = filename.height
    mirror_hor = SimpleImage.blank(width*2, height)
    for x in range (width):
        for y in range (height):
            pixel = filename.get_pixel(x, y)
            mirror_hor.set_pixel(x, y, pixel)
            mirror_hor.set_pixel((width *2) - (x+1) ,y ,pixel)
    return mirror_hor

def mirror_ver(filename):                                                         """gets you the vertical mirror image of the image"""
    width = filename.width
    height = filename.height
    mirror_ver = SimpleImage.blank(width, height*2)
    for x in range (width):
          for y in range (height):
            pixel = filename.get_pixel(x, y)
            mirror_ver.set_pixel(x, y, pixel)
            mirror_ver.set_pixel(x,(height*2)-(y+1),pixel)
    return mirror_ver

def main():
    filename = get_file()
    x = input("Please enter your selection out of Grayscale, Red_Channel, Horizontal_Mirror, Vertical_Mirror or Darker: ")
    
    if x == str('Grayscale'):
        filename = SimpleImage(filename)
        grayscale_filename = grayscale(filename)
        grayscale_filename.show()

    elif x == str('Red_Channel'):
        filename = SimpleImage(filename)
        red_filename = red_channel(filename)
        red_filename.show()

    elif x == str('Red_Screen'):
        filename = SimpleImage(filename)
        red_filename = red_channel(filename)
        red_filename.show()
    
    elif x == str('Horizontal_Mirror'):
        filename = SimpleImage(filename)
        mirror_hor_filename = mirror_hor(filename)
        mirror_hor_filename.show()
    
    elif x == str('Vertical_Mirror'):
        filename = SimpleImage(filename)
        mirror_ver_filename = mirror_ver(filename)
        mirror_ver_filename.show()

    elif x == str('Darker'):
        filename = SimpleImage(filename)
        darker(filename)
        filename.show()

    else:
        filename = SimpleImage(filename)
        grayscale_filename = grayscale(filename)
        grayscale_filename.show()
        red_filename = red_channel(filename)
        red_filename.show()
        darker(filename)
        filename.show()
        mirror_hor_filename = mirror_hor(filename)
        mirror_hor_filename.show()
        mirror_ver_filename = mirror_ver(filename)
        mirror_ver_filename.show()

        
if __name__ == '__main__':
    main()
