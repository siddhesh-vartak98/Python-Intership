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
from collections import Counter


def adjSmallwindow(window):
    w = 850 # width for the window size
    h = 790 # height for the window size
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




def function_q5(event):
        global screen 
        root = Toplevel(screen)
        big_frame = tk.Frame(root,bg='white',width='850',height='710',bd=4,relief=RIDGE)
        big_frame.place(x=25,y=60)
        #adjSmallwindow(root)
        w=850
        h=700
        ws=screen.winfo_screenwidth()
        hs=screen.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        root.geometry("%dx%d+%d+%d"%(w,h,x,y))
        
        root.configure(background='white')
       
        df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
        df=df.replace(np.NaN,-999)
        #df = df[df['Category'] != '1.9']
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
            
        for i in range(len(y_count)-1):
            for j in range(len(y_count)-1):
                if y_count[j]<y_count[j+1]:
                    y_count[j],y_count[j+1] = y_count[j+1],y_count[j]
                    x_label[j],x_label[j+1] = x_label[j+1],x_label[j]
        #colors
        #colors = ['#ff9999','#66b3ff','#99ff99']#,'#ffcc99']
        figure1 = plt.Figure(figsize=(6,6), dpi=100)
        
        color = cm.rainbow(np.linspace(2, 1, 10))
        #fig1, ax1 = plt.subplots()
        ax3 = figure1.add_subplot(111)
        ax3.barh(x_label, y_count,color = color)
        ax3.set_title("CHART ON TREND OF DOWNLOAD OVER THE CATEGORY")
        bar_plot = FigureCanvasTkAgg(figure1, big_frame) 
        bar_plot.get_tk_widget().place(x=100,y=0)
        ax3.set_xlabel("Downloads")
        #ax3.legend() 
    
        root.mainloop()

""" Ques 5 END=============================================================================================="""



""" Ques 3 START=============================================================================================="""
def qn3(category):
    global sample
    Installs = []
    sample.drop(index=10472,axis=0,inplace=True)
    sample=sample.replace(np.NaN,0)

    for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
            Installs.append(0)
        else:
            Installs.append(int(i.replace('+','').replace(',','')))
    ans=[]
    count = []
    
    for i in category:
        total=0
        c=0
        for j in range(len(sample['Category'])):
            if j!=10472:
                if sample['Category'][j]==i:
                    total=total+Installs[j]
                    c+=1
                    
        ans.append(total)
        count.append(c)
        
        
    cat,avg = [],[]    
    for index in range(len(ans)):
        cat.append(category[index])
        avg.append(round(ans[index]/count[index]))
    
    return  cat,avg

