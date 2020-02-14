from tkinter import *
from tkinter import messagebox
import re, pymysql
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import pypdfocr.pypdfocr_gs as pdfImg
from PIL import Image, ImageTk
import sys
from collections import OrderedDict 

def tableFormate(data,table_frame):
    global screen,df
    global string_table
    x=60
    y=30
    string="App Name\t\tCategory\tRating    \tReviews\t\tSize\tInstalls\t\tType\tPrice\tContent Rating\t Geners\t\tLast Update\tCurr ver    Android Ver\n"
    tk.Label(table_frame,text=string,font=("Helvetica",11,'bold'),fg='black',bg='#d8dce3').place (x=x-3,y=y)
    
    for index in range(len(data)):
        if index%2==0:
            color='#ffffff'
        else:
            color='#f5f5f5'
        y+=30
        string ="{}...\t\t{}\t  {}    \t{}\t\t{}\t{}   \t{}\t{}\t{}              \t{}\t{}\t{}\t  {}     \n".format(data['App'][index][0:13],str(data['Category'][index])[0:10],str(data['Rating'][index]) ,str(data['Reviews'][index]),str(data['Size'][index]),str(data['Installs'][index])[0:9],str(data['Type'][index]),str(data['Price'][index]),str(data['Content Rating'][index]),str(data['Genres'][index])[0:12],str(data['Last Updated'][index])[0:10],str(data['Current Ver'][index])[0:6],str(data['Android Ver'][index])[0:9])
        tk.Label(table_frame,text=string,font=("Helvetica",11,'bold'),fg='black',bg=color, borderwidth=2, relief="groove").place(x=x,y=y)
    
    summary = "Summary\t\t Rows : %d  Columns : %d "%(df.shape[0],df.shape[1])
    
    tk.Label(table_frame,text=summary,font=("Helvetica",11,'bold'),fg='black',bg="white" ).place(x=x,y=y+45)
    
    #insert_button = tk.Button(table_frame,fg="white",font=('Helvetica',10,'bold'),width=13,text="+ADD",bg="#7aaffa",command=mouseClick).place(x=1315,y=y+42)
    
# This function is used for adjusting window size and making the necessary configuration on start of window
def adjustWindow(window):
    w = 1200 # width for the window size 1200
    h = 700 # height for the window size 700
    ws = screen.winfo_screenwidth() # width of the screen
    hs = screen.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen and where it is placed
    window.resizable(False, False) # disabling the resize option for the window
    window.configure(background='white') # making the background white of the window
    
def donothing():
   
   print("File not exist")
   
def int_menubar(screen):
    menubar = Menu(screen)
    
    categorymenu = Menu(menubar, tearoff = 0)
    menubar.add_command(label = "Home",command=overviewClick)
    
    categorymenu.add_separator()
    categorymenu.add_command(label = "category", command =categoryClick)
    menubar.add_cascade(label = "Category", menu = categorymenu)
    
    installmenu = Menu(menubar, tearoff=0)
    installmenu.add_separator()
    installmenu.add_command(label = "install", command = installClick)
    menubar.add_cascade(label = "Install", menu = installmenu)
    
    srmenu = Menu(menubar, tearoff=0)
    srmenu.add_command(label = "Study Review", command = reviewClick)
    menubar.add_cascade(label = "Study Review", menu = srmenu)
    
    mldmenu = Menu(menubar, tearoff=0)
    mldmenu.add_command(label = "M L Model", command = donothing)
    menubar.add_cascade(label = "M L Model", menu = mldmenu)
        
    idatamenu = Menu(menubar, tearoff=0)
    idatamenu.add_command(label = "Insert Data", command = dataInserteClick)
    menubar.add_cascade(label = "Insert Data", menu = idatamenu)
    
    samenu = Menu(menubar, tearoff=0)
    samenu.add_command(label = "Serch App", command = donothing)
    menubar.add_cascade(label = "Serch App", menu = samenu)
        
    
    screen.config(menu = menubar)

def overviewClick():
    global screen
    #import InsightsDesign as over
    #over.startingScreen(screen)
    screen.destroy()
    main_screen()


def categoryClick():
    global screen
    import catgory as cat
    cat.startingScreen(screen)


def reviewClick():
    global screen
    import review as rev
    rev.startingScreen(screen)
    
def machineClick(event):
    global screen 
    import InsightsDesignForMachineLearningModels as mac
    mac.startingScreen(screen)

def installClick():
    global screen
    import install as inst
    inst.startingScreen(screen)
    
def searchAppClick(event):
    global screen
    import InsightsDesignForSearchApp as app
    app.startingScreen(screen)

    
def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)

def dataInserteClick():
    global screen
    import DesignToInsertData as did 
    did.startingScreen(screen)

def sizeClick(event):
    print("")
    
def main_screen():
    global screen,df
    screen = Tk() # initializing the tkinter window
    screen.title("google case study") # mentioning title of the window
    adjustWindow(screen) # configuring the window
    
    Label(screen, text="Google App - Survery Manager", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#d9660a').pack()
    Label(text="", bg='white').pack() # for leaving a space in between
    int_menubar(screen)
   
    Label(screen, text="", bg='#51EE13', width='20', height='20').place(x=0, y=100)
    Message(screen, text='" The best way to find yourself is to lose yourself in the service of others."  \n\n - By --Mohandas Karamchand Gandhi', width='180', font=("Helvetica", 10, 'bold', 'italic'), fg='white', bg='#51EE13', anchor = CENTER).place(x=10, y=100)
    #photo = PhotoImage(file="google_play.png") # opening left side image - Note: If image is in same folder then no need to mention the full path
    #label = Label(screen,width='150', height="150", image=photo, text="") # attaching image to the label
    #label.place(x=20, y=250)
    #label.image = photo # it is necessary in Tkinter to keep a instance of image to display image in label
   
    df=pd.read_csv(r'C:\Users\Dell1\Music\googleplaystore-App-data.csv')
    big_frame = tk.Frame(screen,bg='white',width='1000',height='550',bd=4,relief=RIDGE)
    big_frame.place(x=200,y=100)
    table_frame = tk.Frame(big_frame,bg='white',width='1500',height='410',bd=4,relief=RIDGE)
    table_frame.place(x=1,y=100)

    tk.Label(table_frame,text="App's Data Table",width=15,height='1',font=("Calibri",11,'bold'),fg='black',bg='white').place(x=0,y=0)
    
    tableFormate(df[0:10],table_frame)
    
    #insert_button = tk.Button(screen,bd=2,fg="black",font=('Helvetica',9,'bold'),width=20,text="+ADD",bg="#3869d1",command=lambda :ds.startingScreen(screen)).place(x=20,y=500)
    
    
    df=df.replace(np.NaN,-999)

    screen.mainloop()

main_screen()
    