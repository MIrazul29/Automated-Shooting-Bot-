from pyfirmata import Arduino, util,SERVO
from time import sleep

import cv2

board = Arduino('COM3')
pin=10
board.digital[pin].mode=SERVO



face_f = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_f.detectMultiScale(gray, 1.1, 4)

    if type(face) == tuple:
        #this will make the servo arm in 90 degree position
        board.digital[pin].write(90)
        sleep(.015)

        print('Not Human') # will print human or not
    else:
        # this will make the servo arm in 0 degree position ,which will trigger the gun
        board.digital[pin].write(0)
        sleep(.015)
        print('HUMAN') # will print human or not

    for (x, y, h, w) in face:
        cv2.rectangle(frame, (x, y), (x + h, y + w), (255, 0, 0), 2)

    cv2.imshow("d", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()