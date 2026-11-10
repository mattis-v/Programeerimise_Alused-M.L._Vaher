pixel = "O"
space = " "

def treep(height,offset):
    for y in range(height):
        print((space*(height-y-1)+pixel*(2*y+1))+(space*(offset)+pixel*(2*(height-y)-1)+space*(-height+y+1)))
        
        
height = 18
offset = 17

treep(height,offset)