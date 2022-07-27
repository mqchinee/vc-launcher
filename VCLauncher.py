# импорт библиотек
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import subprocess
from tkinter import ttk
from tkinter import filedialog
import json
from tkinter import font as tkFont
import random
import threading
import subprocess
import uuid
import pathlib
import webbrowser
import os
import pystray
from pystray import MenuItem as item
from PIL import Image

# на всякий пожарный?
from plyer.utils import platform
from plyer import notification
import plyer.platforms
import plyer.platforms.win
from plyer.platforms import *
from plyer.platforms.win import *
import plyer.platforms.win.notification

# получаем главную папку
mainpath = pathlib.Path().resolve()
openmainpath = os.path.realpath(mainpath)

# аааа мультипоток
def new_thread(threads):
	x = threading.Thread(target=threads)
	x.start()

# как я хотел вытаскивать аргументы (я забил болт)

#json_file = open("samplnick.txt")

#variables = json.load(json_file)

# Скрытый интерфейс

hidden_root = Tk()
hidden_root.geometry("0x0")
hidden_root.call('wm', 'iconphoto', hidden_root._w, tk.PhotoImage(file='assets/logo1.png'))
hidden_root.attributes('-alpha', 0)
hidden_root.title('VCLauncher')
hidden_root.configure(background="orange")

def minim(event=None):
	hidden_root.iconify()

def quitApp():
	hidden_root.destroy()

def on_focus(event):
	root.lift()

root = Toplevel(hidden_root) 
root.overrideredirect(True)
root.transient(hidden_root)
root.geometry("1150x600")
buttonf = tkFont.Font(family='Arial', size=10)
buttonf2 = tkFont.Font(family='assets/vc.otf')

placeholder = 'Введите ник...'

def erase(event=None):
	if nick.get() == placeholder:
		nick.configure(foreground='black')
		nick.delete(0,'end')
		
def add(event=None):
	if nick.get() == '':
		nick.configure(foreground='gray')
		nick.insert(0,placeholder)

# мне лень писать функцию так что DRY момент (я говнокодер, хочешь поспорить?)
		
def on_enterst(e):
	start['background'] = '#ffb733'

def on_leavest(e):
	start['background'] = 'orange'

def on_enter2(e):
	start2['background'] = '#ffb733'

def on_leave2(e):
	start2['background'] = 'orange'

def on_enter3(e):
	start3['background'] = '#3eed41'

def on_leave3(e):
	start3['background'] = '#27d62c'

def on_enter4(e):
	start4['background'] = '#3eed41'

def on_leave4(e):
	start4['background'] = '#27d62c'

def on_enter5(e):
	start5['background'] = '#3eed41'

def on_leave5(e):
	start5['background'] = '#27d62c'

def on_enter6(e):
	start6['background'] = '#e6292c'

def on_leave6(e):
	start6['background'] = '#eb1014'

def exit():
	hidden_root.destroy()

# Трей

def quit_window(icon, item):
	icon.stop()
	hidden_root.destroy()

def show_window(icon, item):
	icon.stop()
	root.after(0,root.deiconify())

def hide_window():
	# снова страхуемся?
	from PIL import Image
	# именно так, я
	root.withdraw()
	img=Image.open("assets/logo1.png")
	menu=(item('Выход', quit_window), item('Показать', show_window))
	icon=pystray.Icon("name", img, "VCLauncher", menu)

	notification.notify(
		title='VCLauncher',
		message='Теперь я тут!',
		app_name='VCLauncher',
		app_icon='assets/logo1.' + ('ico' if platform == 'win' else 'png'),
		timeout=1
	)

	icon.run()

def tostart():
	import time
	start.configure(state='disabled')
	time.sleep(1)
	start.configure(state='normal')
	anick = nick.get()
	subprocess.Popen(f'./vcclient/runtime/java-runtime-alpha/windows-x86/java-runtime-alpha/bin/javaw.exe -Djava.library.path=./vcclient/libraries/natives/ -cp "./vcclient/libraries/*" net.minecraft.client.main.Main --username {anick} --version 1.16.5 --gameDir ./vcclient --assetsDir ./vcclient/assets --assetIndex 1.16 --uuid {uuid.uuid4().hex} --accessToken {uuid.uuid4().hex} --userType mojang')
	hide_window()

# остальное

def openpath():
	os.startfile(openmainpath + "/vcclient")

