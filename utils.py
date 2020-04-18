from glob import glob                                                           
import cv2 
import numpy as np

from PIL import Image
from PIL import Image, ImageOps


pngs = glob('./website_images/images/*.png')
i = 0
for j in pngs:

	img = Image.open(j).convert('L')
	im = img.resize((256, 256))
	im.save('./website_data/images/' + str(i) + '.jpg')
	i += 1

