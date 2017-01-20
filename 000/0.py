
import PIL
pic = PIL.Image.open('0.jpg')
draw = PIL.ImageDraw.Draw(pic)
draw.text((470,0),'1','#FF8247')
pic.show()