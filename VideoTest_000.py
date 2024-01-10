import os

directory_path = "/Users/user/Desktop/CNN/VideoSample/001/"

files = []
files_full_name = []
for root, dirs, files_in_root in os.walk(directory_path):
    for file_name in files_in_root:
        if file_name.endswith(".mp4"):
            parts = file_name.split("_")
            if len(parts) >= 3:
                files.append((parts[0], parts[1], parts[2], parts[3], file_name))
                files_full_name.append(directory_path + file_name)

# print the list of files
for file_info in files:
    print(file_info)

import pandas as pd
df = pd.DataFrame(files, columns=["id", "type1","type2","type3","path"])
#for each folder -> total 9+9 = 18 videos.
#video_types = ['stillx3', 'movingx3', 'half_closedx3'] -> 3x3 (without glasses)
#video_types = ['stillx3', 'movingx3', 'half_closedx3'] -> 3x3 (with glasses)
df.head()


import cv2

# Read videos
cap1 = cv2.VideoCapture(files_full_name[0])
cap2 = cv2.VideoCapture(files_full_name[1])
cap3 = cv2.VideoCapture(files_full_name[2])
cap4 = cv2.VideoCapture(files_full_name[3])

# Grab a frame
#ret, frame = cap1.read()
#frame.shape

Out = "video_out.mp4"

Window = None #1280x720, 1920x1080

#get the fps an the size of the video
fps_c1 = cap1.get(cv2.CAP_PROP_FPS)

h1 = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
w1 = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)

h1 = int(h1)
w1 = int(w1)
dim = (w1, h1)
h1, w1, dim

f4 = cv2.resize(f4, dim, interpolation=cv2.INTER_AREA)

def frameConnect(f1,f2,f3,f4,h1,w1):
    f2 = cv2.resize(f2, dim, interpolation=cv2.INTER_AREA)
    f3 = cv2.resize(f3, dim, interpolation=cv2.INTER_AREA)
    
    BG = cv2.resize(f1, (2*w1, 2*h1), interpolation=cv2.INTER_AREA)
    
    f1 = BG[0:h1, 0:w1]
    f2 = BG[0:h1, w1:2*w1]
    f3 = BG[h1:2*h1, 0:w1]
    f4 = BG[h1:2*h1, w1:2*w1]
    
    return (BG)

if Window == None:
    size = (w1*2, h1*2)
else:
    size = (int(Window.split("x")[0]), int(Window.split("x")[1]))


fps = fps_c1

fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
videowriter = cv2.VideoWriter(Out, fourcc, fps, size)


while (True):
    ret, f1 = cap1.read()
    ret, f2 = cap2.read()
    ret, f3 = cap3.read()
    #ret, f4 = cap4.read()
    if ret == True:
        img = frameConnect(f1,f2,f3,f4,h1,w1)
        img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    else:
        break


cap1.release()
cap2.release()
cap3.release()
cap4.release()
videowriter.release()
cv2.destroyAllWindows()



