"""Text to Image 1.2.1 - Convert text to an image to spot hidden pareidolias.
Copyright (C) 2022  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox
import shutil
from PIL import ImageTk, Image
import io
import math

#create main window
def create_main_window():
    global top
    global root
    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAAAAABWESUoAAABJWlDQ1BJQ0MgcHJvZmlsZQAAKJGdkM1Kw0AUhb9WqVUUBEVBXGThtuDGrtz4g8FFobYRjK7SSYvFJIYkpfgGfRN9mC4EwUfwARRceya6cGE2DlzOx+Xec2YG6k5k4nxxH+KkyNzekX/lXztLbzRYZ5km24HJ007/zKPyfL5Ss/rSsl7Vc3+eRjjMjXSuSkyaFVA7FLenRWpZxead1zsRz8ROGCeh+Em8F8ahZbvbi6OJ+fG0t1kdJpd921ft4nJOhy4OAyaMiShoSRN1TmlzIHXJCHggx0gjhupNNVNwK8rl5HIs8kS6TUXeTpnXVcpAHmN52YR7YnnaPOz/fq99XJSbta15GmRB2VpQ1UcjeH+ENR82nmHlpiKr+fttFTPtcuafb/wCwG5QURqfn2MAAAAJcEhZcwAALiMAAC4jAXilP3YAAAAHdElNRQfmBhAJCy+UZC8dAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAZhJREFUOMvNk09IVFEUh78Xb4aExMVUEGEimOKiyFy0iQTRhWQtWlSLJITXMsxdbUJSCdqIgTs3KaggiIQaErkYoyLd2Az4jwqJFOSFpSM6/96vxXNwrjO2zW917r3f5RzuPccS/+YY/1+w98Odxa+rqdMllSHT0B5bgxf8Dev5D2WREZYauD6yuO6uTD3i5LiXI0RKQ6/jfuh9aaTPOyCsXTof3b+08YApU/Ae8zE7769rlTMLbpYwT6cM3gM4H1IZoYdlU0gOTYw+C/Hkjy94tbVp5eK+wIkJSb9pk9JJg5Sk9Cu6haR1Xkrj5vsNS1Kyhe82/OwjBmUjhlAOYDvdYTRXRvOo8hMvdmz3XnD2sgVvO/b+5t2np0DrTYBg3aT9JjJdDXCmOdMAp5qAs/4iUcidiwkdyvaJh/bY3QAA0wNGkbfqASKxGvvG52QA4Pg5QygA2Okquko/4cMS7LYzKNyqihkv33E66tCWkKXo7fn71XZOs26EJ+ltCoK01lWcr52v9HyTJEtAfDN3AANF/kRYR2A2/wLo0KVETuSETgAAAABJRU5ErkJggg=='

    root= tk.Tk()
    top= root
    top.geometry("260x80")
    top.title("Text to Image")
    top.resizable(0,0)
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#create_buttons
def create_buttons():
    global convert_button
    convert_button=tk.Button(top)
    convert_button.place(x=90,y=20,height=40,width=80)
    convert_button.configure(text="Convert")
    convert_button.bind("<Button-1>",open_file)

#open_file
def open_file(event):
    global textfilename
    data=[('TXT', '*.txt')]
    textfilename=askopenfilename(filetypes=data, defaultextension=data)
    #if str(soundfile)!='':
    parse()
    convert()

#parse
def parse():
    global contents
    with io.open(textfilename, 'r', encoding='utf-8') as file_object:
        contents=''
        eof=False
        while eof==False:
            try:
                char=file_object.read(1)
            except:
                char="?"
            contents=contents+char
            if char=='':
                eof=True

#valid text length
def text_length(textfile):
    global textlen
    textlen=0
    textvar=contents
    textvarlen=len(textvar)
    textfile.seek(0)
    for n in range (1,textvarlen):
        char=textfile.read(1)
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            textlen=textlen+1

#generate_header
def generate_header(textlen):
    global headerbytes
    global width
    global heigth
    global bmpsize
    ratio=(textlen)/12
    squareroot=math.sqrt(ratio)
    width=int((squareroot*4)/1.3333)
    heigth=int((squareroot*3)/1.3333)
    headerbytes=io.BytesIO()
    headerfile=open("26col2.bmp",'rb')
    bytesread=headerfile.read(2)
    headerbytes.write(bytesread)
    bmpsize=128+textlen
    filesize=width*heigth+240
    byteappend=filesize.to_bytes(4,'little')
    headerbytes.write(byteappend)
    value=0
    value=value.to_bytes(2,'little')
    headerbytes.write(value)
    value=0
    value=value.to_bytes(2,'little')
    headerbytes.write(value)
    value=240
    value=value.to_bytes(4,'little')
    headerbytes.write(value)
    value=40
    value=value.to_bytes(4,'little')
    headerbytes.write(value)    
    headerbytes.write(width.to_bytes(4,'little'))
    headerbytes.write(heigth.to_bytes(4,'little'))
    headerfile.seek(26)
    bytesread=headerfile.read(8)
    headerbytes.write(bytesread)
    filesize=width*heigth+240
    sizebyte=filesize.to_bytes(4,'little')
    headerbytes.write(sizebyte)
    headerfile.seek(38)
    bytesread=headerfile.read(206)
    headerbytes.write(bytesread)

    
#convert_bitrate
def convert():
    global headerbytes
    global width
    global heigth
    global bmpsize
    textfile=contents
    textlen=len(contents)
    generate_header(textlen)
    tempfile=open("tempfile.bmp",'wb')
    headerbytes.seek(0)
    headerread=headerbytes.read()
    tempfile.write(headerread)
    for pixels in range (1,textlen):
        char=textfile[pixels]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91):
            code=asciicode-64
            pixarray=code.to_bytes(1,'big')
            tempfile.write(pixarray)
        elif (asciicode>96 and asciicode<123):
            code=asciicode-96
            pixarray=code.to_bytes(1,'big')
            tempfile.write(pixarray)
    tempfile.close()
    data=[('BMP','*.bmp')]
    bmpfilesavename=asksaveasfilename(filetypes=data, defaultextension=data)
    shutil.copy("tempfile.bmp",bmpfilesavename)
    os.remove("tempfile.bmp")
    imgfileshow=Image.open(bmpfilesavename)
    imgfileshow.show()
      

#main             
def main():
        create_main_window()
        create_buttons()

main()
root.mainloop()
