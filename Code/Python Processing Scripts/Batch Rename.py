import os

fileRoot = r"C:\Users\xxxx\files_to_rename//"
nameRoot = r"C:\Users\xxxx\original_files//"

#list of files in folder to rename
files = os.listdir(fileRoot)

#list of files in folder with names
files2 = os.listdir(nameRoot)

for i, file in enumerate(files):
    os.rename(os.path.join(fileRoot, file), os.path.join(fileRoot, ''.join([files2[i]])))
    print(i)
    