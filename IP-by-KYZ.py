import struct
import turtle
pixels=0
myImage = open(r"C:\Khizer Projects (CPP)\Image Processing\myBMP.bmp",'rb')
myImage.seek(10)
dataOffset = myImage.read(4)
dataOffsetInt = struct.unpack('i',dataOffset)
print("Offset:",dataOffsetInt[0])
myImage.seek(4,1)
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
scr.setup(wInt[0],hInt[0])
scr.colormode(255)
tr.hideturtle()
tr.setpos(0,0)

#Reading process
myImage.seek(dataOffsetInt[0],0)

for col in range(hInt[0]):
    for row in range(wInt[0]):
        b=myImage.read(1)
        g=myImage.read(1)
        r=myImage.read(1)
        turtle.penup()
        tr.goto(row, col)
        turtle.pendown()
        tr.dot(3)
        tr.color(r[0],g[0],b[0])
        pixels += 1

print("Total pixels drawn:",pixels)
turtle.update()
turtle.done()
myImage.close()