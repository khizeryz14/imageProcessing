import struct

def copyFiles():
    myImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP.bmp",'rb')
    outImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP-brighter.bmp",'wb+')
    toWrite = myImage.read()
    outImage.write(toWrite)
    

def keepInRange(totalBrightness):
    if totalBrightness >= 255:
        return 255
    elif totalBrightness < 0:
        return 0
    else:
        return totalBrightness
    
copyFiles()
myImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP.bmp",'rb')
outImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP-brighter.bmp",'rb+')
myImage.seek(14)
dataOffset = myImage.read(4)
dataOffsetInt = struct.unpack('i',dataOffset)
w = myImage.read(4)
wInt = struct.unpack('i',w)
h = myImage.read(4)
hInt = struct.unpack('i',h)

#Reading process
myImage.seek(dataOffsetInt[0],0)
outImage.seek(dataOffsetInt[0],0)
brightness = int(input("Enter how much to increase brightness by (0-255): "))

for col in range(hInt[0]):
    for row in range(wInt[0]):
        r=myImage.read(1)
        g=myImage.read(1)
        b=myImage.read(1)
        
        rOut = keepInRange(r[0] + brightness)
        gOut = keepInRange(g[0] + brightness)
        bOut = keepInRange(b[0] + brightness)

        bOut = int.to_bytes(bOut,1,"little")
        gOut = int.to_bytes(gOut,1,"little")
        rOut = int.to_bytes(rOut,1,"little")

        outImage.write(rOut)
        outImage.write(gOut)
        outImage.write(bOut)

myImage.close()
outImage.close()