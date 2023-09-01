# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:29:36 2022

@author: Emmanuel Usman
"""

from PIL import Image
ca = 'ca.jpg'
ca = Image.open(ca)
im = 'im.jpg'
im = Image.open(im)
hk = 'hk.jpg'
hk = Image.open(hk)
bw = 'bw.jpg'
bw = Image.open(bw)
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