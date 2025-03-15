import numpy as np
import cv2 
import glob
import imutils

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


print("Done with making the panorama(unedited)")

print("Second part of the program") 
if not error:
	
	stitchedImg = cv2.copyMakeBorder(stitchedImg, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0,0,0)) 
	#makes black border around image

	gray = cv2.cvtColor(stitchedImg, cv2.COLOR_BGR2GRAY)
	threshImage = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
	#makes grayscale, and makes each pixel black or white(0 or 1)

	cv2.imshow("O/I image", threshImage)
	cv2.waitKey(0)

	contours = cv2.findContours(threshImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	contours = imutils.grab_contours(contours)
	areaOI = max(contours, key=cv2.contourArea)
	#finds the round corners of the unedited image and the max area(rectangle?) of the contour

	mask = np.zeros(threshImage.shape, dtype="uint8")

	x, y, w, h = cv2.boundingRect(areaOI) 
	#coords and width and height
	cv2.rectangle(mask, (x,y), (x+w, y + h), 255, -1)
	#makes rectangle around our area of intersest(the photo)

	minRectangle = mask.copy()
	subtrac = mask.copy()

	#subracting minRect with the thresh image until we get the area we want
	while cv2.countNonZero(subtrac) > 0:
		minRectangle = cv2.erode(minRectangle, None)
		subtrac = cv2.subract(minRectangle, threshImage)

	contours = cv2.findCountours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#does it again
	areaOI = max(contours, key=cv2.contourArea)

	cv2.imshow("minRectangle Image", minRectangle)
	cv2.waitket(0)

	x, y, w, h = cv2.boundingRect(areaOI)

	stitchedImg = stitchedImg[y:y + h, x:x + w]

	cv2.imwrite("stitchedOutputProcessed.png", stitchedImg)

	cv2.imshow("Stiched Image Processed", stitchedImg)
	cv2.waitKey(0)

else:
	print("Images could not be stitched!")
	print("Probably not enough keypoints being detected!")


