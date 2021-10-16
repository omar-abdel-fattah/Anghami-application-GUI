
# import the needed libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Tk
from PIL import Image, ImageTk
import pandas as pd
from csv import writer

# define the global lists
users=[]
all_songs=[]
all_songs_names=[]

class user(object):
    songs=[]
    def __init__(self,first,last,username,password):  # user class constructor
        self.first=first
        self.last=last
        self.username=username
        self.password=password
    def __init__(self):
        print("xxx")
    def add_song(self,song):  # function to add songs to user
        self.songs.append(song)
	

    def disp_data(self):  # function to display all user info
        data = self.first + "\t" + self.last + "\t" + self.username + "\t" + "\n"
        print(data)
        for obj in self.songs:
            print(obj.name)


class song(object):
    def __init__(self,name,mp4):
        self.name=name
        self.mp4=mp4





def Signin() : # sign-in page

    def get_object(username, password):  # a function to return the object after searching in the ysers lists by password and user name

        for obj in users:
            if str(obj.password) == str(password) and str(obj.username) == str(username):
                return obj
        return 0

    def next(username,password): 

        curr_user=get_object(username,password)

	#if no data is entered 
        if curr_user==0:
            print("error try again")
            entry1.delete(0, 20)
            entry2.delete(0,20)
        else:
		#check the checkbutton state is pressed
            if state.get()==1:
                master.destroy()   #destroy the sign-in page
                welcome_page(curr_user)  # run welcome page for the current user



# intialize a starting page
    master = Tk()
    image = Image.open("angh.jpg")  # add image 
    image = image.resize((298, 100)) # resize image
    test = ImageTk.PhotoImage(image)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0, y=75)
    state = IntVar()
    master.title("SignIn page")  # add title
    master.minsize(width=300, height=300)   # set size of page
    master.configure(bg='purple')
    label1 = Label(master, text="username")
    label2 = Label(master, text="password")
    username=tk.StringVar()
    passw=tk.StringVar()
    entry1 = ttk.Entry(master, textvariable=username)
    entry2 = ttk.Entry(master, textvariable=passw, show='*')
    label1.grid(row=0, sticky=E)
    label2.grid(row=1, sticky=E)
    c = Checkbutton(master, text="I am not a robot",variable=state)
    c.grid(columnspan=2)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    d = Button(master, text="Sign in", command=lambda: [next(username.get(),passw.get())],
               font=('Helvetica bold', 20), bg="grey")  # set a button functions to be done in case triggered
    d.place(x=100, y=190)  


# welcome page
def welcome_page(user1):
	#intialize the page
    master = Tk()
    master.minsize(width=300, height=300)
    master.configure(bg='purple')
    master.title("Anghami Plus")
    label1 = Label(master, text="Welcome "+user1.first +" "+user1.last , font=('Helvetica bold',20), bg='purple', fg="white")
    label1.place(x=30, y=10)
    image = Image.open("angh.jpg")
    image = image.resize((300, 100))
    test = ImageTk.PhotoImage(image)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0, y=60)
    
#intialize the buttons and setting the events functions to be executed
    c = Button(master, text="Add song", command=lambda: [master.destroy(), song_page(user1)],
               font=('Helvetica bold', 15), bg="grey") 
    c.place(x=100, y=190)
    b = Button(master, text="LOG OUT", command=lambda: [master.destroy(), main()],
               font=('Helvetica bold', 15), bg="grey")
    b.place(x=100, y=250)

