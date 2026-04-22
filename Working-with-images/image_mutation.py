from PIL import Image

TUNING=(100,100,100) #setting the pixel tuning in %. 100% means no change for R G B

# CREATE AN IMAGE FROM A FILE
im = Image.open("beach.jpg")
pixelMap= im.load()
# LOOP THROUGH ALL THE PIXELS
img=Image.new(im.mode, im.size)
pixelsNew=img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixel=(pixelMap[x,y])
        newPixel=[0,0,0]
        for color in range(3):
            if pixel[color] * (TUNING[color])/100 > 255:
                newPixel[color]=255
            else:
                newPixel[color]=int(pixel[color] * (TUNING[color]/100))
        pixelsNew[x,y]=(newPixel[0], newPixel[1], newPixel[2])
im.close()
img.show()
img.save("out.tif")
img.close()
# SHOW THE CHANGED IMAGE
#win = ImageWin(img.getWidth(),img.getHeight())
#img.draw(win)