def function_q3(event):
    
    global screen,sample
    
    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='800',height='710',bd=4,relief=RIDGE)
    big_frame.place(x=25,y=60)
    w=850
    h=790
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.configure(background='white')
   
    """category=sample['Category'].unique()
    
    cat,avg = qn3(category)
    #print(len(cat))
    #print(len(avg))
    
    #print(cat[avg.index(max(avg))])
    #print(max(avg))
     
    #print(cat[avg.index(min(avg))])
    #print(min(avg)) 
    
    lowest = []
    for index in range(len(avg)):
        if avg[index]<250000:
            lowest.append(category[index])
        
    label = category
    val = avg
    
    color = cm.rainbow(np.linspace(0, 1, len(label)))
    figure2 = plt.Figure(figsize=(7,6), dpi=100)
    
    chart = figure2.add_subplot(111)
    
    bar_plot = chart.barh(label,val,color=color)
    
    chart.set_ylabel("Category")
    chart.set_xlabel("Average Installs")
    figure2.suptitle("Category with Their Average Download")
    chart.legend()
    
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=10,y=0)"""
    
    """String=
            There are 33 Unique Categories are available in the Data set where {} Category has 
            managed to get the Maximum Downloads across all the years and {} Category has got 
            the Lowest Downloads Accept {} and {} Category All the categories have managed to get 
            the average of 2,50,000 Downloads
    .format(cat[avg.index(max(avg))],cat[avg.index(min(avg))],lowest[0],lowest[1])"""
    dictionary = {
    "most": {},
    "least": {},
    "average": {}
    }
    average_installs = []
    df = df[df['Installs'] != 'Free']
    def get_average(count, category):
        if count > 250000:
            average_installs.append(category)

    df['Installs'] = df['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
    df['Installs'] = df['Installs'].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)
    df['Installs'] = df['Installs'].apply(lambda x: int(x))        
    # getting the set of installs
    installs = list(set(df.Installs))
    print(installs, '\n') # we can see that the minimum install is 0
    df_min_installs = df[df['Installs'] == 0]
    min_installs = list(set(df_min_installs.Category))
    String1= "The categories which have minimum installs are: ".format(min_installs)
    tk.Label(big_frame,text=String1,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=40)
    droplist = OptionMenu(big_frame, *min_installs)
    droplist.config(width=17)
    #anversion.set('--select andriod version--')
    droplist.place(x=600,y=40)
    
    df_max_installs = df[df['Installs'] == 500000000]
    max_installs = list(set(df_max_installs.Category))
    #print("The categories which have maximum installs are: ", '\n'.join(max_installs), '\n')
    tk.Label(big_frame,text="The categories which have maximum installs are:",font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=80)
    droplist = OptionMenu(big_frame, *max_installs)
    droplist.config(width=17)
    #anversion.set('--select andriod version--')
    droplist.place(x=600,y=80)
    
    df.apply(lambda row: get_average(row['Installs'], row['Category']), axis=1)
    #print("The categories which have atleast average installs are: ", '\n'.join(set(average_installs)))
    output = []  #get unique value 
    for x in average_installs:
        if x not in output:
            output.append(x)
    tk.Label(big_frame,text="The categories which have atleast average installs are: ",font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=140)
    droplist = OptionMenu(big_frame, *output)
    droplist.config(width=17)
    #anversion.set('--select andriod version--')
    droplist.place(x=600,y=140)
    
    #tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=565)
    
    root.mainloop()

""" Ques 3 END================================================================================================="""


"""Feature cat_download size START============================================================================="""
def feature_cat_size(event):
    
    global screen,df
    
    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='750',height='690',bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    w=800
    h=790
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    
    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    
    #print(df.head(5))
    
    
    # Data cleaning for "Size" column
    #print(df['Size'].head(5))
    """df['Size'] = df['Size'].map(lambda x: x.rstrip('M'))
    df['Size'] = df['Size'].map(lambda x: str(round((float(x.rstrip('k'))/1024), 1)) if x[-1]=='k' else x)
    df['Size'] = df['Size'].map(lambda x: np.nan if x.startswith('Varies') else x)
    #print(df['Size'].head(5))"""
    df["Size"] = df["Size"].apply(lambda x: str(x).replace(",", "") if "," in str(x) else x)
    df["Size"] = df["Size"].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    df["Size"] = df["Size"].apply(lambda x: str(x).replace("Varies with device", "NAN") if "Varies with device" in str(x) else x)
    df["Size"] = df["Size"].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)

    df = df[df["Size"] != '1000+']
    df=df.replace(np.NaN,-999)
    #print(df.isnull().sum())
    
    #print(df['Category'].unique())
    total = 0
    count=0
    dict_cat_size = {} 
    for index in range(len(df)):
            if df['Category'][index]==-999 or df['Size'][index]==-999 :
                continue
            if df['Category'][index] in dict_cat_size:
                dict_cat_size[df['Category'][index]][0]+=float(df['Size'][index])
                dict_cat_size[df['Category'][index]][1]+=1
            else:
                dict_cat_size[df['Category'][index]]=[float(df['Size'][index]),1]
    #print(dict_cat_size)
    
    for category in dict_cat_size:
        try:
            size = dict_cat_size[category][0]  
            count = dict_cat_size[category][1]
            dict_cat_size[category]=float(size/count)
        except:
            print('')
            
            
    #print(dict_cat_size)
            
            
    #print(len(dict_cat_size))
    
    x_label,y_count = [],[]
    
    for cat in dict_cat_size:
        x_label.append(cat)
        y_count.append(dict_cat_size[cat])
    
    colors = cm.rainbow(np.linspace(0, 1, len(x_label)))
    
    figure2 = plt.Figure(figsize=(9,7), dpi=80)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    bar_plot = chart.barh(x_label,y_count,color=colors)
    chart.set_ylabel("CATEGORY")
    chart.set_xlabel("Download size")
    figure2.suptitle('Download size per Category')
    chart.legend()

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=3,y=0)
    
    #'TRAVEL_AND_LOCAL,Family,game,sports 
    String="""
            The Google Play Store shows apps’ actual download sizes. 
            Game and Family app categories have the highest average download size,
            while TOOLS category is the smallest on average.
           """
           
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=50,y=520)
   
    root.mainloop()
    

