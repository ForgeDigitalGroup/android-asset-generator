from PIL import Image, ImageColor

# name of the file to save
importFilename = "../background-color.txt"
exportFilename = "ic_launcher_background.png"

width = 500
height = 500

with open(importFilename) as file:
    hexColor = file.readline()

print('Color:', hexColor)

img = Image.new(mode="RGB", size=(width, height), color=ImageColor.getrgb(hexColor))
img.save(exportFilename)
