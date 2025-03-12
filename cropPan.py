import cv2
import numpy as np
import imutils 
import glob

uncroppedPath = glob.glob("./stitchedOutput.png")
print(uncroppedPath)
uncroppedPan = cv2.imread(uncroppedPath[0]) #only one image

cv2.imshow("Uncropped Panorama", uncroppedPan)
cv2.waitKey(0)
cv2.destroyAllWindows()

testImage = uncroppedPan
height, width = testImage.shape[:2]
print(f"Origional height: {height}\nOrigional Width: {width}\n")
testImage = imutils.resize(testImage, width=width - 2250)
cv2.imshow("tested stretched image", testImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Unfinished