"""Feature cat_download size END============================================================================="""

"""Feature cat_rev START============================================================================="""
def feature_cat_review(event):
    
    global screen,df
    
    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='750',height='690',bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    w=800
    h=790
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    
    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    
    df=df.replace(np.NaN,-999)

    dict_cat_review = {}
    for index in range(len(df)):
        
        if df['Category'][index]==-999:
            continue
        
        if df['Category'][index] in dict_cat_review:
            dict_cat_review[df['Category'][index]]+=df['Reviews'][index]
        else:
            dict_cat_review[df['Category'][index]]=df['Reviews'][index]
  
    y_count=[]
    x_label=[]
    for i in dict_cat_review:
        x_label.append(i)
        y_count.append(dict_cat_review[i])
        
    
    #print(y_count)
    
    colors = cm.rainbow(np.linspace(0, 1, len(x_label)))
    
    figure2 = plt.Figure(figsize=(9,7), dpi=80)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    bar_plot = chart.barh(x_label,y_count,color=colors)
    chart.set_ylabel("CATEGORY")
    chart.set_xlabel("COUNT OF TOTAL REVIEWS")
    figure2.suptitle('COUNT OF TOTAL REVIEW UNDER DIFFERENT CATEGORY')
    chart.legend()

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=3,y=0)
    
    String="""
           It looks like only a small number of users take the time to write 
           an app review.Our analysis has shown that users tend to leave more 
           reviews for apps in Games,Social,Communication and Family categories
           """
           
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=50,y=580)
   
    root.mainloop()
    

"""Feature cat_rev END============================================================================="""

""" Ques 4 START================================================================================================================================="""

def function_q4(event):
    """work not done"""
    global screen,df
    
    #df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='580',height='530',bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    w=700
    h=600
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    df = pd.read_csv(r"C:\Users\Dell1\Music\googleplaystore-App-data.csv")
    df=df.replace(np.NaN,-999)
    df = df[df['Category'] != '1.9']
    #print(df.isnull().sum())
    #print(df.head(5))
    categories = Counter(df.Category)
    #print(sorted(categories)) #for test
    average_ratings = []
    # grouping by categories and taking the sum of ratings
    sum_ratings = df.groupby('Category').sum()
    sum_ratings['Rating']['ART_AND_DESIGN']

    for category, rating in zip(sorted(categories), sum_ratings['Rating']):
        sum_ratings['Rating'][category] = rating / categories[category]
        average_ratings.append((category, sum_ratings['Rating'][category]))

    x_ticks = [k[0] for k in average_ratings]
    ratings = [k[1] for k in average_ratings]
    y_pos = np.arange(len(ratings))
    print(x_ticks)
    print(y_pos)
    # finding the maximum average
    highest_max_average_rating = sum_ratings['Rating'].idxmax() # the average shown is EDUCATION
    print("The category with highest maximum average rating is {} with rating {:.3f}".format(highest_max_average_rating, max(sum_ratings['Rating'])))
    #print(x_ticks, ratings) #for test
    figure3=plt.figure(figsize=(9,6))
    graph = plt.bar(x_ticks,ratings, align='center', alpha=0.6)
    plt.xticks(y_pos, x_ticks,rotation=45, horizontalalignment='right',fontweight='light')
    plt.gca().invert_yaxis()
    #plt.xlabel('CATEGORY')
    #plt.ylabel('rating count')
    #plt.savefig('Q4.png', bbox_inches='tight')
    #plt.show()

    
    #figure3 = plt.Figure(figsize=(7,4), dpi=80)
    ax3 = figure3.add_subplot(111)
    #ax3.scatter(y_count,x_label,color='r')
    scatter3 = FigureCanvasTkAgg(figure3, big_frame) 
    scatter3.get_tk_widget().place(x=1,y=0)
    #ax3.legend() 
    ax3.set_xlabel("CATEGORY")
    ax3.set_ylabel("RATING")
    ax3.set_title('CATEGORIES WITH HIGHEST MAXIMUM AVERAGE RATING')

    String = """
            There are Total 33 Unique categories are present in the data set 
            but out of {} Categories has managed to get the Highest Maximum 
            Average Rating of From the User
            Average Rating from given data set is {:.1f}
            """.format(len(xlabel),avg_rating)
            
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=300)
    
    root.mainloop()

