import os, sys
from PIL import Image

max_width = 700

imgs = [f for f in os.listdir("images/")]
to_remove = []
for img_name in imgs:
    try:
        print(img_name)
        img = Image.open("images/{}".format(img_name))
        wpercent = (max_width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((max_width, hsize), Image.Resampling.LANCZOS)
        img.save("images/{}".format(img_name))
    except:
        to_remove.append("images/{}".format(img_name))