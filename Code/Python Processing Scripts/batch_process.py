import os
from PIL import Image

#If arg = 1 do pre-crop, if arg = 2 do post-crop
arg = 1
scanRoot = r"C:\Users\xxxxx\images_to_process//"
saveRoot0 = r"C\Users\xxxxx\scans_adjusted//"
saveRoot1 = r"C:\Users\xxxxx\images_splilt//"
saveRoot2 = r"C:\Users\xxxxx\images_to_crop//"

#arg = 2
#scanRoot = r"C:\Users\xxxxx\images_cropped//"
#saveRoot1 = r"C:\Users\xxxxx\images_cleaned//"
#saveRoot2 = saveRoot1
#saveRoot0 = ""


# Check whether the specified path exists or not
def checkExists(path):
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")
    else:
        print("The directory exists!")

        
def precrop_image(scanRoot, file, crop_bottom):
    image = Image.open(scanRoot+file)
    pre_width, pre_height = image.size
    cropped = image.crop((0, 0, pre_width, pre_height - crop_bottom))
    cropped.save(saveRoot0+file, quality=100)

    
def separate(original_location, filename, xPieces, yPieces, save_location):
    separate_input = original_location + filename
    imgname, file_extension = os.path.splitext(filename)
    im = Image.open(separate_input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            newname = save_location + imgname + "_" + str(i) + "_" + str(j) + file_extension
            a.save(newname, quality=100)


def cut(original_location, filename, save_location):
    cut_input = original_location + filename
    imgname, file_extension = os.path.splitext(filename)
    im = Image.open(cut_input)
    imgwidth, imgheight = im.size
    height = imgheight - 80
    width = imgwidth
    if "_3_0" in imgname:
        box = (0, 0, width, height)
        a = im.crop(box)
        newname = save_location + imgname + file_extension
        a.save(newname, quality=100)
    elif "_3_1" in imgname:
        box = (0, 0, width, height)
        a = im.crop(box)
        newname = save_location + imgname + file_extension
        a.save(newname, quality=100)
    elif "_3_2" in imgname:
        box = (0, 0, width, height - 40)
        a = im.crop(box)
        newname = save_location + imgname + file_extension
        a.save(newname, quality=100)
    else:
        newname = save_location + imgname + file_extension
        im.save(newname, quality=100)


def clean(original_location, filename, save_location):
    clean_input = original_location + filename
    imgname, file_extension = os.path.splitext(filename)
    im = Image.open(clean_input)
    imgwidth, imgheight = im.size
    height = imgheight - 2
    width = imgwidth - 2
    box = (2, 2, width, height)
    a = im.crop(box)
    newname = save_location + imgname + file_extension
    a.save(newname, quality=100)


def main():
    countOne = 1
    countTwo = 1

    if arg == 1:
        path = saveRoot1
        path2 = saveRoot2
        checkExists(path)
        checkExists(path2)
        print("Separating Images")
        for file in os.listdir(scanRoot):
            print(countOne)
            xPieces = 3
            yPieces = 4
            precrop_image(scanRoot, file, 50)
            separate(saveRoot0, file, xPieces, yPieces, saveRoot1)
            countOne += 1

        print("Cutting Numbers")
        for file2 in os.listdir(saveRoot1):
            print(countTwo)
            cut(saveRoot1, file2, saveRoot2)
            countTwo += 1

    elif arg == 2:
        path = saveRoot1
        checkExists(path)
        print("Cleaning Cropped Images")
        for file in os.listdir(scanRoot):
            print(countOne)
            print(file)
            clean(scanRoot, file, saveRoot1)
            countOne += 1


if __name__ == "__main__":
    main()
