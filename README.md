# Face Morphing Print-Scan Research

This is the process that is followed to develop high quality printed and scanned photos using scripts found in the Code folder  

## Presentations
https://pages.nist.gov/ifpc/2022/presentations/29_NIST-IFPC_CITeR_Morph_Presentation_Nov_17_2022.pdf

## Equipment

Scanner  
[Epson Perfection V850 Pro](https://epson.com/For-Work/Scanners/Photo-and-Graphics/Epson-Perfection-V850-Pro-Photo-Scanner/p/B11B224201)  

Printer  
[Canon Pixma Pro 100](https://www.usa.canon.com/support/p/pixma-pro-100)  

## Software
[Adobe Photoshop](https://helpx.adobe.com/photoshop/get-started.html)  
[Visual Studio Code](https://code.visualstudio.com/download)  
[PyCharm IDE](https://www.jetbrains.com/help/pycharm/installation-guide.html) (optional)  
[Scanner Driver and EPSON Scan Utility](https://epson.com/Support/Scanners/Perfection-Series/Epson-Perfection-V850-Pro/s/SPT_B11B224201)  
[Canon Pixma Pro 100 Driver](https://www.usa.canon.com/support/p/pixma-pro-100)  


## Requirements
See [Requirements.txt](https://github.com/rneddojr/Face-Morphing-Research/blob/695b36eadd654adc9eb9cf6734fb0f6177676ea8/Requirements.txt) for all python libraries used  
For JavaScript Code run in debugging and have ExtendScript and ExtendScript Debugger on Visual Studio Code  

## Running Scripts and Processing  

###Preprocessing Stage - Set up pictures for printing  

1. Resize digital morphs to 600 by 600 pixels using [cropResize.py]()  
Edit Line 4 to the set of images that need to be printed  
```
fileRoot = r"C:\Users\xxxx\imgs_to_resize//"
```

2. Arrange images on page for printing - [Create Print Pages.py]()
Edit Line 9 to the set of images that need to be printed  
Edit Line 10 to the location you want the Print Pages to be stored  
Edit Line 11 to fit the dataset that you are printing and image type: Bonafide or Morph  
```
imgRoot = r"C://Users//xxxx//Dataset//imgs//"
printPageRoot = r"C://Users//xxxx//Dataset_Print_Pages//"
pageName = "Dataset_Morph_Print_Page_" or pageName = "Dataset_Bonafide_Print_Page_"
```

Edit Line 54 to fit the dataset. This is for the physical page numbering system
```
# Default Line
draw.text((2200, 3200), pageCounterStringTwo + " Data PS", (0, 0, 0), font=font)
# Use for Morphed Images
draw.text((2200, 3200), pageCounterStringTwo + " Data MPS", (0, 0, 0), font=font)
# Use for Bonafide Images
draw.text((2200, 3200), pageCounterStringTwo + " Data BPS", (0, 0, 0), font=font)
```

### Prep for Printing Stage
3. Launch Adobe Photoshop  
3i. Navigate to print under File then Print with any file opened  
3ii. Set settings to image seen [here](https://github.com/rneddojr/Face-Morphing-Research/blob/00568c74c8d94f527ac85f823047209291cebe7e/Assisting%20Images/Photoshop%20Settings/Photoshop%20Print%20Settings.png)  
You will have to modify the ICC to match the specific type of paper that is being used to print  
For help see [here]() 
Default for printing should be:
```
Canon Pro-100 <GL><PP> 1/2 Photo Paper Plus Glossy&Gold  
```
Unless other types of paper are being used then adjust the ICC profile accordingly to match.

### Begin Printing
4. Launch Visual Studio Code and open print.js  
4i. Run print.js with [Run --> Start Debugging)]()  
4ii. {Select Host Application --> Adobe Photoshop]()  
4iii. Navigate to Adobe Photoshop and select folder containing pages for printing and press select folder  

## Scanning Stage

### Prepare Scanner
5. Launch EPSON Scan  
5i. Load [professional mode]()  
5ii Set [adjustments to off (unchecked)]()  
5iii. Set ICM in configuration tab to sRGB  
Go to file configuration and assure:  
Image type: jpg or jpeg  
Image compression: 1, highest quality  
Folder location: respective dataset ex. Dataset_Bonafide_Page_PS_ or Dataset_Morph_Page_PS_  
Scan numbering: set to the respective page number that is being scanned  

## Processing Stage

5. Launch python IDE and open batch_process.py  
Edit lines 5 through lines 13  
```
line 5 - line 8 uncomment
arg = 1
scanRoot = r"C:\Users\xxxxx\images_to_process//"
saveRoot1 = r"C:\Users\xxxxx\images_splilt//"
saveRoot2 = r"C:\Users\xxxxx\images_to_crop//"

and comment 
#arg = 2
#scanRoot = r"C:\Users\xxxxx\images_cropped//"
#saveRoot1 = r"C:\Users\xxxxx\images_cleaned//"
#saveRoot2 = saveRoot1
```
Line 5 and 10 determine which set of instructions are performed  
scanRoot is the location of files to be processed  
saveRoot1 is the save location of the files after the first pass  
saveRoot1is the save location of the files after the second pass    

6. Launch Visual Studio Code and open crop.js  
6i. Run crop.js with [Run --> Start Debugging)]()  
6ii. {Select Host Application --> Adobe Photoshop]()  
6iii. Navigate to Adobe Photoshop and select folder containing pages for cropping and press select folder  

Check for mis-cropped images in cropped folder - check with eyes and use sort by dimensions in file explorer  
Isolate mis-cropped images and hand crop images as requireed  

7. Launch python IDE and open batch_process.py  
Edit lines 5 through lines 13  
```
line 5 - line 8 comment
#arg = 1
#scanRoot = r"C:\Users\xxxxx\images_to_process//"
#saveRoot1 = r"C:\Users\xxxxx\images_splilt//"
#saveRoot2 = r"C:\Users\xxxxx\images_to_crop//"

and uncomment 
arg = 2
scanRoot = r"C:\Users\xxxxx\images_cropped//"
saveRoot1 = r"C:\Users\xxxxx\images_cleaned//"
saveRoot2 = saveRoot1
```
scanRoot is the location cropped images from crop.js  
saveRoot is the output of the cleaned images  

8. Launch python IDE and open Batch Rename.py   
Edit lines 3 and 4
```
fileRoot = r"C:\Users\xxxx\files_to_rename//"
nameRoot = r"C:\Users\xxxx\original_files//"
```
nameRoot is the original files and are ufor naming are from the original source images  
Copy and rename the cleaned folder from the previous step to dataset_Renamed  

9. Launch python IDE and open cropResize.py  
Edit line 4
```
fileRoot = r"C:\Users\xxxx\imgs_to_resize//"
```
Copy and rename the renamed folder from the previous step to dataset_Resized  
