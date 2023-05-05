import os
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

fontRoot = r"C://Users//rebel//Desktop//Research_with_Liu//FRLL and London Dataset//Font//aver-font//Aver-opKo.ttf"

morphRoot = r"C:\Users\rebel\Downloads\morphs\feret\morph_diffusionC//"
morphPageRoot = r"C:\Users\rebel\Downloads\morphs//FERET Diff Pages//"
pageName = "FERET_DiffusionC_Print_Page_"

imageHeight = 600
imageWidth = 600
lrMargin = 188
tpMargin = 180

font = ImageFont.truetype(fontRoot, 52)


def get_morph_pages(file_count):
    morphPages = file_count / 12
    morphPages = math.ceil(morphPages) + 1
    return morphPages


def make_morph_pages(morphPages):
    pageCountTwo = 1

    for morphPages in range(1, morphPages):
        pageCountStringTwo = str(pageCountTwo)
        fullTwo = pageCountStringTwo.zfill(2)
        Image_Rename_Two = morphPageRoot + pageName + fullTwo + ".png"
        imgb = Image.new("RGB", (2550, 3300), (255, 255, 255))
        imgb.save(Image_Rename_Two, 'PNG')
        pageCountTwo = pageCountTwo + 1
    return


def pasteImages(counter, counterTwo, pageCounter, filename, file_extension):
    img2 = Image.open(morphRoot + filename + file_extension)
    saveType = ".png"
    temp = str(math.ceil(pageCounter / 4))
    pageCounterStringTwo = temp
    fulltwo = pageCounterStringTwo.zfill(2)

    img6 = Image.open(morphPageRoot + pageName + fulltwo + saveType)
    draw = ImageDraw.Draw(img6)

    if counter == 1:
        img6.paste(img2, (lrMargin * counter + imageWidth * (counter - 1), tpMargin * counterTwo + imageHeight * (counterTwo - 1)))
        img6.save((morphPageRoot + pageName + fulltwo + saveType), 'PNG', quality=100)
        if counterTwo == 1:
            draw.text((2200, 3200), pageCounterStringTwo + " FERET DC", (0, 0, 0), font=font)
            img6.save(morphPageRoot + pageName + fulltwo + saveType, 'PNG', quality=100)

    elif counter == 2:
        img6.paste(img2, (lrMargin * counter + imageWidth * (counter - 1), tpMargin * counterTwo + imageHeight * (counterTwo - 1)))
        img6.save(morphPageRoot + pageName + fulltwo + saveType, 'PNG', quality=100)

    elif counter == 3:
        img6.paste(img2, (lrMargin * counter + imageWidth * (counter - 1), tpMargin * counterTwo + imageHeight * (counterTwo - 1)))
        img6.save(morphPageRoot + pageName + fulltwo + saveType, 'PNG', quality=100)
        counterTwo = counterTwo + 1

    counter = counter + 1

    return counter, counterTwo


location = morphPageRoot

# Check whether the specified path exists or not
isExist = os.path.exists(location)

if not isExist:
    # Create a new directory because it does not exist 
    os.makedirs(location)
    print("The new directory is created!")
else:
    print("The directory exists!")

# Counts the number of files in the morphs folder desired
path, dirs, fileCount = next(os.walk(morphRoot))
file_count = len(fileCount)
morphPages = get_morph_pages(file_count)
make_morph_pages(morphPages)

pageCounter = 1
pageCounterTwo = 1
identityCounter = 1
counter = 1
counterTwo = 1
fileType = ".png"
test_count = 1
progress = 0

for file in os.listdir(morphRoot):
    if file.endswith(fileType):
        filename, file_extension = os.path.splitext(file)
        if counter > 3:
            counter = 1
            pageCounter = pageCounter + 1
        if counter <= 3:
            if counterTwo > 4:
                counterTwo = 1
            counter, counterTwo = pasteImages(counter, counterTwo, pageCounter, filename, file_extension)
            progress = progress + 1
            print(progress)
    else:
        continue
