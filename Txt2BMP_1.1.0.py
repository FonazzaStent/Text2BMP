import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox
import shutil
from PIL import ImageTk, Image

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
    convert()

#convert_bitrate
def convert():
    headerbytes= b'B'b'M'b'\xf2'b'\xb0'b'\x04'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xf2'b'\x00'b'\x00'b'\x00'b'|'b'\x00'b'\x00'b'\x00'b'\x80'b'\x02'b'\x00'b'\x00'b'\xe0'b'\x01'b'\x00'b'\x00'b'\x01'b'\x00'b'\x08'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xb0'b'\x04'b'\x00'b'\x12'b'\x17'b'\x00'b'\x00'b'\x12'b'\x17'b'\x00'b'\x00'b'\x1a'b'\x00'b'\x00'b'\x00'b'\x1a'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xff'b'\x00'b'\x00'b'\xff'b'\x00'b'\x00'b'\xff'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'B'b'G'b'R'b's'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x02'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xfd'b'\x00'b'M'b'\x00'b'\xff'b'\x00'b'\xa5'b'\x00'b'7'b'\x00'b'\xfd'b'\x00'b'k'b'\x00'b'\xff'b'\x00'b'\xff'b'\x00'b'\xe4'b'\x00'b'\xff'b'G'b'\x00'b'\x00'b'\xd7'b'\x00'b'\xff'b'\x00'b'\xa6'b'\x05'b'\xff'b'\x00'b'B'b'D'b'|'b'\x00'b'\x00'b'"'b'\xff'b'\x00'b'\xff'b'\x8e'b'\x00'b'\x00'b'\x00'b'b'b'\xff'b'\x00'b'\x00'b'\x8c'b'\xff'b'\x00'b'\xff'b'\xcc'b'\x00'b'\x00'b'^'b'\xff'b'\x00'b'\x00'b'\x00'b'\xb9'b'\xff'b'\x00'b'\x93'b'\xff'b'\x00'b'\x00'b'\n'b'\xff'b'&'b'\x00'b'\xf9'b'\xf9'b'\x00'
    textfile=open(textfilename,'r')
    tempfile=open("tempfile.bmp",'wb')
    tempfile.write(headerbytes)
    for pixels in range (1,1921600):
        char=textfile.read(1)
        if char=='':
            textfile.seek(0,0)
        else:
            asciicode=ord(char)
            if asciicode >97 and asciicode<123:
                code=asciicode-97
                pixarray=code.to_bytes(2,'big')
            #print (pixarray)
                tempfile.write(pixarray)
            #print (pixarray)
    #imgfile=Image.open("tempfile.bmp")    
    #img=imgfile.convert("P", palette=Image.Palette.ADAPTIVE, dither=Image.Dither.FLOYDSTEINBERG, colors=256)
    data=[('BMP','*.bmp')]
    bmpfilesavename=asksaveasfilename(filetypes=data, defaultextension=data)
    shutil.copy("tempfile.bmp",bmpfilesavename)
    tempfile.close()
    textfile.close()
    os.remove("tempfile.bmp")
    imgfileshow=Image.open(bmpfilesavename)
    imgfileshow.show()
    
        

#main             
def main():
        create_main_window()
        create_buttons()

main()
root.mainloop()
