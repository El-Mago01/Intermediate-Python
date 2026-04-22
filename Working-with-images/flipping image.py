from image import *

# ACCESS AN IMAGE FROM A FILE
img = Image("gal2.jpg")

# LOOP THROUGH THE PIXELS
halfWidth=img.getWidth()//2
halfHeight=img.getHeight()//2
print(f"The image size is {img.getWidth()} x {img.getHeight()}")

Horizontal_line=halfHeight
print(f"The horizontal flip line is at {Horizontal_line}")
for x in range(img.getWidth()):
    for y in range(img.getHeight()):
        #Shrink the image
        if y%2 == 0: #skip uneven lines
            p.getRed(x,y)
            p.getRed(x,y)
            p.getRed(x,y)
            p.setRed(100)
            p.setGreen(100)
            p.setBlue(100)
           # if y < Horizontal_line:
                #The normal image comes next
                #print(f"Y-{y} Above HL-{Horizontal_line}")
           #     p = img.getPixel(x, y)
            #else:
                #The flipped image comes next
                #print(f"Y-{y} Below HL-{Horizontal_line}, getting image from {y-2*y+2*Horizontal_line}")
              #  p = img.getPixel(x, y-2*y+2*Horizontal_line)
            # SET THE PIXEL IN THE IMAGE
            img.setPixel(x,y//2,p)
        else:        # The line is uneven
            p.getPixel(x,y)
            #print(f"{x} - {y}")
            img.setPixel(x,(y//2+1)+1,p)
    #print(p)
# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)