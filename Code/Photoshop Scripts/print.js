main();

function main(){
    var imgpath = Folder.selectDialog("Please select input folder");
    const fileList = imgpath.getFiles();
    var len = fileList.length;
    var sortedList = new Array(len);
    const numArray = new Array(len);
    sortedList, numArray = sort_array(fileList, sortedList, numArray);
    fileList = sortedList;
    var start = Math.min.apply(Math, numArray)
    var end = Math.max.apply(Math, numArray)
    for(i = start; i<end; i++) {
        var toPrintImg = new File (fileList[i]);
        var doc = open(toPrintImg);
        activeDocument.resizeImage (2550, 3300, 300, ResampleMethod.BICUBIC);
        $.sleep(1000);
        printIt();
        $.sleep(2500);
        app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
    }
}

function printIt() { 
    //app.activeDocument.printPreferences.profile("Canon Pro-100 <GL><PP> 1/2 Photo Paper Plus Glossy&Gold");
    app.activeDocument.printSettings.flip = false;
    app.activeDocument.printSettings.negative = false;
    app.activeDocument.printOneCopy();
}

function sort_array(fileList, sortedList, numArray) {
    const nums = new Array(fileList.length)
    for(i=0; i<fileList.length; i++) {
        var ammended_file = "";
        var file = fileList[i];
        splitstring = file.toString().split("_");
        var num_w_ex = splitstring.pop();
        var num_split = num_w_ex.split(".");
        var num = Number(num_split[0]);
        nums[i] = num;
        for(j=0; j<splitstring.length; j++) {
            if (j == 0)
                ammended_file = splitstring[j] + "_";
            else
                ammended_file = ammended_file + splitstring[j] + "_";
        }
        sortedList[num] = ammended_file + num_split[0] + "." + num_split[1];
    }
    numArray = nums;
    return sortedList, numArray;
}
