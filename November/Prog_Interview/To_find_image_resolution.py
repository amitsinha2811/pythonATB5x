import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/hp/Desktop/Naukri.com/AmitPics.jpg")
width, height = img.size
print(width,"x",height)