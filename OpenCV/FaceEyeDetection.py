import cv2 as cv

image = cv.imread("C:/Users/Yayoi/Documents/Flask/OpenCV/ff.jpg")

casc_class = "C:/Users/Yayoi/Documents/Flask/OpenCV/haarcascade_face.xml"
face_cascade = cv.CascadeClassifier(casc_class)

eye_class = "C:/Users/Yayoi/Documents/Flask/OpenCV/haarcascade_eye.xml"
eye_cascade = cv.CascadeClassifier(eye_class)

smile_class = "C:/Users/Yayoi/Documents/Flask/OpenCV/haarcascade_smile.xml"
smile_cascade = cv.CascadeClassifier(smile_class)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30,30),
    flags = cv.CASCADE_SCALE_IMAGE
)
for (x,y,w,h) in faces:
    cv.rectangle(image, (x,y), (x+w, y+h),(255,255,255),2)

    eyes = eye_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 2,
        flags = cv.CASCADE_SCALE_IMAGE
    )
   
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(image, (ex,ey), (ex+ew, ey+eh),(255,0,0),1)

print("Found ", len(eyes), " eyes")
cv.imshow("Faces and Eyes: ", image)
cv.waitKey(0)