#! /usr/bin/python3
import os
import random
from PIL import Image

def pick_random_size(max_size):
    width = random.randint(1, max_size)
    height = random.randint(1, max_size)
    image_size = (width, height)
    return image_size

cur_dir = os.listdir()

for file in cur_dir:
    try:
        img = Image.open(file)
        img = img.resize(pick_random_size(100))
        img.save(f"./folder_resized_imgs/{file}")
    except Exception as e:
        pass
    
