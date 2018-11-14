from bs4 import BeautifulSoup
import cv2 as cv
from io import BytesIO
import requests
from PIL import Image
from matplotlib import pyplot as plt

# Do not judge me
URL = "http://konachan.net/post/show/144301/blue_eyes-blue_hair-blush-bow-chibi-cirno-fairy-re"
page = requests.get(URL)
HTML = page.text
soup = BeautifulSoup(HTML,'lxml')
# Find the image source file , this isn't the full size image
for img in soup.find_all("img",id="image",class_="image"):
    imageURL = img['src']

r = requests.get(imageURL)
img = Image.open(BytesIO(r.content))
img.save("image.jpg")

# OpenCV opens images in B G R color format so we have to convert colors so it displays on our plot correctly
imgBGR = cv.imread("image.jpg")
imgRGB = cv.cvtColor(imgBGR,cv.COLOR_BGR2RGB)

# not sure on the values yet,but these work well for this image
# https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
edges = cv.Canny(imgRGB,100,200)
edgePil = Image.fromarray(edges)
edgePil.save("imageEDGES.jpg")

plt.subplot(121),plt.imshow(imgRGB,cmap = 'gray')
# Don't show any axis or tickmarks
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()





