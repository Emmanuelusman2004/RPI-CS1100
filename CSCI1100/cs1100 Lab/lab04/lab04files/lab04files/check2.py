# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:20:07 2022

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
'im.jpg', 'hk.jpg','bw.jpg',
blankimg = Image.new('RGB', (512, 512), (255,255,255)) 
#blankimg.show()


ca = ca.resize((256,256))
im = im.resize((256,256))
hk = hk.resize((256,256))
bw = bw.resize((256,256))
#care.show()

blankimg.paste(ca, (0,0))
blankimg.paste(im, (256,0))
blankimg.paste(hk, (0,256))
blankimg.paste(bw, (256,256))
blankimg.show()

print(blankimg.size)