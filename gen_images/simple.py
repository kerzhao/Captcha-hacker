import os, sys
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter

width = 130
height = 53
# alternative
font_path = 'F:/gtest/Captcha-hacker/gen_images/fonts/english/Helvetica Narrow Bold.ttf'
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype(font_path, 36)
draw = ImageDraw.Draw(image)


def rand_char():
	upper = chr(random.randint(65, 90))
	lower = chr(random.randint(97, 122))
	digit = chr(random.randint(48, 57))
	cpool = [upper, lower, digit]
	return random.choice(cpool)

def rand_color_char():
	R = random.randint(32, 127)
	G = random.randint(32, 127)
	B = random.randint(32, 127)
	return (R, G, B)

def rand_color_back():
	R = random.randint(64, 255)
	G = random.randint(64, 255)
	B = random.randint(64, 255)
	return (R, G, B)

"""
def rand_font():
	fonts = os.listdir('fonts')
	return random.choice(fonts)
"""

def draw_back():
	for x in range(width):
		for y in range(height):
			draw.point((x, y), fill=rand_color_back())
	return None

def draw_char():
	for c in range(4):
		draw.text((60*c+10, 10), rand_char(), font=font, fill=rand_color_char())
	return None

def draw_all(fn, form):
	draw_back()
	draw_char()
	i = image.filter(ImageFilter.GaussianBlur)
	i.save(fn, form)

draw_all('captcha.jpg', 'jpeg')