import cv2
image = cv2.imread(r"/Users/jacksondouglass/Documents/Code/ImageStitching/curtian.jpg")
#print(image)


height, width = image.shape[:2]


cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
