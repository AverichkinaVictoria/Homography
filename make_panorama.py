import cv2
import os

mainFolder = 'Images'
myFolders = os.listdir(mainFolder)

for folder in myFolders:
    path = mainFolder + '/' + folder
    images = []
    mylist = os.listdir(path)
    for imgs in mylist:
        curImg = cv2.imread(f'{path}/{imgs}')
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    status, result = stitcher.stitch(images)
    cv2.imshow(folder, result)
    cv2.waitKey(0)


