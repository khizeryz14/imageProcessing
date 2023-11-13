import struct

def copyFiles():
    myImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP.bmp",'rb')
    outImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP-contrast.bmp",'wb+')
    toWrite = myImage.read()
    outImage.write(toWrite)
    

def keepInRange(totalContrast):
    if totalContrast >= 255:
        return 255
    elif totalContrast < 0:
        return 0
    else:
        return int(totalContrast)
    
copyFiles()
myImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP.bmp",'rb')
outImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP-contrast.bmp",'rb+')
myImage.seek(10)
dataOffset = myImage.read(4)
dataOffsetInt = struct.unpack('i',dataOffset)
myImage.seek(4,1)
w = myImage.read(4)
wInt = struct.unpack('i',w)
h = myImage.read(4)
hInt = struct.unpack('i',h)

#Reading process
myImage.seek(dataOffsetInt[0],0)
outImage.seek(dataOffsetInt[0],0)
contrast = float(input("Enter contrast factor: "))

for col in range(hInt[0]):
    for row in range(wInt[0]):
        r=myImage.read(1)
        g=myImage.read(1)
        b=myImage.read(1)
        
        rOut = keepInRange(((r[0]-128)*contrast)+128)
        gOut = keepInRange(((g[0]-128)*contrast)+128)
        bOut = keepInRange(((b[0]-128)*contrast)+128)

        bOut = int.to_bytes(bOut,1,"little")
        gOut = int.to_bytes(gOut,1,"little")
        rOut = int.to_bytes(rOut,1,"little")

        outImage.write(rOut)
        outImage.write(gOut)
        outImage.write(bOut)

myImage.close()
outImage.close()