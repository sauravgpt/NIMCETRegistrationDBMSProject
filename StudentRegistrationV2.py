# from tkinter import *
import webbrowser
import sqlite3
from tkinter import Button, Entry, IntVar, Label, OptionMenu, Radiobutton, StringVar, Tk, Toplevel


root = Tk()
root.geometry('640x600')
root.title("Exam Registration Form")
conn = sqlite3.connect('Registration.db')

firstN = StringVar()
lastN = StringVar()
gender = StringVar()
DOB = StringVar()
add1 = StringVar()
add2 = StringVar()
city = StringVar()
pincode = IntVar()
state = StringVar()
country = StringVar()
email = StringVar()
category = StringVar()
nationality = StringVar()


def isVerified():
    print("Inside Verified")
    if firstN.get() == "" or gender.get() == "" or add1.get() == "" or DOB.get() == "" or city.get() == "" or pincode.get() == 0 or state.get() == "" or email.get() == "" or category.get() == "" or nationality.get() == "" or country.get() == "Please Select":
        return 0
    else:
        return 1


def Update():
    if isVerified() == 0:
        Label(root, text="All fields are mandatory to update").place(x=20, y=450)
    else:
        name = firstN.get() + " " + lastN.get()
        Gender = gender.get()
        dob = DOB.get()
        completeAddress = add1.get() + " " + add2.get()
        City = city.get()
        Pincode = pincode.get()
        State = state.get()
        Country = country.get()
        Email = email.get()
        Category = category.get()
        Nationality = nationality.get()

        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT email FROM Student WHERE email=?", (email.get(),))
            rows = cursor.fetchall()
            print(rows[0][0])
            print(Email)
            if rows[0][0] == Email:
                query = """UPDATE Student SET fullName=?, Gender=?, dateOfBirth=?, address=?, city=?, pincode=?, state=?, country=?, category=?, nationality=? WHERE email=?"""
                data = (name, Gender, dob, completeAddress, City,
                        Pincode, State, Country, Category, Nationality, Email)
                cursor.execute(query, data)
                conn.commit()
                print('Record Updated Successfully')
            else:
                Label(root, text="Email provided does not exists           ",).place(
                    x=20, y=450)

def deleteRecord():
    curr = conn.cursor()
    curr.execute("DELETE FROM Student WHERE email=?", (email.get(),))
    conn.commit()

def retrieveWindow():
    retrieveWin = Toplevel(root)
    retrieveWin.geometry('400x400')
    cur = conn.cursor()
    Em = email.get()

    cur.execute("SELECT *FROM Student WHERE email=?", (email.get(),))
    rows = cur.fetchall()
    if(len(rows) == 0):
        Label(
            retrieveWin, text="Email WRONG/NOT FOUND").place(x=40, y=40)
    else:
        Label(retrieveWin, text="Your Details:").place(x=30, y=10)
        Label(retrieveWin, text="Name:    " + rows[0][0]).place(x=20, y=25)
        gen = ""
        if rows[0][1] == "M":
            gen = "Male"
        else:
            gen = "Female"
        Label(retrieveWin, text="Gender:      " + gen).place(x=20, y=40)
        Label(retrieveWin, text="DOB:     " + rows[0][2]).place(x=20, y=55)
        Label(retrieveWin, text="Address  :  ").place(x=20, y=79)
        Label(retrieveWin, text=rows[0][3]).place(x=30, y=94)
        Label(retrieveWin, text=rows[0][4]).place(x=30, y=110)
        Label(retrieveWin, text=rows[0][5]).place(x=70, y=110)
        Label(retrieveWin, text=rows[0][6]).place(x=30, y=125)
        Label(retrieveWin, text=rows[0][7]).place(x=70, y=125)
        Label(retrieveWin, text="Email:       " +
                rows[0][8]).place(x=30, y=140)
        Label(retrieveWin, text="Category:        " +
                rows[0][9]).place(x=30, y=155)
        if rows[0][10] == "IN":
            cat = "India"
        else:
            cat = "Foriegn Country"
        Label(retrieveWin, text="Nationality:     " + cat).place(x=30, y=172)
        Button(retrieveWin, text='Delete', width=20, bg='red', fg='white', command=deleteRecord).place(x=70, y=210)
    conn.commit()


