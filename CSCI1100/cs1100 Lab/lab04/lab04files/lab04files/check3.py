# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:26:03 2022

@author: Emmanuel Usman
"""

from PIL import Image
from check2_helper import make_square

ca = 'ca.jpg'
ca = Image.open(ca)
ca = make_square(ca)
im = 'im.jpg'
im = Image.open(im)
im = make_square(im)
hk = 'hk.jpg'
hk = Image.open(hk)
hk = make_square(hk)
bw = 'bw.jpg'
bw = Image.open(bw)
bw = make_square(bw)

#ca.show()

blankimg = Image.new('RGB', (1000, 360), (255,255,255)) 
#blankimg.show()


ca = ca.resize((148,256))
im = im.resize((148,256))
hk = hk.resize((148,256))
bw = bw.resize((148,256))
bw = bw.resize((148,256))
bw = bw.resize((148,256))
#care.show()

blankimg.paste(ca, (31,20))
blankimg.paste(im, (189,60))
blankimg.paste(hk, (347,20))
blankimg.paste(bw, (505,60))
blankimg.paste(bw, (663,20))
blankimg.paste(bw, (821,60))
blankimg.show()

print(blankimg.size)