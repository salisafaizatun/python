import matplotlib, cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

%matplotlib inline
img = cv2.imread('fotodata.png')
im = mpimg.imread('fotodata.png')

#convert image to RGB color for matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#show image with matplotlib
plt.imshow(img)

#import image to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)

#gray image represented as a2-d array
print(gray_img)
