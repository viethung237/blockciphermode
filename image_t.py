from PIL import Image
import aes_function
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()
#import numpy as np
img = Image.open('tiger-jpg.jpg')
size = width,height = img.size
binary = Image.new(img.mode,img.size)
red =[] #luu R vao list red
for x in range(width):
    for y in range(height):
         R,G,B =  img.getpixel((x,y))
         red.append(R)
s_hex='' #luu chuoi hexa cua R
for i in range(len(red)):
    s_hex += aes_function.dectohex(red[i]).upper()

block_text =[] #chia chuoi hexa thanh cac khoi 128 bit
for i in range(0, len(s_hex), 32):
    block_text.append(s_hex[i:i + 32])
m = len(block_text) - 1
n = len(block_text[m])
if n != 32:
    block_text[m] += '8'
    for i in range(32 - n - 1):
        block_text[m] += '0'
out_plain =[]
s_plain=''
b_plain =[]
for i in block_text :
    out_plain.append(aes_function.encrypt(i,key))
out_plain[m] = out_plain[m][:n]
for i in out_plain:
    s_plain += i
for i in range(0,len(s_plain),2):
    b_plain.append(aes_function.bintodec(int(aes_function.hextobin(s_plain[i:i+2]))))
k = 0
for x in range(width):
    for y in range(height):
        binary.putpixel((x,y),b_plain[k])
        k += 1
binary.show()