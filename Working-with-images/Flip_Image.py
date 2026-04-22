from image import *

# CREATE AN IMAGE FROM A FILE
img = Image("gal2.jpg")
img2 = Image.new(RGB, (img.getWidth(), img.getHeight() * 2))

# LOOP THROUGH THE PIXELS
halfWidth = img.getWidth() // 2
halfHeight = img.getHeight() // 2
for x in range(halfWidth, img.getWidth()):
    for y in range(img.getHeight()):
        # GET THE DATA
        p = img.getPixel(x, y)

        # print(p)

        # UPDATE THE IMAGE
        img.setPixel(x, y, p)
for x in range(halfWidth, img.getWidth()):
    for y in range(img.getHeight(), img.getHeight() * 2):
        # GET THE DATA
        p = img.getPixel(x, y - img.getHeight())

        # print(p)

        # UPDATE THE IMAGE
        img.setPixel(x, y, p)

# SHOW THE RESULT
win = ImageWin(img.getWidth(), 2 * img.getHeight())
img.draw(win)









