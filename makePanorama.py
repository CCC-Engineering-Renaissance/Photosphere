import numpy as np
import cv2 
import glob

#Goes into local folder and searches for all files that end in jpg
imagePathsList = glob.glob("./*.jpg")
for path in imagePathsList:
	print(path)
imageList = []

#Reads/appends each image into imageList
for image in imagePathsList:
	imgTemp = cv2.imread(image)
	if imgTemp is not None:	
		imageList.append(imgTemp)
		height, width = imgTemp.shape[:2]
	
		cv2.imshow('Image', imgTemp)
		
		cv2.waitKey(0) #waits for keypress
		cv2.destroyAllWindows()
	else:
		print("Image not loaded successfully.\n")



#image stithcer
image_stchr = cv2.Stitcher_create()

error, stitchedImg = image_stchr.stitch(imageList)

#Writes image to local folder and shows it to the screen
if not error:
	print("Done! Here's your image!")
	cv2.imwrite("stitchedOutput.png", stitchedImg)
	cv2.imshow("Stitched Image", stitchedImg)
	height, width = stitchedImg.shape[:2]
	print(str(height)  + " " + str(width))
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	print("Error")


print("Done with program")