def forum():
	webbrowser.open("https://vanilla-craft.ru/")

def groupvk():
	webbrowser.open("https://vk.com/vanilla.crafts")

def conversation():
	webbrowser.open("https://vk.cc/9NhbcK")

hidden_root.eval(f'tk::PlaceWindow {str(root)} center')

root.bind('<Button>', on_focus)
hidden_root.bind('<FocusIn>', on_focus)

fback = PhotoImage(file = "assets/bg.png")
logo = PhotoImage(file = "assets/logo1.png")

canvas1 = Canvas( root, width = 1150, height = 600, highlightthickness=0)

title_bar = tk.Label(canvas1, background='orange', relief='flat', bd=2, width=500, height=3)
stopb = tk.Button(canvas1, background='red', foreground='white', width=7, height=2, relief='flat', text='', activebackground='#f74f5d', bd=0, command=exit)
title_bar_c = canvas1.create_window(0, 3, window = title_bar)
stopbc = canvas1.create_window(1130, 9.6, window = stopb)

nick = tk.Entry(canvas1, background = 'white', foreground= 'black', width=66, relief='flat')
nick.bind('<FocusIn>', erase)
add()
nick_c = canvas1.create_window(63.7, 230, anchor="nw", window=nick)

start = tk.Button(canvas1, background='orange', foreground='white', width=49, height=2, relief='flat', text='Войти в игру', activebackground='#ffb733', bd=0, command=tostart)
start_c = canvas1.create_window(65, 260, anchor="nw", window=start)

start2 = tk.Button(canvas1, background='orange', foreground='white', width=49, height=2, relief='flat', text='Открыть папку с клиентом', activebackground='#ffb733', bd=0, command=openpath)
start_c2 = canvas1.create_window(65, 310, anchor="nw", window=start2)

start3 = tk.Button(canvas1, background='#27d62c', foreground='white', width=16, height=2, relief='flat', text='Форум', activebackground='#36d139', bd=0, command=forum)
start_c3 = canvas1.create_window(65, 360, anchor="nw", window=start3)

start4 = tk.Button(canvas1, background='#27d62c', foreground='white', width=16, height=2, relief='flat', text='VK', activebackground='#36d139', bd=0, command=groupvk)
start_c4 = canvas1.create_window(205, 360, anchor="nw", window=start4)

start5 = tk.Button(canvas1, background='#27d62c', foreground='white', width=16, height=2, relief='flat', text='Беседа', activebackground='#36d139', bd=0, command=conversation)
start_c5 = canvas1.create_window(345, 360, anchor="nw", window=start5)

start6 = tk.Button(canvas1, background='#eb1014', foreground='white', width=49, height=2, relief='flat', text='Отправить лаунчер в трей', activebackground='#de1417', bd=0, command=hide_window)
start_c6 = canvas1.create_window(65, 410, anchor="nw", window=start6)

start.bind("<Enter>", on_enterst)
start.bind("<Leave>", on_leavest)

start2.bind("<Enter>", on_enter2)
start2.bind("<Leave>", on_leave2)

start3.bind("<Enter>", on_enter3)
start3.bind("<Leave>", on_leave3)

start4.bind("<Enter>", on_enter4)
start4.bind("<Leave>", on_leave4)

start5.bind("<Enter>", on_enter5)
start5.bind("<Leave>", on_leave5)

start6.bind("<Enter>", on_enter6)
start6.bind("<Leave>", on_leave6)

canvas1.pack(fill = "both", expand = False)
canvas1.create_image( 0, 0, image = fback, anchor = "nw")

canvas1.create_image( 50, 80, image = logo, anchor = "nw")

canvas1.create_text(304, 150, font=('arial', 30), text = "VC               ", fill="Orange")
canvas1.create_text(304, 150, font=('arial', 30), text = "     Launcher", fill="White")
canvas1.create_text(60, 580, font=('arial', 10), text = "VCLauncher v1.0", fill="White")

lastClickX = 0
lastClickY = 0

start.configure(font=buttonf)
start2.configure(font=buttonf)
start6.configure(font=buttonf)

def SaveLastClickPos(event):
	global lastClickX, lastClickY
	lastClickX = event.x
	lastClickY = event.y

def Dragging(event):
	x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
	root.geometry("+%s+%s" % (x , y))

title_bar.bind('<Button-1>', SaveLastClickPos)
title_bar.bind('<B1-Motion>', Dragging)

root.mainloop()