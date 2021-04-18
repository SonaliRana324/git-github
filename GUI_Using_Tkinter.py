from tkinter import *
from db_practice import DBHelper





def call_db():

    #db = DBHelper()
    n = name.get()
    print(n)
    #g = gender.get()
    #p = phone.get()
    #a = address.get()
    #db.insert_into(n, g, p, a)


root = Tk()

root.geometry("600x700")
root.title("Dance Registration")
#label = Label(text= "Registration Form" ,bg = "black" , fg= "white", font="comicsansms 9 bold" ,padx= 3, pady = 3)
#label.grid

frame = Frame(root , borderwidth=2, bg="grey", relief=SUNKEN)
frame.grid(row = 0 , column = 0 , sticky = "ns")
#label2 = Label(root,text = "Register" , fg = "black")
#label2()


#variables

name = StringVar()
gender = StringVar()
phone = IntVar()
address = StringVar()

fullname = Label(frame, text = "Full Name" , fg = "Black")
fullname.grid(row = 0 , column = 0)
name_entry = Entry(frame, textvariable = name)
name_entry.grid(row = 1 , column = 0)

Gender = Label(frame , text = "Gender" , fg = "Black")
Gender.grid(row = 2 , column = 0)
gender_entry = Entry(frame, textvariable = gender)
gender_entry.grid(row = 3, column= 0)

Phone_no = Label(frame, text = "Phone No." , fg = "Black")
Phone_no.grid(row = 4 , column = 0)
phone_entry = Entry(frame, textvariable = phone)
phone_entry.grid( row= 5 , column = 0)

Addres = Label(frame, text = "Address" , fg = "Black")
Addres.grid(row = 6 , column = 0)
address_entry = Entry(frame, textvariable = address)
address_entry.grid(row = 7 , column = 0)

Button(text="Submit" , command = call_db).grid()














root.mainloop()