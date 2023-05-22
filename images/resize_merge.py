#!/usr/bin/python3

from PIL import Image

image = Image.open('merge.jpeg')
wid, hie = image.size

print('resizing image: ', image.size)

new_image = image.resize((int(wid*.75), int(hie*.75)))
new_image.save('smaller_merge.jpeg')

print('image resized successfully;', new_image.size)

