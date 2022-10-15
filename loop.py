from rembg import remove
from PIL import Image
# treka=Image.open("F:\Python\Images\Abokreka.jpg")
# treka.show()
# box = (100, 100, 400, 400)
# new_image = treka.crop(box)
# new_image.show()
# print(treka.format, treka.size, treka.mode)
# input_path = 'F:\Python\Images\Abokreka.jpg'
# output_path = 'output.jpg'
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)

def say_hello(name):
    ''' This is the first Documenting '''
    print(f"Hi, {name}") 

say_hello("Ahmed")    
help(say_hello)
print(say_hello.__doc__)