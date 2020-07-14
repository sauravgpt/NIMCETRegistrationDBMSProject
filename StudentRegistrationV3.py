import webbrowser
import sqlite3
from tkinter import Button, Entry, IntVar, Label, OptionMenu, Radiobutton, StringVar, Tk, Toplevel, END


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
passwd = StringVar()

def getData():
    fname = firstN.get()
    lname = lastN.get()
    Gender = gender.get()
    dob = DOB.get()
    Add1 = add1.get()
    Add2 = add2.get()
    City = city.get()
    Pincode = pincode.get()
    State = state.get()
    Country = country.get()
    Email = email.get()
    Category = category.get()
    Nationality = nationality.get()
    Password = passwd.get()

    data = [fname, lname, Gender, dob, Add1, Add2, City,
            Pincode, State, Country, Email, Category, Nationality, Password]
    return data


def clearForm():
    firstN.set('')
    lastN.set('')
    gender.set('')
    DOB.set('')
    add1.set('')
    add2.set('')
    city.set('')
    pincode.set(0)
    state.set('')
    country.set('Please Select')
    email.set('')
    category.set('')
    nationality.set('')
    passwd.set('')


def isVerified():
    print("Inside Verified")
    datas = getData()
    for data in datas:
        print(data)
    if len(firstN.get()) == 0 or len(gender.get()) == 0 or len(add1.get()) == 0 or len(DOB.get()) == 0 or len(city.get()) == 0 or pincode.get() == 0 or len(state.get()) == 0 or len(email.get()) == 0 or len(category.get()) == 0 or len(nationality.get()) == 0 or country.get() == "Please Select" or len(passwd.get()) == 0:
        print('all not filled')
        return 0
    else:
        print('all filled')
        return 1


def Update(retrieveWin):
    oldData = fetchData()
    fName.delete(0, END)
    fName.insert(0, oldData[0])
    lName.delete(0, END)
    lName.insert(0, oldData[1])
    date.delete(0, END)
    date.insert(0, oldData[3])
    A1.delete(0, END)
    A1.insert(0, oldData[4])
    A2.delete(0, END)
    A2.insert(0, oldData[5])
    A3.delete(0, END)
    A3.insert(0, oldData[6])
    A4.delete(0, END)
    A4.insert(0, oldData[7])
    A5.delete(0, END)
    A5.insert(0, oldData[8])
    Label(retrieveWin, text="Go back to update",).place(x = 30, y = 300)


def deleteRecord():
    curr = conn.cursor()
    curr.execute("DELETE FROM Student WHERE email=?", (email.get(),))
    clearForm()
    conn.commit()

def fetchData():
    cur = conn.cursor()
    cur.execute("SELECT *FROM Student WHERE email=? and passwd=?", (email.get(),passwd.get(),))
    rows = cur.fetchall()
    if(len(rows) == 0):
        return -1
    fname = rows[0][0]
    lname = rows[0][1]
    Gender = rows[0][2]
    dob = rows[0][3]
    Add1 = rows[0][4]
    Add2 = rows[0][5]
    City = rows[0][6]
    Pincode = rows[0][7]
    State = rows[0][8]
    Country = rows[0][9]
    Email = rows[0][10]
    Category = rows[0][11]
    Nationality = rows[0][12]
    Password = rows[0][13]

    data = [fname, lname, Gender, dob, Add1, Add2, City,Pincode, State, Country, Email, Category, Nationality, Password]
    return data

def retrieveUtil():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student WHERE email=?", (email.get(),))
    fetchedEmail = cur.fetchall()
    conn.commit()
    if len(fetchedEmail) == 0 and len(passwd.get()) == 0:
        Label(root, text="Email not matched                                     ").place(x=20, y=500)
    else:
        data = fetchData()
        if data == -1:
            Label(root, text="Wrong Password                                     ").place(x=20, y=500)
        else:
            Label(root, text="                                          ").place(x=20, y=500)
            retrieveWindow(data)
        

def retrieveWindow(data):
    retrieveWin = Toplevel(root)
    retrieveWin.geometry('400x400')
    L1 = Label(retrieveWin, text="Your Details:")
    L1.place(x=30, y=10)
    L2 = Label(retrieveWin, text="Name:    " + data[0] + ' ' + data[1])
    L2.place(x=20, y=25)
    gen = ""
    if data[2] == "M":
        gen = "Male"
    else:
        gen = "Female"
    L3 = Label(retrieveWin, text="Gender:      " + gen)
    L3.place(x=20, y=40)
    L4 = Label(retrieveWin, text="DOB:     " + data[3])
    L4.place(x=20, y=55)
    L5 = Label(retrieveWin, text="Address  :  ")
    L5.place(x=20, y=79)
    L6 = Label(retrieveWin, text=data[4])
    L6.place(x=30, y=94)
    L7 = Label(retrieveWin, text=data[5])
    L7.place(x=30, y=110)
    L8 = Label(retrieveWin, text=data[6])
    L8.place(x=70, y=110)
    L9 = Label(retrieveWin, text=data[7])
    L9.place(x=30, y=125)
    L10 = Label(retrieveWin, text=data[8])
    L10.place(x=70, y=125)
    L11 = Label(retrieveWin, text="Email:       " + data[10])
    L11.place(x=30, y=140)
    L12 = Label(retrieveWin, text="Category:        " + data[11])
    L12.place(x=30, y=155)
    if data[12] == "IN":
        cat = "India"
    else:
        cat = "Foriegn Country"
    L13 = Label(retrieveWin, text="Nationality:     " + cat)
    L13.place(x=30, y=172)
    Button(retrieveWin, text='Delete', width=20, bg='brown', fg='white', command=deleteRecord).place(x=40, y=210)
    Button(retrieveWin, text='Update', width=20, bg='brown', fg='white', command=lambda: Update(retrieveWin)).place(x=190, y=210)
    Button(retrieveWin, text='Back', width=20, bg='brown', fg='white', command=retrieveWin.destroy).place(x=210, y=250)
    conn.commit()


