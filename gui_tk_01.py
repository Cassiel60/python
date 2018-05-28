# -*- coding: utf-8
from Tkinter import *
root = Tk()
root.title("Welcome to WUST")
root.geometry('300x200')

Label(root, text=u'武科大校训', font=('Arial', 20)).pack()

frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text=u'厚德', font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text=u'博学', font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text=u'崇实', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text=u'去浮', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

root.mainloop()