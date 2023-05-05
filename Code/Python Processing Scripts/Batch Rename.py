import os

#nameRoot = r"C://Users//rebel//Desktop//Research_with_Liu//FRLL and London Dataset//neutral_aligned//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//IJCB//frll//source_printscan//neutral_aligned//"

#nameRoot = r"C://Users//rebel//Desktop//Research_with_Liu//FRLL and London Dataset//smiling_aligned//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//biosig//biosig2022//IJCB//frll//source_printscan//smiling_aligned//"

#nameRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Clarkson Dataset//Stills//bonefide_cu_aligned//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Clarkson Dataset//JPG//Stills//CU Source Images PS//"

#nameRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Feret//Source Images//alignedResizedNot//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Feret Dataset//JPG//Source Images//i2//Feret_S_Renamed//"

#nameRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Feret//Source Images//feretUsed//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//Feret Dataset//JPG//Source Images//Intermediary//Feret Stills Renamed//"

#nameRoot = r"C://Users//rebel//Desktop//Research_with_Liu//FRGC Morphs//Source Images//alignedResizedNot//"
#fileRoot = r"C://Users//rebel//Desktop//Research_with_Liu//Ranked Morph Pages//FRGC Dataset//JPG//Source Images//FRGC_Source_Processed_1-173//"

fileRoot = r"C:\Users\rebel\Desktop\Research_with_Liu\Clarkson_Dataset\Diffusion\morph_digital//"
nameRoot = r"C:\Users\rebel\Downloads\morph-diffusion\morph-diffusion//"

#list of files in folder to rename
files = os.listdir(fileRoot)

#list of files in folder with names
files2 = os.listdir(nameRoot)

for i, file in enumerate(files):
    os.rename(os.path.join(fileRoot, file), os.path.join(fileRoot, ''.join([files2[i]])))
    print(i)
    