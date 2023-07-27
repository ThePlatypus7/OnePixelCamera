from PIL import Image
import numpy as np
import random
import gui as g
import serial

portNumber = 'COM6'
arduinoConnected = False
arduPort = -1
showImageInWindowsImageView = False

gui = g.Ui()

#loading test image
testImg = Image.open("test.bmp")
#splitting color channels
r, g, b = testImg.split()
#converting to numpy array
testImg = np.asarray(r, dtype=np.uint8)

#get width and height from GUI
width, height = gui.startWindow()

#initializing new image array
img=np.zeros([height,width])

i = width * height
rValues = [0] * i
gValues = [0] * i
bValues = [0] * i

#try serial connection
if arduinoConnected:
    try:
        arduPort = serial.Serial(portNumber, 9600)
    except:
        pass
        
    if arduPort == -1:
        arduinoConnected = False
        print("Arduino not connected or wrong Port")

if arduinoConnected:
    #send image size to arduino
    arduPort.write(width)
    arduPort.write("\n")
    arduPort.write(height)
    #collecting live data from arduino
    while i > 0:
        if arduPort.in_waiting > 0:
            res = arduPort.readline()
            print(i)
            i -= 1
            rValues[i] = res.decode("Ascii")
else:
    #generating random Values
    for k in range(len(rValues)):
        rValues[int(k)] = random.randint(0,1024)
        gValues[int(k)] = random.randint(0,1024)
        bValues[int(k)] = random.randint(0,1024)

#gui.recordWindow()

minimum = min(rValues)
maximum = max(rValues)

for k in range(len(rValues)):
    rValues[int(k)] = int((rValues[int(k)] - minimum) * (255 - 0) / (maximum - minimum) + 0)

minimum = min(gValues)
maximum = max(gValues)

for k in range(len(gValues)):
    gValues[int(k)] = int((gValues[int(k)] - minimum) * (255 - 0) / (maximum - minimum) + 0)

minimum = min(bValues)
maximum = max(bValues)

for k in range(len(bValues)):
    bValues[int(k)] = int((bValues[int(k)] - minimum) * (255 - 0) / (maximum - minimum) + 0)    

gui.showImage(width, height, rValues, gValues, bValues)


if showImageInWindowsImageView:
    for x in range(width):
        for y in range(height):
            img[y,x] = rValues[y * width + x]
        
    img = Image.fromarray(img.astype(np.uint8))
    img.show()