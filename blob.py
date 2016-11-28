import cv2

__blobSettings__ = cv2.SimpleBlobDetector_Params()

# Change thresholds
__blobSettings__.minThreshold = 0;
__blobSettings__.maxThreshold = 255;

# Filter by Area.
__blobSettings__.filterByArea = True
__blobSettings__.minArea = 20*20*3.14

# Filter by Circularity
__blobSettings__.filterByCircularity = True
__blobSettings__.minCircularity = 0.5

# Filter by Convexity
__blobSettings__.filterByConvexity = False
__blobSettings__.minConvexity = 0.87

# Filter by Inertia
__blobSettings__.filterByInertia = False
__blobSettings__.minInertiaRatio = 0.01

