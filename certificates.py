import pandas as pd
from PIL import Image, ImageDraw, ImageFont

d1 = pd.read_csv('name.csv')
name_list = d1["name"].tolist() 
for i in name_list:
    im = Image.open('Event Certificate Template.jpg')
    d = ImageDraw.Draw(im)
    location = (121, 600)
    text_color = (0,188,255)
    selectFont = ImageFont.truetype("C:/WINDOWS/FONTS/SEGOEUI.TTF", 100)
    d.text(location, i, fill = ((text_color)), font = selectFont)
    im.save("Certificate_" + i + ".png")
