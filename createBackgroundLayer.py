from PIL import Image
import sys
# name of the file to save
filename = "ic_launcher_background.png"

width = 500
height = 500
color1 = int(sys.argv[1])
color2 = int(sys.argv[2])
color3 = int(sys.argv[3])

img = Image.new(mode="RGB", size=(width, height), color=(color1, color2, color3))
img.save(filename)