import random
from PIL import Image
import numpy as np

width=3840; height=2160; boxsize=60
color_list = [(240,248,255), (238,106,80), (135,206,255), (54,100,139)]

mat = np.zeros((height, width, 3), dtype=np.uint8)

for x in range(0,width,boxsize):
    for y in range(0,height,boxsize):
        color=random.choice(color_list)
        for i in range(x,x+boxsize):
            for o in range(y,y+boxsize):
                mat[o][i]= color

im = Image.fromarray(mat,mode="RGB")
im.save("image.png")