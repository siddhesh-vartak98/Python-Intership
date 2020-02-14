import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import pypdfocr.pypdfocr_gs as pdfImg
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.cm as cm

def adjSmallwindow(window):
    w = 750 # width for the window size
    h = 700 # height for the window size
    ws = screen.winfo_screenwidth() # width of the screen
    hs = screen.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen and where it is placed
    window.resizable(False, False) # disabling the resize option for the window
    window.configure(background='white') # making the background white of the window

def adjustWindow(window):  #mian window
    w = 1200 # width for the window size
    h = 690 # height for the window size
    ws = screen.winfo_screenwidth() # width of the screen
    hs = screen.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen and where it is placed
    window.resizable(False, False) # disabling the resize option for the window
    window.configure(background='white') # making the background white of the window



"""Ques 1 START====================================================================================================================""" 
def function_q1(event):
    global screen
  
    root = Toplevel(screen)
    
    big_frame = tk.Frame(root,bg='white',width='1010',height=750,bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)

    
    w=1025
    h=800
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="percentage download in each category on the playstore",width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()

    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    
    df=df.replace(np.NaN,-999)
    
    dict_cat_count = {}
    for index in range(len(df)):
        
        if df['Category'][index]==-999:
            continue
        
        if df['Category'][index] in dict_cat_count:
            dict_cat_count[df['Category'][index]]+=1
        else:
            dict_cat_count[df['Category'][index]]=1
    
    y_count=[]
    x_label=[]
    for i in dict_cat_count:
        x_label.append(i)
        y_count.append(dict_cat_count[i])
    
    figure1 = plt.Figure(figsize=(10,7), dpi=100)
    
    color = cm.rainbow(np.linspace(0, 1, len(x_label)))
    #fig1, ax1 = plt.subplots()
    ax3 = figure1.add_subplot(111)
    ax3.pie(y_count, labels=x_label,colors = color, autopct='%1.1f%%', startangle=200)
    ax3.set_title("Pie chart on Category")
    #ax3.xlim(0,3.0)
    pie_plot = FigureCanvasTkAgg(figure1, big_frame) 
    pie_plot.get_tk_widget().place(x=0,y=0)
    #ax3.legend(loc=0) 
    
    string = """
    FAMILY and GAME were the most common categories, accounting for about 18.2% and 10.6% respectively, of the total number of
    apps in our dataset. Parenting,Wheather and Comics were the least prevalent category with less than 1% of the total number 
    of apps in our dataset.
    """
    tk.Label(big_frame,text=string,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=590)
    root.mainloop()
    
"""Ques 1 END===================================================================================================================="""


"""Ques 10 START================================================================================================================"""
def install():
    Installs=[]
    global sample
    for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
           Installs.append(0)
        else:
           Installs.append(int(i.replace('+','').replace(',','')))
    return Installs 


def qn10part2():
    global sample
    content=sample['Content Rating']
    counter=0
    installs=install()
    teen=0
    mature=0
    x=0
    for i in content:
        if i.strip()=='Teen':
            teen=teen+installs[counter]
            counter=counter+1
        elif i.strip()=='Mature 17+':
            mature=mature+installs[counter]
            counter=counter+1
    return teen,mature
         
def function_q10(event):
    global sample
    sample = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='450',height='500',bd=4,relief=RIDGE)
    big_frame.place(x=30,y=60)
    w=500
    h=570
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    
    teen,mature = qn10part2()
    
    #print(teen,mature)
    #print(teen/mature)
    
    #plt.bar(['teen','mature'],[teen,mature],color=['pink','blue'])
    
    label = ['teen','mature']
    val= [teen,mature]
    color = color=['green','yellow']
    figure2 = plt.Figure(figsize=(4,4), dpi=100)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    bar_plot = chart.bar(label,val,color=color)
    
    chart.set_ylabel("Frequency")
    chart.set_xlabel("Installs")
    figure2.suptitle("Installs for Teen")
    chart.legend()
    """
    for idx,rect in enumerate(bar_plot):
            height = rect.get_height()
            chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,val[idx],ha='center', va='bottom', rotation=0)
    """
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=0,y=10)

    String ="""The ratio of downloads for the app that 
               qualifies as teen versus mature17+ is {:.1f}""".format(teen/float(mature))
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=410)

    root.mainloop()

"""Ques 10 END ================================================================================================================="""


"""Ques 2 START===================================================================================================================="""
def install():
    global sample
    Installs=[]
    for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
           Installs.append(0)
        else:
           Installs.append(int(i.replace('+','').replace(',','')))
    return Installs  



