# @author: Jeremy Locatelli 
# CST 205 Homework 4
# 10/29/18


from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap
import random
from PIL import Image


app = Flask(__name__)
bootstrap = Bootstrap(app)

# I slammed my head against the for_url method for a good hour and a half, i know this isn't the best way.
def imageDetails(image):
    img = Image.open("static/"+str(image)+".jpg")
    details = """The colormode is {}, image size is {} x {}""".format(img.mode,img.width,img.height)
    return details

@app.route('/')
@app.route('/home')
def main():
    c = list(range(1,9))
    randimgs = random.sample(c,3)
    return render_template('index.html',images=randimgs)

@app.route('/image/<image>')
def image(image):
    #PIL details about image
    deets = imageDetails(image)    
    return render_template("image.html",image=image, details=deets)

if __name__ == '__main__':
    app.run()