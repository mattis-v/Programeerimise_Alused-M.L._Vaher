pixel = "A"
space = " "

def treep(bark,width,height,offset,trees):
    for y in range(height):
        print((space*(height-y-1)+pixel*(2*y+1*width)+space*(offset+height-y-1))*trees)
    for x in range(bark):
        print((space*(height-bark-1)+pixel*(2*bark+1*width)+space*(offset+height-bark-1))*trees)

bark = 1
width = 1
height = 5
offset = 5
trees = 3

treep(bark,width,height,offset,trees)