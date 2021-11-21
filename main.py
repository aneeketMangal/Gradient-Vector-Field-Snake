# Importing required libraries
import numpy as np
from PIL import Image
import math
im = Image.open('download.png')
im = im.convert('L')
h = 1
k = 1
im2 = im.copy()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        cp = im.getpixel((i, j))
        # print(cp)
        dp = [0, 0]

        for ii in range(im.size[0]):
            for jj in range(im.size[1]):
                dh  = math.sqrt((i*i)+(j*j)+(h))
                dx = (i-ii)
                dy = (j-jj)
                x = float(dx/dh)
                y = float(dy/dh)
                fx = im.getpixel((ii, jj))
                g = 1/(1+ (abs(float(fx)-float(cp))/k)**2)
                gf = g*cp
                gf = 1
                x = x* gf
                y = y*gf
                dp[0]+=x
                dp[1]+=y
        if(i == 0 and j == 0):
            print(dp)
                

                
im.show()