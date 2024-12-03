import random
from PIL import Image
import numpy as np
import math

width=13680; height=10080
boxsize=180; halfsize=90
d=halfsize-45
color_list = [(70,32,102), (255,184,95), (255,122,90), (0,170,160), (142,210,201)]
background_color = (255,255,255)
connections_counter=0
mat = np.zeros((height, width, 3), dtype=np.uint8)

  
# painting time - dots and background
for x in range(0,width,boxsize):
    for y in range(0,height,boxsize):
        color=random.choice(color_list)
        centerx=x+halfsize; centery=y+halfsize           

        for i in range(x,x+boxsize):
            for o in range(y,y+boxsize):
                if int(math.sqrt(math.pow(o-centery,2)+math.pow(i-centerx,2)))  < d:
                    mat[o][i]=color
                else:
                    mat[o][i] = background_color   #background

# connecting same color dots
for x in range(0,width-boxsize,boxsize):
    for y in range(0,height-boxsize,boxsize):
        color=mat[y+halfsize][x+halfsize]
        # horizontal -
        if (str(mat[y+halfsize][x+halfsize]) == str(mat[y+halfsize][x+halfsize+boxsize]) ):
            connections_counter=connections_counter+1
            for i in range(x+halfsize,x+halfsize+boxsize):
                mat[y+halfsize][i]=color;mat[y+halfsize+1][i]=color;mat[y+halfsize-1][i]=color
        # vertical |
        if str(mat[y+halfsize][x+halfsize]) == str(mat[y+halfsize+boxsize][x+halfsize]):
            connections_counter=connections_counter+1
            for i in range(y+halfsize,y+halfsize+boxsize):
                mat[i][x+halfsize]=color;mat[i][x+halfsize+1]=color;mat[i][x+halfsize-1]=color
        # diagonal \
        if str(mat[y+halfsize][x+halfsize]) == str(mat[y+halfsize+boxsize][x+halfsize+boxsize]):
            connections_counter=connections_counter+1
            ii=x+halfsize
            for i in range(y+halfsize,y+halfsize+boxsize):
                mat[i][ii]=color;mat[i][ii+1]=color;mat[i][ii-1]=color;
                ii=ii+1
        # diagonal /
        if str(mat[y+halfsize+boxsize][x+halfsize]) == str(mat[y+halfsize][x+halfsize+boxsize]):
            connections_counter=connections_counter+1
            color=mat[y+halfsize+boxsize][x+halfsize]
            ii=x+halfsize
            for i in range(y+halfsize+boxsize,y+halfsize,-1):
                mat[i][ii]=color;mat[i][ii+1]=color;mat[i][ii-1]=color;
                ii=ii+1

# connecting same color dots: edge cases
for x in range(0,width-boxsize,boxsize):
    if (str(mat[height-halfsize][x+halfsize]) == str(mat[height-halfsize][x+halfsize+boxsize])):
        connections_counter=connections_counter+1
        color=mat[height-halfsize][x+halfsize]
        for i in range(x+halfsize,x+halfsize+boxsize):
            mat[height-halfsize][i]=color;mat[height-halfsize][i+1]=color;mat[height-halfsize][i-1]=color;

for y in range(0,height-boxsize,boxsize):
    if (str(mat[y+halfsize][width-halfsize]) == str(mat[y+halfsize+boxsize][width-halfsize])):
        connections_counter=connections_counter+1
        color=mat[y+halfsize][width-halfsize]
        for i in range(y+halfsize,y+halfsize+boxsize):
            mat[i][width-halfsize]=color;mat[i][width-halfsize+1]=color;mat[i][width-halfsize-1]=color;

# Printing number of connections and printing the image
print("Number of connections: ",connections_counter)
im = Image.fromarray(mat,mode="RGB")
im.save("image.png")
print("Success exporting image.png")
