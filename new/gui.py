#Thêm thư viện tkinter
import time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import cv2

#Tạo một cửa sổ mới
def clickRun():    
    messagebox.showinfo("State","Run")
          

def clickSave():
    messagebox.showinfo("State","Saved")
def showImg():
    img_in=cv2.imread(r'C:\Users\Admin\test_py\OpenEIT\new\bg.png')
    img_resize=cv2.resize(img_in,(200,200))
    cv2.imshow('butoon',img_resize)
    bt1=Button(text='time',image=img_resize)
    bt1.place(x=20,y=30)
    cv2.waitKey(0)
   
   
    
    

window = Tk()
window.geometry('1200x800')
menu=Menu(window)
new_item=Menu(menu)
menu.add_cascade(label='Funtion', menu=new_item)
new_item.add_command(label="Run",command=showImg)
new_item.add_command(label="Save",command=clickSave)

window.config(menu=menu)
#Thêm tiêu đề cho cửa sổ

window.title('welcome PhyK app')

#Đặt kích thước của cửa sổ


#Lặp vô tận để hiển thị cửa sổ
window.mainloop()

