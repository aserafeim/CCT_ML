# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:38:26 2021

@author: alexs
"""

from PIL import Image

image=Image.open('CCT_4140.jpg')

###Get image dimensions

##Calculate new image dimensions


test=image.size

new_image=image.resize((400,400))

new_image.save('test_image.png')

