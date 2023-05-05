import os
from PIL import Image

#fileRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\Ranked Morph Pages\Clarkson Dataset\E4E\I\part4_cleaned//"
#fileRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\IJCB\clarkson_e4e\821-863//"
fileRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\Clarkson_Dataset\Diffusion\morph_diffusion_cropped_resized//"

def resize_and_crop_images(fileRoot, filename):
    img = Image.open(fileRoot + filename)
    width, height = img.size
    if width > height:
        delta = width - height
        left = int(delta/2)
        upper = 0
        right = height + left
        lower = height
    else:
        delta = height - width
        left = 0
        upper = int(delta/2)
        right = width
        lower = width + upper
    img = img.crop((left, upper, right, lower))
    img = img.resize((600, 600), Image.LANCZOS)
    img.save(os.path.join(fileRoot, filename), quality = 100)

count = 1

for filename in os.listdir(fileRoot):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        resize_and_crop_images(fileRoot, filename)
    else:
        continue
    print(count)
    count = count + 1