def compare():
    global solution,Installs,sample
    r1=0  #number of apps under 10000 to 50000
    r2=0  #number of apps under 50000 to 150000
    r3=0  #number of apps under 150000 to 500000
    r4=0  #number of apps under 500000 to 5000000
    r5=0  #number of apps over 5000000
    temp1,temp2,temp3,temp4,temp5=[],[],[],[],[]
    
    for i in range(len(Installs)):
        if i!=10472:
            if Installs[i]>=10000 and Installs[i]<50000:
                r1=r1+1
                temp1.append(sample['App'][i])
            if Installs[i]>=50000 and Installs[i]<150000:
                r2=r2+1
                temp2.append(sample['App'][i])
            if Installs[i]>=150000 and Installs[i]<500000:
                r3=r3+1
                temp3.append(sample['App'][i])
            if Installs[i]>=500000 and Installs[i]<5000000:
                r4=r4+1
                temp4.append(sample['App'][i])
            if Installs[i]>=5000000:
                r5=r5+1
                temp5.append(sample['App'][i])
    solution=[temp1,temp2,temp3,temp4,temp5]
    return [r1,r2,r3,r4,r5]

def function_q2(event):
    global screen,Installs,solution,sample
    # source for question 2
    Installs=[]             # list for storing integer based installation for easy comparision
    solution=[1,1,1,1,1]             #list storing names of apps which falls under particular category of sorting
    
    sample=pd.read_csv(r'C:\Users\Dell1\Music\googleplaystore-App-data.csv')#reading data for the data set
    sample=sample.replace(np.NaN,0)
    sample.drop(index=[10472],inplace=True)
    
    Installs=install()
    ''' for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
            Installs.append(0)
        else:
            Installs.append(int(i.replace('+','').replace(',',''))) '''
    
    global screen,df,dict_app_relation
    
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='650',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=30,y=60)
    adjSmallwindow(root)
    
    label = ["10k-50k","50k-150k","150k-500k","500k-5M","More than 5M"]    
    val = compare()
    
    color = cm.rainbow(np.linspace(0, 1, 10))
    figure2 = plt.Figure(figsize=(6,4), dpi=100)

    chart = figure2.add_subplot(111)
    bar_plot = chart.bar(label,val,color=color)
    chart.set_ylabel("Frequency")
    chart.set_xlabel("Installs")
    figure2.suptitle("Month Indicating best downloads")
    chart.legend()

    for idx,rect in enumerate(bar_plot):
            height = rect.get_height()
            chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,val[idx],ha='center', va='bottom', rotation=0)
    
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=0,y=10)

    String="""
    The Google Play Store offers a wide range of applications,
    Many Applications got 500k-5M and more than 5M Installs
    Not a single Application has the Install in range between 150K-500K,
    45% of application have got more than 500K Installs
    """
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=40,y=400)
    root.mainloop()
    


"""Ques 2 END===================================================================================================================="""

#Cleaning the Size Column

"""
- using this method to clean "size" column
- size column contains the strings like 
'M' stands for megabyte
"Varies with device"
"k" stands for kilobyte

finally convert every app size to megabytes and return as float type
"""
#def size_row():
''''global sample
    SizeR=[]
    for i in sample['Size']:  #converting string based installs into integer based
        if i=='10,000+':
            SizeR.append(0)
        elif 'k' in SizeR:
            x=SizeR[-1:]
            SizeR.append(float(i.replace('x',''))/1000)
        elif i=='Varies with device':
           SizeR.append(0)
        elif 'M' in SizeR:
            x=SizeR[-1:]
            SizeR.append(float(i.replace('M','')))
    return SizeR '''
def size(size):
    if 'M' in size:
        x = size[:-1]
        x = float(x)*1000000
        return(x)
    elif 'k' == size[-1:]:
        x = size[:-1]
        x = float(x)*1000
        return(x)
    else:
        return None 

def compare1():
    global solution,Size,sample
    r1=0  #number of apps under 10000 to 50000
    r2=0  #number of apps under 50000 to 150000
    r3=0  #number of apps under 150000 to 500000
    temp1,temp2,temp3=[],[],[]
    
    for i in range(len(sample["Size"])):
        if i!='10,000+':
            if (sample["Size"][i])>=10000000 and (sample["Size"][i])<20000000:
                r1=r1+1
                temp1.append(sample['App'][i])
            if (sample["Size"][i])>=20000000 and (sample["Size"][i])<30000000:
                r2=r2+1
                temp2.append(sample['App'][i])
            if (sample["Size"][i])>=30000000:
                r3=r3+1
                temp3.append(sample['App'][i])
    solution=[temp1,temp2,temp3]
    return [r1,r2,r3]