def database():
    x = isVerified()
    if x == 0:
        Label(root, text="All fields are mandatory to submit",).place(x=20, y=450)
    else:
        name = firstN.get() + " " + lastN.get()
        Gender = gender.get()
        dob = DOB.get()
        completeAddress = add1.get() + " " + add2.get()
        City = city.get()
        Pincode = pincode.get()
        State = state.get()
        Country = country.get()
        Email = email.get()
        Category = category.get()
        Nationality = nationality.get()

        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student (fullName TEXT, Gender TEXT, dateOfBirth DOB, address TEXT, city TEXT, pincode NUMBER, state TEXT, country TEXT, email TEXT, category TEXT, nationality TEXT);')
        cursor.execute('INSERT INTO Student (fullName, Gender, dateOfBirth, address, city, pincode, state, country, email, category, nationality) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                       (name, Gender, dob, completeAddress, City, Pincode, State, Country, Email, Category, Nationality))
        conn.commit()
        Label(root, text="Submitted Successfully                                     ").place(
            x=20, y=450)


Label(root, text="               NIMCET 2020 Registration form",
      font=("bold", 15)).place(x=100, y=10)
Label(root, text="1. Name in full (As per X Board)",
      font=("Ubuntu", 13)).place(x=10, y=60)

# First name
Label(root, text="First Name").place(x=30, y=82)
fName = Entry(root, bd=1, textvar=firstN)
fName.place(x=120, y=82)
# Last Name
Label(root, text="Last Name").place(x=30, y=102)
lName = Entry(root, bd=1, textvar=lastN)
lName.place(x=120, y=102)

# print(type(fullName))
# Gender
Label(root, text="2. Gender", font=("Ubuntu", 13)).place(x=10, y=122)
Radiobutton(root, text="Male", padx=5, variable=gender,
            value='M', font=("Ubuntu", 11)).place(x=190, y=122)
Radiobutton(root, text="Female", padx=20, variable=gender,
            value='F', font=("Ubuntu", 11)).place(x=270, y=122)

# DOB
Label(root, text="3. Date of birth (DD-MON-YY)",
      font=("Ubuntu", 13)).place(x=10, y=142)
date = Entry(root, text="DD", width=11, textvar=DOB)
date.place(x=270, y=142)

# Address
Label(root, text="4. Address", font=("Ubuntu", 13)).place(x=10, y=162)
Label(root, text="Address Line 1").place(x=30, y=182)
Label(root, text="Address Line 2").place(x=30, y=202)
Label(root, text="City").place(x=30, y=222)
Label(root, text="State").place(x=250, y=222)
Label(root, text="Pincode").place(x=30, y=242)
Label(root, text="Country").place(x=250, y=242)
Label(root, text="Email").place(x=30, y=262)
Label(root, text="5. Category", font=("Ubuntu", 13)).place(x=10, y=282)
Label(root, text="6. Nationality", font=("Ubuntu", 13)).place(x=10, y=305)


Entry(root, textvar=add1, width=50).place(x=120, y=182)
Entry(root, textvar=add2, width=50).place(x=120, y=202)
Entry(root, textvar=city).place(x=120, y=222)
Entry(root, textvar=pincode).place(x=120, y=242)
Entry(root, textvar=state).place(x=310, y=222)

countries = ["Argentina", "Australia", "Brazil", "Canada", "China", 'Germany', 'France', "India", "Indonesia", "Italy",
             "Japan", "Mexico", "the Russian Federation", "Saudi Arabia", "South Africa", "South Korea", "Turkey", "the UK", "the US"]
countryDropList = OptionMenu(root, country, *countries)
countryDropList.config(width=10)
countryDropList.place(x=310, y=242)
country.set('Please Select')

Entry(root, textvar=email, width=30).place(x=120, y=262)

Radiobutton(root, text="Gen", padx=20, variable=category,
            value='Gen', font=("Ubuntu", 11)).place(x=120, y=282)
Radiobutton(root, text="SC/ST", padx=20, variable=category,
            value='SC/ST', font=("Ubuntu", 11)).place(x=220, y=282)
Radiobutton(root, text="BC", padx=20, variable=category,
            value='BC', font=("Ubuntu", 11)).place(x=320, y=282)
Radiobutton(root, text="OBC", padx=20, variable=category,
            value='OBC', font=("Ubuntu", 11)).place(x=420, y=282)
Radiobutton(root, text="Disabled", padx=20, variable=category,
            value='Disable', font=("Ubuntu", 11)).place(x=520, y=282)

Radiobutton(root, text="Indian", padx=20, variable=nationality,
            value='IN', font=("Ubuntu", 11)).place(x=120, y=302)
Radiobutton(root, text="Foreign National", padx=20, variable=nationality,
            value='NOTIN', font=("Ubuntu", 11)).place(x=220, y=302)


Button(root, text='Submit', width=20, bg='brown',
       fg='white', command=database).place(x=30, y=380)
Button(root, text='Update', width=20, bg='brown',
       fg='white', command=Update).place(x=200, y=380)
Entry(root, textvar=email, width=30).place(x=30, y=420)
Button(root, text='Retrieve', width=20, bg='brown',
       fg='white', command=retrieveWindow).place(x=220, y=420)


def openLink():
    webbrowser.open(
        'https://github.com/sauravgpt/NIMCETRegistrationDBMSProject/blob/master/StudentRegistration.py')


Button(root, text='Source code on GitHub', width=35, bg='blue',
       fg='white', command=openLink).place(x=360, y=500)

root.mainloop()
