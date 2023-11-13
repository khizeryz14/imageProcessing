import struct

def copyFiles():
    myImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP.bmp",'rb')
    outImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP-grey.bmp",'wb+')
    toWrite = myImage.read()
    outImage.write(toWrite)
    
    
copyFiles()
myImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP.bmp",'rb')
outImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP-grey.bmp",'rb+')
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

for col in range(hInt[0]):
    for row in range(wInt[0]):
        r=myImage.read(1)
        g=myImage.read(1)
        b=myImage.read(1)
        
        greyValue = (r[0] + g[0] + b[0])//3

        greyPixel = int.to_bytes(greyValue,1,"little")

        outImage.write(greyPixel) #r
        outImage.write(greyPixel) #g
        outImage.write(greyPixel) #b

myImage.close()
outImage.close()