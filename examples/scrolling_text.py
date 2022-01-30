# MIT License

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
# Improved by the yongdol503

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os.path
import time
import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
from PIL import Image, ImageDraw, ImageFont, ImageColor

def main():
  
    color = ImageColor.getrgb('hsl(192, 100%, 84%)')
    base = Image.new('RGBA', device.size, color)
    
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'fonts', 'NanumSquareRoundEB.ttf'))

    fnt = ImageFont.truetype(font_path, device.height-70)
    

    d = ImageDraw.Draw(txt)                         

    d.text((10,30), "Yo", font=fnt, fill=(0,0,0,255))
    

    out = Image.alpha_composite(base, txt)
    
    device.display(out.convert(device.mode))

if __name__ == '__main__':
    try:
        device=TFT.ST7735(rst=24, dc=25, rotate=180, 
            spi=SPI.SpiDev(port=0,device=0,max_speed_hz=64*1000000))
        device.begin()
        main()
    except KeyboardInterrupt:
        pass