# Signup page
def Signup():
	#intialize the page settings and labels and buttons
    master = Tk()
    master.minsize(width=300, height=300)
    master.title("SignUP page")
    master.configure(bg='purple')
    passw=tk.StringVar()
    first = tk.StringVar()
    last = tk.StringVar()
    username = tk.StringVar()
    label1 = Label(master, text="First name", font=('Helvetica bold', 15), bg='purple', fg="white")
    label2 = Label(master, text="Last name", font=('Helvetica bold', 15), bg='purple', fg="white")
    label3 = Label(master, text="Username", font=('Helvetica bold', 15), bg='purple', fg="white")
    label4 = Label(master, text="Password", font=('Helvetica bold', 15), bg='purple', fg="white")
    entry1 = ttk.Entry(master,textvariable=first)  # first textbox
    entry2 = ttk.Entry(master,textvariable=last)
    entry3 = ttk.Entry(master,textvariable=username) # fourth textbox
    entry4 = ttk.Entry(master,textvariable=passw,show='*')
    label1.grid(row=0, sticky=E)
    label2.grid(row=1, sticky=E)
    label3.grid(row=2, sticky=E)
    label4.grid(row=3, sticky=E)
    user1= user()
    state = IntVar()
	#Set the user data to be as set by him/her
    def set_data(user1):

        user1.password=passw.get()
        user1.last=last.get()
        user1.username=username.get()
        user1.first=first.get()
        users.append(user1)
        for obj in users:
            obj.disp_data()
	#add image and resize it
    image = Image.open("angh.jpg")
    image = image.resize((300, 100))
    test = ImageTk.PhotoImage(image)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0, y=200)
    c = Checkbutton(master, text="I agree to Terms & Conditions", bg='purple', font=('Helvetica bold', 15),variable=state)
    c.grid(columnspan=2)
    print(state.get())
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    b = Button(master, text="Sign up", command=lambda: [master.destroy(),set_data(user1),welcome_page(user1)], font=('Helvetica bold', 20),
               bg="grey")
    b.grid(row=25, column=1)
    b.place(x=100, y=145)


def get_songs():
    user_list = []

    df = pd.read_csv("songs.csv")
    for row in range(0, len(df.index)):
        user_list = list(df.loc[row])
        temp_song = song(user_list[0], user_list[1])
        all_songs.append(temp_song)
        user_list.clear()
    for a in all_songs:
        print(a.mp4)
    for obj in all_songs:
        all_songs_names.append(obj.name)
def identify_song(name):
    for obj in all_songs:
        if obj.name == name:
            return obj
def song_page(user1):
    # this is a function which returns the selected combo box item
    def getSelectedComboItem():
        return box.get()

    # this is the function called when the button is clicked
    def add_func():

        user1.add_song(identify_song(selected_song.get()))
        user1.disp_data()

    # this is the function called when the button is clicked
    def done_func():
        root.destroy()
        main()

    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('300x346')
    root.configure(background='#CD00CD')
    root.title('Songs')
    selected_song = tk.StringVar()
    # This is the section of code which creates a combo box
    box = ttk.Combobox(root, values=all_songs_names, font=('arial', 12, 'normal'),textvariable=selected_song, width=20)
    box.place(x=21, y=193)
    box.current(1)

    # This is the section of code which creates a button
    Button(root, text='Add', bg='#CDC1C5', font=('arial', 12, 'normal'), command=add_func).place(x=49, y=238)

    # This is the section of code which creates a button
    Button(root, text='Done!', bg='#CDC1C5', font=('arial', 12, 'normal'), command=done_func).place(x=142, y=238)

    # This is the section of code which creates the a label
    Label(root, text='Choose your fav Songs', bg='#CD00CD', font=('arial', 12, 'normal')).place(x=55, y=154)

    # First, we create a canvas to put the picture on


    image = Image.open("angh.jpg")
    image = image.resize((298, 100))
    test = ImageTk.PhotoImage(image)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0, y=23)
    root.mainloop()





# main page
class main:
    def __init__(self):
        root= Tk()
        root.minsize(width=400,height=400)
        root.title("Anghami +")
        root.configure(bg='purple')
        label = Label(root, text="welcome to Anghami", bg="white", fg="black",font=('Helvetica bold',30))
        label.grid(row=0,column=1)
        label.place(x=10, y=10)
        label2 = Label(root, text="Free Music!Anytime..Anywhere", bg="white", fg="black",font=('Helvetica bold',15))
        label2.grid(row=1,column=1)
        label2.place(x=35,y=75)

        image=Image.open("angh.jpg")
        image=image.resize((400,120))
        test = ImageTk.PhotoImage(image)
        label1 = Label(image=test)
        label1.image = test
        label1.place(x=0,y=150)


        sign_in = Button(root, text="sign in",bg='grey', fg="black", command=lambda :[root.destroy(),Signin()],font=('Helvetica bold',15))
        sign_in.grid(row=10,column=1)
        sign_in.place(x=280, y=300)
        sign_up = Button(root, text="sign up",bg='grey', fg="black", command=lambda :[root.destroy(),Signup()],font=('Helvetica bold',15))
        sign_up.grid(row=10,column=2)
        sign_up.place(x=100,y=300)
        root.mainloop()

#main 

get_songs()
x=main()



