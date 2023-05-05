var inFolder = Folder.selectDialog("Please select folder to process");
var outfolder = Folder.selectDialog("Please select folder to Save to");

if (inFolder != null) {
	var fileList = inFolder.getFiles(/\.(jpg|tif|png|psd|)$/i);
	for(var a = 0; a < fileList.length; a++) {
		if (fileList[a] instanceof File) {
			var doc = open(fileList[a]);
			doc.flatten();
			var docname = doc.name.slice(0, -4);
			CropStraighten();
			doc.close(SaveOptions.DONOTSAVECHANGES);
			var count = 1;
			while(app.documents.length) {
				var saveFile = new File(decodeURI(outfolder) + "/" + docname + ".jpg");
				SaveJPEG(saveFile, 12);
				activeDocument.close(SaveOptions.DONOTSAVECHANGES) ;
				count++;
			}
		}
	}
};

function CropStraighten() {
	executeAction( stringIDToTypeID('CropPhotosAuto0001'), undefined, DialogModes.NO );
};

function SaveJPEG(saveFile, jpegQuality) {
	jpgSaveOptions = new JPEGSaveOptions();
	jpgSaveOptions.embedColorProfile = true;
	jpgSaveOptions.formatOptions = FormatOptions.STANDARDBASELINE;
	jpgSaveOptions.matte = MatteType.NONE;
	jpgSaveOptions.quality = jpegQuality;
	activeDocument.saveAs(saveFile, jpgSaveOptions, true,Extension.LOWERCASE);
};

function zeroPad(n, s) {
	n = n.toString();
	while(n.length < s) n = '0' + n;
	return n;
};