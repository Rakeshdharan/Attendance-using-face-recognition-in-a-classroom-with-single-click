import sys
sys.path.append('~/.local/lib/python3.5/site-packages')
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm



DATADIR = '/home/rak/attendance_facial/datasets'
CATEGORY=[]
for L in os.listdir(DATADIR): 
    CATEGORY.append(L)
print(CATEGORY)


training_data = []
IMG_SIZE=[96,96]

def create_training_data():
    for category in CATEGORY:  

        path = os.path.join(DATADIR,category)  
        class_num = CATEGORY.index(category) 
        
        for img in tqdm(os.listdir(path)):
           
            try:
                img_array = cv2.imread(os.path.join(path,img) ) 
                img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
                new_array = cv2.resize(img_array, (IMG_SIZE[0], IMG_SIZE[1])) 
                training_data.append([new_array,class_num+1]) 
            except OSError as e:
                print("OSErrroBad img most likely", e, os.path.join(path,img))
            except Exception as e:
                print("general exception", e, os.path.join(path,img))

create_training_data()
print(len(training_data))

import random
random.shuffle(training_data)


faces=[]
Ids=[]

for features,label in training_data:
    faces.append(features)
    Ids.append(label)



print(Ids)

recognizer = cv2.face.LBPHFaceRecognizer_create()  
recognizer.train(faces, np.array(Ids))                                       
recognizer.write('/home/rak/attendance_facial/trainingData.yml')
print('Model trained and saved successfully...')