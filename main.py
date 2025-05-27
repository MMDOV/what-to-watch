import os
from random import randint

path = r"/mnt/HDD/Downloads/Video/"

names = os.listdir(path)

# TODO: add some filters

rand = randint(0, len(names))

os.system(f"mpv {path}{names[rand]}")
