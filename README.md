# Face-Morphing-Research

## Presentations
https://pages.nist.gov/ifpc/2022/presentations/29_NIST-IFPC_CITeR_Morph_Presentation_Nov_17_2022.pdf

## Equipment

Scanner

Printer

## Software
https://helpx.adobe.com/photoshop/get-started.html
https://code.visualstudio.com/download
https://www.jetbrains.com/help/pycharm/installation-guide.html optional
https://epson.com/Support/Scanners/Perfection-Series/Epson-Perfection-V850-Pro/s/SPT_B11B224201
Scanner Driver and EPSON Scan Utility

## Requirements
See here for all python libraries used
For JavaScript Code run in debugging and have ExtendScript and ExtendScript Debugger on Visual Studio Code

## Running Scripts and Processing
###Preprocessing Stage - Set up pictures for printing

Resize images to 600 by 600 pixels - cropResize.py
Arrange images on page for printing - Create Print Pages.py
Rename pageName variable to particular dataset line ~65
Change numbering of page to particular dataset and image type line ~107
For morph “ dataset MPS”
For source “ dataset SPS”

###Printing Stage
Prerequisites
Download Visual Studia Code
and have 
Send images to printer - print.js
Must have adobe photoshop open and downloaded

## Scanning Stage
Launch Scanner Software 
Load professional mode
Set adjustments to off, unchecked
Check configuration tab to ICM with sRGB
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