def function_q3(event):
    global screen,SizeR,solution,sample
    # source for question 2
    SizeR=[]             # list for storing integer based installation for easy comparision
    solution=[1,1,1]             #list storing names of apps which falls under particular category of sorting
    
    sample=pd.read_csv(r'C:\Users\Dell1\Music\googleplaystore-App-data.csv')#reading data for the data set
    sample=sample.replace(np.NaN,0)
    #sample.drop(index=[10472],inplace=True)
    
    #SizeR=size_row()
    sample["Size"] = sample["Size"].map(size)
    print(sample["Size"])
    global screen,df,dict_app_relation
    
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='650',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=30,y=60)
    adjSmallwindow(root)
    
    label = ["10-20MB","20-30MB","More than 30MB"]    
    val = compare1()
    
    color = cm.rainbow(np.linspace(0, 1, 10))
    figure2 = plt.Figure(figsize=(6,4), dpi=100)

    chart = figure2.add_subplot(111)
    bar_plot = chart.bar(label,val,color=color)
    chart.set_ylabel("Frequency")
    chart.set_xlabel("Size")
    figure2.suptitle("Month Indicating best downloads")
    chart.legend()

    for idx,rect in enumerate(bar_plot):
            height = rect.get_height()
            chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,val[idx],ha='center', va='bottom', rotation=0)
    
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=0,y=10)

    String="""
    The Google Play Store offers a wide range of applications,
    Many Applications got xxx-xx and more than xM Installs
    Not a single Application has the Install in range between xxxxxxx,
    xx% of application have got more than xxxx Installs
    """
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=40,y=400)
    root.mainloop()




"""Ques 7 START===================================================================================================================="""
def function_q7(event):
    
    global screen,df,dict_app_relation
    
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='700',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=30,y=60)
    w=750
    h=700
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')
    
    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    #print(df.head(5))
    
    dict_varies=[]
    dict_andro=[]
    
    """These Dictionary will store the key as Category of App and items as name of the app"""
    dict_cat_app_var={}
    dict_cat_app_andro={}
    
    df.drop(df.index[9148],axis=0, inplace=True)
    df.drop(df.index[10472],axis=0,inplace=True)
    # Data cleaning for "Installs" column
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    for index in range(len(df['App'])):
        try:
            if df['Android Ver'][index] == "Varies with device":
                dict_varies.append(df['Installs'][index])
                if df['Category'][index] in dict_cat_app_var:
                    dict_cat_app_var[df['Category'][index]]+=df['Installs'][index]
                else:
                    dict_cat_app_var[df['Category'][index]] = df['Installs'][index]
                #dict_varies[df['App'][index]] = df['Installs'][index]
            else:
                dict_andro.append(df['Installs'][index])
                #dict_andro[df['App'][index]] = df['Installs'][index]
                if df['Category'][index] in dict_cat_app_andro:
                    dict_cat_app_andro[df['Category'][index]]+=df['Installs'][index]
                else:
                    dict_cat_app_andro[df['Category'][index]]=df['Installs'][index]
        except:
            continue
        
    sum_varies = sum(dict_varies)
    sum_andro = sum(dict_andro)
    
    size=[sum_varies,sum_andro]
    Android_Ver = ['Varying', 'Not varying']
    
    figure1 = plt.Figure(figsize=(5,4), dpi=80)
    
    color = cm.rainbow(np.linspace(0, 1, 10))
    #fig1, ax1 = plt.subplots()
    ax3 = figure1.add_subplot(111)
    ax3.pie(size, labels=Android_Ver,colors = color, autopct='%1.1f%%', startangle=200)
    ax3.set_title("""% download of Varying Android \n
                    version vs Non-varying Android Ver in dataset""",fontsize=10)
    #ax3.xlim(0,3.0)
    pie_plot = FigureCanvasTkAgg(figure1, big_frame) 
    pie_plot.get_tk_widget().place(x=0,y=0)
    #ax3.legend(loc=0) 
    
    figure1 = plt.Figure(figsize=(5,3), dpi=80)
    count = [len(dict_varies),len(dict_andro)]
    color = cm.rainbow(np.linspace(0, 1, 2))
    #fig1, ax1 = plt.subplots()
    ax2 = figure1.add_subplot(111)
    ax2.pie(count, labels=Android_Ver,colors = color, autopct='%1.1f%%', startangle=200)
    ax2.set_title("Frequency Varying Android version vs Non-varying Android Ver in dataset",fontsize=9)
    #ax3.xlim(0,3.0)
    pie_plot = FigureCanvasTkAgg(figure1, big_frame) 
    pie_plot.get_tk_widget().place(x=100,y=300)
    #ax3.legend(loc=0) 
    
    String ="""
    Given DataSet consist wide range of applications,
    With different Android Versions outof which only 
    12.5% Applications Have varying Android Version
    """
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=310,y=60)
    String ="""
    Frequency of Varying Android Version is lesser in the data set but
    their total download is higher than the Applications with other Android version
    This shows that Application with Varying android version has chance to get higher downloads
    """
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=510)

    root.mainloop()
    


