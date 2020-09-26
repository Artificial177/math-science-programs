import os, glob
import numpy as np
import cv2

'''
A program that detects faces from a continuous video feed. 
'''

CENTER_X = 100
CENTER_Y = 80
CENTER_POS = (CENTER_X, CENTER_Y)

# Deletes all images from a prior test run.
list = glob.glob('ztest*.jpg') # Replace with a different directory path.
for path in list:
   try:
      os.remove(path)
   except:
      print("Error while deleting: ", path)

vr = cv2.VideoCapture(0) #(VR = Video Recognizer)

cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Insert Directory Path
cascade_eye = cv2.CascadeClassifier('haarcascade_eye.xml') # Replace

def showPositionedWindow(window_name, img_name, coords):
   cv2.namedWindow(window_name)
   cv2.moveWindow(window_name, coords[0], coords[1])
   cv2.imshow(window_name, img_name)

i = 0
while True:
   ret, frame = vr.read()
   gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   faces = cascade_face.detectMultiScale(gray_frame, scaleFactor = 1.2, minNeighbors = 5)

   for (x, y, w, h) in faces:
      if i % 5 == 0 and i != 0:
         print(str(i) + ": " + str(faces))
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
      gray_reg = gray_frame[y:y+h, x:x+w]
      color_reg = frame[y:y+h, x:x+w]
      eyes = cascade_eye.detectMultiScale(gray_reg, scaleFactor = 1.2)
      # Uncomment below if you want to try to detect eyes, but it doesn't work quite well yet. 
      for (x1, y1, w1, h1) in eyes:
         #cv2.rectangle(color_reg, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
         pass

   showPositionedWindow('frame', frame, CENTER_POS)
   if i % 5 == 0 and i != 0:
      # Saves certain frames from each run to a folder. 
      cv2.imwrite('Face Detect Images/ztest' + str(i) + '.jpg', frame)
   if cv2.waitKey(1) & 0xFF == ord('z'):
     break

   i += 1
vr.release()
cv2.destroyAllWindows()
