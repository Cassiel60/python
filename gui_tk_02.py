#-*-coding:utf-8-*-

import Tkinter
from Tkconstants import *

def callback():
	var.set(u'吹吧你，我才不信呢')

root= Tkinter.Tk()
frame1=Tkinter.Frame(root)
frame2=Tkinter.Frame(root)


var=Tkinter.StringVar()   # 未在StringVar()前面加入Tkinter,会一直提示报错，StringVaar()未定义。
var.set(u'您下载的影片含有未成年人限制内容，\n请满18周岁后再点击观看！')
textLabel=Tkinter.Label(frame1,
				textvariable=var,
				justify=LEFT)

textLabel.pack(side=LEFT)

photo=Tkinter.PhotoImage('1.gif')
imgLabel=Tkinter.Label(frame1,image=photo)
imgLabel.pack(side=RIGHT)

theButton=Tkinter.Button(frame2,text=u'我已经满18周岁',command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

root.mainloop()