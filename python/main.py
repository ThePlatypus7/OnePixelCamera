#from time import sleep
from PIL import Image
import serial
import numpy as np

s = serial.Serial('COM6', 9600)

testImg = Image.open("test.bmp")

print(testImg.format, testImg.size, testImg.mode)

r, g, b = testImg.split()
testImg = np.asarray(r, dtype=np.uint8)

#im.show()

width = testImg.shape[0]
height = testImg.shape[1]

width = 100
height = 100

img=np.zeros([width,height])

i = 10000

values = [0] * 250000

while i > 0:
    if s.in_waiting > 0:
        res = s.readline()
        print(i)
        i -= 1
        values[i] = res.decode("Ascii")



for x in range(width):
    for y in range(height):
        img[x,y] = values[x * 100 + y]/2.0
        
img = Image.fromarray(img.astype(np.uint8))
img.show()