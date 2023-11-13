import struct

def copyFiles():
    myImage = open("C:\\Users\\khize\\Downloads\\bmp image.bmp",'rb')
    outImage = open("C:\\Users\\khize\\Downloads\\grey-bmp.bmp",'wb+')
    toWrite = myImage.read()
    outImage.write(toWrite)
    
    
copyFiles()
myImage = open("C:\\Users\\khize\\Downloads\\bmp image.bmp",'rb')
outImage = open("C:\\Users\\khize\\Downloads\\grey-bmp.bmp",'rb+')
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

for col in range(hInt[0]):
    for row in range(wInt[0]):
        r=myImage.read(1)
        b=myImage.read(1)
        g=myImage.read(1)
        
        greyValue = (r[0] + b[0] + g[0])//3

        greyPixel = int.to_bytes(greyValue,1,"little")

        outImage.write(greyPixel)
        outImage.write(greyPixel)
        outImage.write(greyPixel)

myImage.close()
outImage.close()