import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Anirudh.png')
img = img[:,:,1]
histr = cv2.calcHist([img],[0],None,[256],[0,255])

m1=0
m2=0
for x,y in enumerate(histr):
    if m1<y:
        m1=y
    if m2>y:
        m2=y

print(histr)
print(m1)
print(m2)
