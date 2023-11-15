import openai,hugface
import io, sys,os
from PIL import Image

prmpt = input("\033[48;5;196mhellio, what image do you want\n\033[;0m")
file_name = input("Save as: ")
print("\n\nprompt is: ",prmpt)
image_reply = hugface.genArt(prmpt)
image = Image.open(io.BytesIO(image_reply))

try:
    
    image.save(f'{file_name}.jpg')
    print("using jpg")
except:
    print("using png")
    if os.path.exists(f'{file_name}.jpg'):
        os.remove(f'{file_name}.jpg')
    else:
        print("The file does not exist")
    image.save(f'{file_name}.png')