def database():
    x = isVerified()
    L = Label(root, text="All fields are mandatory to submit",)
    if x == 0:
        L.place(x=20, y=500)
    else:
        L = Label(root, text="",)
        data = getData()

        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student (fName TEXT, lName TEXT, Gender TEXT, dateOfBirth DOB, add1 TEXT, add2 TEXT, city TEXT, pincode NUMBER, state TEXT, country TEXT, email TEXT, category TEXT, nationality TEXT, passwd TEXT);')
        cursor.execute("SELECT email FROM Student WHERE email=? and passwd=?", (email.get(),passwd.get(),))
        fetchedEmail = cursor.fetchall()
        if(len(fetchedEmail) != 0):
            query = """UPDATE Student SET fName=?, lName=?, Gender=?, dateOfBirth=?, add1=?, add2=?, city=?, pincode=?, state=?, country=?, category=?, nationality=? WHERE email=?"""
            data = (data[0],  data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[11], data[12], data[10])
            cursor.execute(query, data)
            conn.commit()
            Label(root, text="Updated Successfully                                     ").place(x=20, y=500)
        else:
            cursor.execute('INSERT INTO Student (fName, lName, Gender, dateOfBirth, add1, add2, city, pincode, state, country, email, category, nationality, passwd) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                        (data[0],  data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13]))
            conn.commit()
            Label(root, text="Submitted Successfully                                     ").place(x=20, y=500)
        clearForm()


Label(root, text="               NIMCET 2020 Registration form", font=("bold", 15)).place(x=100, y=10)
Label(root, text="1. Name in full (As per X Board)", font=("Ubuntu", 13)).place(x=10, y=60)

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
Radiobutton(root, text="Male", padx=5, variable=gender, value='M', font=("Ubuntu", 11)).place(x=190, y=122)
Radiobutton(root, text="Female", padx=20, variable=gender, value='F', font=("Ubuntu", 11)).place(x=270, y=122)

# DOB
Label(root, text="3. Date of birth (DD-MON-YY)",
      font=("Ubuntu", 13)).place(x=10, y=142)
date = Entry(root, width=11, textvar=DOB)
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


A1 = Entry(root, textvar=add1, width=50)
A1.place(x=120, y=182)
A2 = Entry(root, textvar=add2, width=50)
A2.place(x=120, y=202)
A3 = Entry(root, textvar=city)
A3.place(x=120, y=222)
A4 = Entry(root, textvar=pincode)
A4.place(x=120, y=242)
A5 = Entry(root, textvar=state)
A5.place(x=310, y=222)

countries = ["Argentina", "Australia", "Brazil", "Canada", "China", 'Germany', 'France', "India", "Indonesia", "Italy",
             "Japan", "Mexico", "the Russian Federation", "Saudi Arabia", "South Africa", "South Korea", "Turkey", "the UK", "the US"]
countryDropList = OptionMenu(root, country, *countries)
countryDropList.config(width=10)
countryDropList.place(x=310, y=242)
country.set('Please Select')

Entry(root, textvar=email, width=30,).place(x=120, y=262)

Radiobutton(root, text="Gen", padx=20, variable=category, value='Gen', font=("Ubuntu", 11)).place(x=120, y=282)
Radiobutton(root, text="SC/ST", padx=20, variable=category, value='SC/ST', font=("Ubuntu", 11)).place(x=220, y=282)
Radiobutton(root, text="BC", padx=20, variable=category, value='BC', font=("Ubuntu", 11)).place(x=320, y=282)
Radiobutton(root, text="OBC", padx=20, variable=category, value='OBC', font=("Ubuntu", 11)).place(x=420, y=282)
Radiobutton(root, text="Disabled", padx=20, variable=category, value='Disable', font=("Ubuntu", 11)).place(x=520, y=282)

Radiobutton(root, text="Indian", padx=20, variable=nationality, value='IN', font=("Ubuntu", 11)).place(x=120, y=302)
Radiobutton(root, text="Foreign National", padx=20, variable=nationality, value='NOTIN', font=("Ubuntu", 11)).place(x=220, y=302)


Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=30, y=380)
Entry(root, textvar=email, width=30).place(x=30, y=420)
Entry(root, textvar = passwd, width=10).place(x=30, y=460)
Label(root, text='Password').place(x=100, y=460)
Button(root, text='Retrieve', width=20, bg='brown', fg='white', command=retrieveUtil).place(x=220, y=420)
Button(root, text='Clear', width=20, bg='brown', fg='white', command=clearForm).place(x=180, y=380)


def openLink():
    webbrowser.open('https://github.com/sauravgpt/NIMCETRegistrationDBMSProject/edit/master/StudentRegistrationV2.py')


Button(root, text='Source code on GitHub', width=35, bg='blue', fg='white', command=openLink).place(x=360, y=500)

root.mainloop()