""" Ques 4 END================================================================================================================================="""

def data():
    global frame
    
    for i in range(50):
       tk.Label(frame,text=i).grid(row=i,column=0)
       tk.Label(frame,text="my text"+str(i)).grid(row=i,column=1)
       tk.Label(frame,text="..........").grid(row=i,column=2)


def myfunction(event):
    global canvas
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)
def overviewClick():
    global screen
    import main as over
    over.main_screen()

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

def dataInserteClick():
    global screen
    import DesignToInsertData as did 
    did.startingScreen(screen)

    
def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)


def sizeClick(event):
    print("")


   
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
    mldmenu.add_command(label = "M L Model", command = None)
    menubar.add_cascade(label = "M L Model", menu = mldmenu)
        
    idatamenu = Menu(menubar, tearoff=0)
    idatamenu.add_command(label = "Insert Data", command = dataInserteClick)
    menubar.add_cascade(label = "Insert Data", menu = idatamenu)
    
    samenu = Menu(menubar, tearoff=0)
    samenu.add_command(label = "Serch App", command = None)
    menubar.add_cascade(label = "Serch App", menu = samenu)
        
    
    screen.config(menu = menubar)

def startingScreen(root):
    global screen,df,canvas_big_frame,frame
    
    df=pd.read_csv(r'C:\Users\Dell1\Music\googleplaystore-App-data.csv')
    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Catgory of App")
    int_menubar(screen)
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="CATEGORY",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()

                           
    big_frame=tk.Frame(screen,bg='#F8E0E0',width='1300',height='700',bd=4,relief=RIDGE)# to change background in category page
    big_frame.place(x=3,y=100)
    
    """
    4) Which category of apps have managed to get the highest maximum average ratings from the users.

    3) Which category of apps have managed to get the most,least and an average of 2,50,000 downloads atleast.

    """
    
    q4 = tk.Label(big_frame,text = "The apps that managed to get the highest \n maximum rating from the user.",width=60,height=7,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q4.bind("<Button-1>", function_q4)
    q4.place(x=50,y=10)
    
    
    feat_cat_rev = tk.Label(big_frame,text = "Category V/S Review",width=38,height=5,font=("Calibri",17,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    feat_cat_rev.bind("<Button-1>", feature_cat_review)
    feat_cat_rev.place(x=700,y=10)
    
    #function_q11(frame1)
    
    feat_cat_size = tk.Label(big_frame,text = "Category V/S Size",width=45,height=5,font=("Calibri",17,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    feat_cat_size.bind("<Button-1>", feature_cat_size)
    feat_cat_size.place(x=50,y=230)       
    
    q3 = tk.Label(big_frame,text = "Category of apps that managed to get most, \n least an average of 2,50,000 downloads.",width=50,height=7,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q3.bind("<Button-1>", function_q3)
    q3.place(x=700,y=230)       
    
    q5 = tk.Label(big_frame,text = "Category wise download trend for the data \n is available over the period.",width=60,height=8,font=("Calibri",13,'bold'),bd=10,fg='#fcb643',bg='#ffe9a1',relief=RIDGE)
    q5.bind("<Button-1>", function_q5)
    q5.place(x=50,y=440)       
    
    screen.mainloop()
    
#startingScreen(tk.Tk())
