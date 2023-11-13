import struct
import turtle
pixels=0
myImage = open("C:\\Users\\khize\\Downloads\\bmp image.bmp",'rb')
myImage.seek(14)
dataOffset = myImage.read(4)
dataOffsetInt = struct.unpack('i',dataOffset)
print("Offset:",dataOffsetInt[0])
w = myImage.read(4)
wInt = struct.unpack('i',w)
print("Image width:",wInt[0])
h = myImage.read(4)
hInt = struct.unpack('i',h)
print("Image height:",hInt[0])

#Turtle setup
tr = turtle.Turtle() #My turtle object
scr = turtle.Screen() #My screen object
turtle.tracer(0,0)
scr.setup(hInt[0],wInt[0])
scr.colormode(255)
tr.setpos(0,0)

#Reading process
myImage.seek(dataOffsetInt[0],0)

for col in range(hInt[0]):
    for row in range(wInt[0]):
        r=myImage.read(1)
        g=myImage.read(1)
        b=myImage.read(1)
        tr.dot(1)
        tr.color(r[0],g[0],b[0])
        tr.goto(row,col)
        pixels += 1

print("Total pixels drawn:",pixels)
turtle.update()
turtle.done()
myImage.close()