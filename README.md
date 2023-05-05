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

1. Resize digital morphs to 600 by 600 pixels using cropResize.py  
2. Arrange images on page for printing - Create Print Pages.py  
3. Rename pageName variable to particular dataset line ~65  
```

```
4. Change numbering of page to particular dataset and image type line ~107  
```
For Morphed Images
“ dataset MPS”
```

```
For Bonafide Images
“ dataset SPS”
```

###Printing Stage
5. Launch Adobe Photoshop  
5i. Navigate to print under File then Print with any file opened  
5ii. Set settings to image seen [here](https://github.com/rneddojr/Face-Morphing-Research/blob/00568c74c8d94f527ac85f823047209291cebe7e/Assisting%20Images/Photoshop%20Settings/Photoshop%20Print%20Settings.png)  
5iii. Printer profile should match paper being used. For help see [here]() 
Canon Pro-100 <GL><PP> 1/2 Photo Paper Plus Glossy&Gold  
6. Launch Visual Studio Code and open print.js  
7. Send images to printer using print.js  
7i. Start Debugging  
7ii. Select Host Application: Adobe Photoshop  
7iii. Navigate to Adobe Photoshop and select folder containing pages for printing  

## Scanning Stage
8. Launch Scanner Software  
8i. Load professional mode  
8ii Set adjustments to off (unchecked)  
8iii. Set ICM in configuration tab to sRGB  
Go to file configuration and assure:  
Image type: jpg or jpeg  
Image compression: 1, highest quality  
Folder location: respective dataset ex. Dataset_Bonafide_Page_PS_ or Dataset_Morph_Page_PS_  
Scan numbering: set to the respective page number that is being scanned  

## Processing Stage

Separate morphs from page format - Batch Separate Morphs.py  
The folder location is going to be the same one as where the images were saved in the scanning stage  
Save images to a new folder ex. Dataset_Bonafide_Split or Dataset_Morph_Split  
Delete blank images from folder  
Cut numbers and scanner bed from images - Batch Cut Numbers.py  
The folder location is going to be the same one as where the images were saved in the Separate morphs script  
Save images to a new folder ex. FRGC_Source_Cut  

Above Steps are removed since a new script was developed. – batch_process.py  
Use arg = 1 to do both steps above  
scanRoot is the scanned images  
saveRoot is the separated and cut images  

Crop and straighten with photoshop - crop.js  
Make a folder for cropped images to reside ex FRGC_Source_Cropped  
Check for mis-cropped images in cropped folder - check with eyes and use sort by dimensions in file explorer  
Isolate mis-cropped images and hand crop  
Clean up cropped images - Batch Clean.py  
Input folder is the cropped images from the previous step  
Output folder is ex. FRGC_Source_Cleaned  

Above step is removed since a new script was developed. – batch_process.py  
Use arg = 2 to do step above   
scanRoot is the cropped images from crop.js  
saveRoot is the cleaned images, Output folder is ex. FRGC_Source_Cleaned  

Renamed Images - batch rename.py  
Files for naming are from the original source images  
Copy and rename the cleaned folder from the previous step to FRGC_Source_Renamed  
Input folder fileRoot is the FRGC_Source_Renamed that was just made  
Resize Images - batch rename.py  
Copy and rename the renamed folder from the previous step to FRGC_Source_Resized  
Input folder fileRoot is the FRGC_Source_Resized that was just made  
