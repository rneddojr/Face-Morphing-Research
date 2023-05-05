import os
from PIL import Image

###################################                              Clarkson                                        #####################################

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank A//Rank A Script 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank A//Rank A Script 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank A//Rank A Script 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank A//Rank A Script 650 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank A//Rank A Epson 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank A//Rank A Epson 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank A//Rank A Epson 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank A//Rank A Epson 650 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank B//Rank B Script 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank B//Rank B Script 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank B//Rank B Script 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank B//Rank B Script 650 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank B//Rank B Epson 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank B//Rank B Epson 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Rank B//Rank B Epson 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Rank B//Rank B Epson 650 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Stills//CU Stills Script 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Stills//CU Stills Script 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Stills//CU Stills Script 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Stills//CU Stills Script 650 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Stills//CU Stills Epson 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Stills//CU Stills Epson 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Stills//CU Stills Epson 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//PNG//Stills//CU Stills Epson 650 PS//"

###################################                                FRLL                                         #####################################

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//JPG//Morphs//FRLL Morphs Script 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//PNG//Morphs//FRLL Morphs Script 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//JPG//Morphs//FRLL Morphs Script 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//PNG//Morphs//FRLL Morphs Script 650 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//JPG//Stills//FRLL Stills Script 600 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//PNG//Stills//FRLL Stills Script 600 PS//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//JPG//Stills//FRLL Stills Script 650 PS//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRLL Dataset//PNG//Stills//FRLL Stills Script 650 PS//"

####################################
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//feretUsed//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Source Images//"

#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//frll//morphs//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//frll//source_images//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//frgc//morphs//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//frgc//source_images//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//feret//morphs//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//feret//source_images//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//clarkson_a//morphs//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//clarkson_a//source_images//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//clarkson_b//morphs//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//clarkson_b//source_images//"

#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//frll//png//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//frgc//png//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//feret//png//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//clarkson_a//png//"
#saveRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//Analyze//PSM_PSS//run//clarkson_b//png//"

#fileRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\Ranked Morph Pages\Feret Dataset\JPG\Source Images\Feret Stills PS//"
#saveRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\Ranked Morph Pages\Feret Dataset\PNG\Source Images\Feret Stills PS//"

fileRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\Ranked Morph Pages\FRGC Dataset\JPG\Source Images\FRGC Sources PS//"
saveRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\Ranked Morph Pages\FRGC Dataset\PNG\Source Images\FRGC Stills PS//"

path = saveRoot

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if not isExist:
    # Create a new directory because it does not exist 
    os.makedirs(path)
    print("The new directory is created!")
else:
    print("The directory exists!")

count = 1

for file in os.listdir(fileRoot):      # all files in directory
    print(count)
    image = Image.open(fileRoot + file)
    finename, extension = file.split(".")
    image.save(saveRoot + finename + ".png")
    count += 1
    