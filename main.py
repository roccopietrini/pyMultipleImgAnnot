import tkinter as tk
import os
import argparse
from _datetime import datetime
from MainWindow import MainWindow

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="Path to the images")
ap.add_argument("-r", "--result", required=False, help="Path to result file")
ap.add_argument("-n", "--number", required=False, default=200, help="Number of folders")
ap.add_argument("-k", "--min", required=False, default=0, help="Number of minimum images for ID")
ap.add_argument("-t", "--time", required=False, default=0, help="Start time")


args = vars(ap.parse_args())

image_path = args["images"]
if args["result"] is not None:
    result = args["result"]
else:
    result = 'result_' + os.path.basename(image_path) + '.csv'
n = int(args["number"])
min_images = int(args["min"])
start_time = int(args["time"])


last_id = -1
if os.path.exists(result):
    with open(result, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[0]
        last_id = int(last_line)

images_folders = [k for k in sorted(os.listdir(os.path.join(os.path.dirname(__file__), image_path)), key=int)
                  if len(os.listdir(os.path.join(os.path.dirname(__file__), image_path, k)))/2 >= min_images and
                  int(sorted(os.listdir(os.path.join(os.path.dirname(__file__), image_path, k)),
                             key=lambda s: datetime.strptime(s[:12], '%H-%M-%S-%f'))[0].split('-')[0]) >= start_time
                  and int(k) > last_id]

images_folders = images_folders[:min(n, len(images_folders))]

if not images_folders:
    print("Nothing to do")
else:
    root = tk.Tk()
    root.title("pyMultipleImgAnnot")
    MainWindow(root, result, image_path, images_folders, n)
    root.mainloop()
