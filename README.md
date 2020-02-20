# pyMultipleImgAnnot
Multiple images binary annotator. 

Annotation binary tool for quicly annotate good/bad images. Tested in Ubuntu, Windows and MacOS.
Suppose you have the following folder structure:


	2019-30-12 

		12
		
			02-00-02-693_rgb.png
			
			...
			
		13
			09-21-03-274_rgb.png
			
			...
			
		14

One subfolder per row is loaded, with images resized and square-cropped to 80x80 pixel. Only subfolders satisfying the requirements are loaded (see parameters
for details). Subfolders images are loaded in batches (parameter n).

![screenshot](https://i.ibb.co/b2mjZgw/Annotazione-2020-02-20-123702.png)

You want to select only good (it's up yo you define "good", in this case is the cat) images from subfolders (12, 13, 14 ..). In my case main folder is a date, 
subfolders are unique IDs. In each subfolder there are many images with timestamp as name. In this way you can filter images by timestamp.
In the first column the subfolder name is loaded in the textbox. You can change it (for example if you want join different subfolders). Using the checkbox
you can flag that subfolder.
By default every image is selected (not greyed):
* Left click: deselect (greyed out)
* Right click: deselect the entire row
* Central click: open the image with the OS image viewer.

# Result File
Clicking on the button "confirm" produce a csv file with the following structure:
original_subfolderID;current_subfolderID;flag;imgX.png;imgY.png;...

Only folders with at least one selected image are present in the result file. First row of the csv must be discarded, is used to temporary mark
the last processed folder, to resume from there.


# Requirements:
Python 3, with the following packages (you can install them using pip):

* pillow


# Usage

```bash
python3 main.py [-h] -i IMAGES_FOLDER [-n MAX_FOLDERS] [-r RESULT_FILE] [-k NUMBER_FILTER] [-t TIME_FILTER]

```

arguments:
```
  -h, --help           show this help message and exit

  -i, IMAGES_FOLDER    path to the first level image folder (Required)
  
  -n, MAX_FOLDERS      number of second level folder to load, default 200. Keep this number not too high, or you will go out of memory.
  
  -r, RESULT_FILE      result csv file, default "result_{IMAGES_FOLDER}.csv"
  
  -k, NUMBER_FILTER    Minimum number of files for a second level folder to be loaded, default 0
  
  -t, TIME_FILTER      Starting hour, only second level folders whose images name start from t as hour will be loaded, default 0

```

