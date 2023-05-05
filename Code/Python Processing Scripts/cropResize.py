import os
from PIL import Image

fileRoot = r"C:\Users\xxxx\imgs_to_resize//"

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