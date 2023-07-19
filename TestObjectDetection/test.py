import cv2
import urllib.request
import numpy as np
import mysql.connector
import concurrent.futures
import keyboard
from datetime import datetime
from win32com.client import Dispatch

mydb = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password = 'root',
    port = '3306',
    database = 'object_detection'
)
mycursor = mydb.cursor()
mycursor.execute('select * from object_detected')
dataFeteched = mycursor.fetchall()

#for data in dataFeteched:
    #print(data)
def speak(str):
    spk = Dispatch('SAPI.spvoice')
    spk.speak(str)



url='http://192.168.116.170/640x480.jpg'
im=None


def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)

        cv2.imshow('live transmission', im)
        cv2.waitKey(5)
        if keyboard.is_pressed("q"):
            break


    cv2.destroyAllWindows()


classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = [line.rstrip() for line in f]

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weigthsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weigthsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127, 5, 127.5))
net.setInputSwapRB(True)
objectInfo=[]
#print(classNames)


def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)

        classIds, confs, bbox = net.detect(im, confThreshold=0.70)
        #print(classIds)

        if len(classIds) != 0:
              for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                        className = classNames[classId-1]
                        cv2.rectangle(im, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(im, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 255, 0), 2)
                        cv2.putText(im, str(confidence), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 255, 0), 2)

                        print(className)

                        query = f"INSERT INTO `object_detection`.`object_detected` (`object_name`, `time`) VALUES ( '{className}', '{datetime.now()}');"
                        #print(query)
                        mycursor.execute(query)
                        mydb.commit()
              speak(className)
              objectInfo.append(className)



        cv2.imshow("detection", im)
        cv2.waitKey(1000)


        if keyboard.is_pressed("q"):
            break


    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
            f1= executer.submit(run1)
            f2= executer.submit(run2)