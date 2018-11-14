from bs4 import BeautifulSoup
import requests
import shutil
from PIL import Image
import time

start = time.time()
# Ironic right?
URL = "http://konachan.net/post/"
page = requests.get(URL) 
pageHTML = page.text
soup = BeautifulSoup(pageHTML,'html.parser')
# print(soup.prettify())

images = []
for img in soup.find_all('img'):
    images.append(img.get('src'))

imgstr = images[-1]

image = requests.get(URL + imgstr, stream=True)
with open("img.jpg","wb") as output:
    shutil.copyfileobj(image.raw,output)
del image
# I only know how to open an image with PIL lol

scrapedimage = Image.open("img.jpg")
scrapedimage.show()
end = time.time()
total = str(end - start)
print("Program completed in " + total + " seconds")