"""Ques 7 END===================================================================================================================="""



def reviewClick():
    global screen
    import review as rev
    rev.startingScreen(screen)

def overviewClick():
    global screen
    import main as over
    over.startingScreen(screen)

    
def machineClick(event):
    global screen 
    import InsightsDesignForMachineLearningModels as mac
    mac.startingScreen(screen)
    
def categoryClick():
    global screen
    import catgory as cat
    cat.startingScreen(screen)

def installClick():
    global screen
    import install as inst
    inst.startingScreen(screen)
    
def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)

def dataInserteClick():
    global screen
    import DesignToInsertData as did 
    did.startingScreen(screen)

def searchAppClick(event):
    global screen
    import InsightsDesignForSearchApp as app
    app.startingScreen(screen)


def sizeClick(event):
    print('')

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def int_menubar(screen):
    menubar = Menu(screen)
    
    homemenu = Menu(menubar, tearoff = 0)
    menubar.add_command(label = "Home",command=overviewClick)
    
    categorymenu = Menu(menubar, tearoff = 0)
    categorymenu.add_separator()
    categorymenu.add_command(label = "category", command =categoryClick)
    menubar.add_cascade(label = "Category", menu = categorymenu)
    
    installmenu = Menu(menubar, tearoff=0)
    installmenu.add_command(label = "install", command = installClick)
    installmenu.add_separator()
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

def startingScreen(root):
    global screen,df
    
    df=pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    
    root.destroy()
    screen = tk.Tk()
    int_menubar(screen)
    adjustWindow(screen)
    screen.title("Install of App")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="INSTALLS",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
                          
    
    big_frame = tk.Frame(screen,bg='#F8E0E0',width='1520',height='730',bd=4,relief=RIDGE)
    big_frame.place(x=3,y=100)
    
    """
    1) What is the percentage download in each category on the playstore.

    2) How many apps have managed to get the following number of downloads
	a) Between 10,000 and 50,000
	b) Between 50,000 and 150000
	c) Between 150000 and 500000
	d) Between 500000 and 5000000
	e) More than 5000000

    7)All those apps , whose android version is not an issue and can work with varying devices , what is the percentage increase or decrease in the downloads.

    """
    q1 = tk.Label(big_frame,text = "Percentage download for each category on the playstore.",width=55,height=8,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q1.bind("<Button-1>", function_q1)
    q1.place(x=50,y=10)
    q2str='''
          Apps Installs
a) Between 10,000 and 50,000
 b) Between 50,000 and 150000
  c) Between 150000 and 500000
    d) Between 500000 and 5000000
    e) More than 5000000'''
    q2 = tk.Label(big_frame,text =q2str ,width=55,height=8,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q2.bind("<Button-1>", function_q2)
    q2.place(x=660,y=10)
    #function_q11(frame1)
    
    q7 = tk.Label(big_frame,text = '''All those apps , whose android version is not an issue  \n and can work with varying devices ,what is the percentage increase \n or decrease  in the downloads.''',width=55,height=7,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q7.bind("<Button-1>", function_q7)
    q7.place(x=50,y=230)       
    
    q10 = tk.Label(big_frame,text = "Question 10 Teen Vs Mature 17+",width=55,height=7,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q10.bind("<Button-1>", function_q10)
    q10.place(x=660,y=230)       
    
    q3str='''
          Number of Installs for the following App Sizes
a) Size between 10 and 20 mb
 b) Size between 20 and 30 mb
  c) More than 30 mb'''
    q3 = tk.Label(big_frame,text =q3str ,width=55,height=7,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q3.bind("<Button-1>", function_q3)
    q3.place(x=410,y=425)

    screen.mainloop()
    
#startingScreen(tk.Tk())
