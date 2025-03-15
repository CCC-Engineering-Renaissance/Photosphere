import cv2
import numpy as np
import glob
#Work in progress
uncroppedPath = glob.glob("./stitchedOutput.png")
print(uncroppedPath)
uncroppedPan = cv2.imread(uncroppedPath[0]) #only one image
height, width = uncroppedPan.shape[:2]
# Intrinsic camera matrix (assuming a full 360 panorama)
focal_length = width  # or any value depending on your needs
K = np.array([[focal_length, 0, width / 2],
              [0, focal_length, height / 2],
              [0, 0, 1]], dtype=np.float32)

# Rotation matrix (identity matrix for a single image)
R = np.eye(3, dtype=np.float32)

radius = 500
sphereWarper = cv2.detail.SphericalWarper(scale=1000)
warpedImage = sphereWarper.warp(uncroppedPan[0], K, R, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
cv2.imshow("sphere image", warpedImage)

cv2.waitKey(0)
cv2.destoryAllWindows()
