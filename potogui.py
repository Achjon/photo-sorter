#!/usr/bin/python3
import os 
import glob
import shutil
from os import listdir
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()


cesta = filedialog.askdirectory(parent=root,initialdir="/home/matej/",title='Vyberte složku s fotkami')

os.mkdir(cesta + "/jpg");
os.mkdir(cesta + "/raw");
os.mkdir(cesta + "/video");


jpg = cesta + "/jpg"
raw = cesta + "/raw"
video = cesta + "/video"
os.chdir(cesta)

for file in os.listdir(cesta):
    if file.endswith(".JPG") or file.endswith(".jpg"):
        shutil.move(file, jpg)

for file in os.listdir(cesta):
    if file.endswith(".CR2")or file.endswith(".cr2")or file.endswith(".cr3")or file.endswith(".CR3"):
        shutil.move(file, raw)

for file in os.listdir(cesta):
    if file.endswith(".MP4") or file.endswith(".mp4"):
        shutil.move(file, video)





