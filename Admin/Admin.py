import tkinter
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.ttk import *
from tkinter import *
import pymysql


class Admin:

    # Opens The Main Window
    def __init__(self):
        self.root = tk.Tk()

        self.root.configure(bg="sky blue")

        # Window Size
        self.root.geometry("480x360")

        # Title Name
        self.root.title("Greetings! ADMIN 🎉✨")

        # Greetings!
        self.labelGreetings = tk.Label(self.root, fg="red", text="Welcome!",
                                       font=('Times New Roman', 18))
        self.labelGreetings.pack(padx=20, pady=30)

        # Button for Managing Faculty
        self.buttonFaculty = tk.Button(self.root, fg="blue", text="Manage Faculty", font=(
            'Times New Roman', 18), command=self.window_faculty)
        self.buttonFaculty.pack(padx=10, pady=25)

        # Button for Managing Students
        self.buttonStudents = tk.Button(
            self.root, fg="blue", text="Manage Student", font=('Times New Roman', 18), command=self.window_student)
        self.buttonStudents.pack(padx=10, pady=25)

        # Button for Managing Accounts
        self.buttonStudents = tk.Button(
            self.root, fg="blue", text="Manage Accounts", font=('Times New Roman', 18), command=self.window_account)
        self.buttonStudents.pack(padx=10, pady=20)

        self.root.mainloop()

    # Function for Creating Manage Faculty Window
    def window_faculty(self):
        # Creates a new Window for Managing Faculty
        self.facultyWindow = tk.Toplevel()

        # Window Size for Faculty
        self.facultyWindow.geometry("800x640+300+0")

        # Title Name
        self.facultyWindow.title("Manage Faculty Accounts")

        self.facultyWindow.resizable(width=False, height=False)

        # Frame Design
        MainFrame = Frame(self.facultyWindow, bd=10, width=770,
                          height=700, relief=RIDGE, bg='sky blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770,
                           height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400,
                          padx=2, bg="sky blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600,
                           height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100,
                            height=400, padx=2, bg="sky blue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90,
                             height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        # Variables
        self.FacultyID = StringVar()
        self.FacultyUserID = StringVar()
        self.FacultySubject = StringVar()

        # Label Title
        self.labelTitle = Label(TitleFrame, font=(
            'arial', 40, 'bold'), text="Faculty Manager", bd=7, fg="blue")
        self.labelTitle.grid(row=0, column=0, padx=132)

        # Entry for ID
        self.id = Label(LeftFrame1, font=(
            'arial', 12, 'bold'), text="No", bd=7)
        self.id.grid(row=0, column=0, sticky=W, padx=5)
        self.entID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                           textvariable=self.FacultyID)
        self.entID.grid(row=0, column=1, sticky=W, padx=5)

        # Entry for FacultyID
        self.facultyID = Label(LeftFrame1, font=(
            'arial', 12, 'bold'), text="Faculty ID", bd=7)
        self.facultyID.grid(row=1, column=0, sticky=W, padx=5)
        self.entFacultyID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=self.FacultyUserID)
        self.entFacultyID.grid(row=1, column=1, sticky=W, padx=5)

        # Entry for Subject
        self.subject = Label(LeftFrame1, font=(
            'arial', 12, 'bold'), text="Subject", bd=7)
        self.subject.grid(row=2, column=0, sticky=W, padx=5)
        self.entSubject = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                textvariable=self.FacultySubject)
        self.entSubject.grid(row=2, column=1, sticky=W, padx=5)

        # Table TreeView
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.faculty_records = ttk.Treeview(LeftFrame, height=17, columns=("id", "user_id", "subject", "date_updated"),
                                            yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.faculty_records.heading("id", text="No")
        self.faculty_records.heading("user_id", text="Faculty ID")
        self.faculty_records.heading("subject", text="Subject")
        self.faculty_records.heading("date_updated", text="Date Updated")

        self.faculty_records['show'] = 'headings'

        self.faculty_records.column("id", width=70)
        self.faculty_records.column("user_id", width=100)
        self.faculty_records.column("subject", width=100)
        self.faculty_records.column("date_updated", width=70)

        self.faculty_records.pack(fill=BOTH, expand=1)

        # Use for putting the information into the entry when you click the data
        self.faculty_records.bind(
            "<ButtonRelease-1>", lambda event: self.facultyInfo(event))
        # Calls the facultyDisplay function to display the Data(s)
        self.facultyDisplay()

        # Buttons
        # For displaying data
        self.btnDisplay = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=0, height=2, command=self.facultyDisplay)
        self.btnDisplay.grid(row=0, column=0, padx=1)
        # For adding new faculty account
        self.btnAddNew = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.facultyAdd)
        self.btnAddNew.grid(row=1, column=0, padx=1)
        # For updating faculty account
        self.btnUpdate = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.facultyUpdate)
        self.btnUpdate.grid(row=2, column=0, padx=1)
        # For deleting faculty account
        self.btnDelete = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.facultyDelete)
        self.btnDelete.grid(row=3, column=0, padx=1)
        # For searching faculty account
        self.btnSearch = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.facultySearch)
        self.btnSearch.grid(row=4, column=0, padx=1)
        # For resetting the entry
        self.btnReset = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=0, height=2, command=self.facultyReset)
        self.btnReset.grid(row=5, column=0, padx=1)
        # For exiting the Faculty Manager
        self.btnExit = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=0, height=2, command=self.facultyExit)
        self.btnExit.grid(row=6, column=0, padx=1)

    # Function For Exiting Faculty
    def facultyExit(self):
        iExit = tkinter.messagebox.askyesno(
            "Faculty Manager Application", "Do you really want to exit?")
        if iExit > 0:
            self.facultyWindow.destroy()
            return

    # Reset all the inputs
    def facultyReset(self):
        self.entID.delete(0, END)
        self.entFacultyID.delete(0, END)
        self.entSubject.delete(0, END)

    # Add Faculty
    def facultyAdd(self):
        if self.FacultyID.get() == "" or self.FacultyUserID.get() == "" or self.FacultySubject.get() == "":
            tkinter.messagebox.showerror(
                "Faculty Manager Application", "Please Enter Correct Details")
        else:
            sqlCon = pymysql.Connect(
                host="localhost", user="root", password="", database="quiz_db")
            cur = sqlCon.cursor()
            cur.execute("INSERT INTO `faculty` (id, user_id, subject) VALUES (%s, %s, %s)", (
                self.FacultyID.get(),
                self.FacultyUserID.get(),
                self.FacultySubject.get()
            ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Faculty Manager Application", "Record Entered Successfully")
            self.facultyDisplay()
            self.facultyReset()

    # Function for displaying the faculty data(s)
    def facultyDisplay(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("SELECT * FROM `faculty`")
        result = cur.fetchall()
        if len(result) != 0:
            self.faculty_records.delete(*self.faculty_records.get_children())
            for row in result:
                self.faculty_records.insert('', END, values=row)
        sqlCon.commit()
        sqlCon.close()

    # Function for when you click a row, that row's data will be displayed on the entry
    def facultyInfo(self, event):
        viewInfo = self.faculty_records.focus()
        learnerData = self.faculty_records.item(viewInfo)
        row = learnerData['values']
        if len(row) > 0:
            self.FacultyID.set(row[0])
        if len(row) > 1:
            self.FacultyUserID.set(row[1])
        if len(row) > 2:
            self.FacultySubject.set(row[2])

    # This Function allows you to update the data
    def facultyUpdate(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("UPDATE faculty SET user_id = %s, subject = %s WHERE id = %s", (
            self.FacultyUserID.get(),
            self.FacultySubject.get(),
            self.FacultyID.get()
        ))
        sqlCon.commit()
        self.facultyDisplay()
        sqlCon.close()
        tkinter.messagebox.showinfo(
            "Faculty Manager Application", "Record Updated Successfully")

    # This function allows you to delete data
    def facultyDelete(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("DELETE from faculty where id=%s", self.FacultyID.get())
        sqlCon.commit()
        self.facultyDisplay()
        sqlCon.close()
        tkinter.messagebox.showinfo(
            "Faculty Manager Application", "Record Deleted Successfully")
        self.facultyReset()

    # Function for searching for faculty
    def facultySearch(self):
        try:
            sqlCon = pymysql.Connect(
                host="localhost", user="root", password="", database="quiz_db")
            cur = sqlCon.cursor()
            cur.execute("SELECT * FROM faculty where id=%s",
                        self.FacultyID.get())

            row = cur.fetchone()

            self.FacultyID.set(row[0])
            self.FacultyUserID.set(row[1])
            self.FacultySubject.set(row[2])

            sqlCon.commit()

        except:
            tkinter.messagebox.showinfo(
                "Faculty Manager Application", "No Such Record Found")
            self.facultyReset()
        sqlCon.close()

    # Function for Creating Manage Student Window
    def window_student(self):
        # Creates a new Window for Managing Students
        self.studentWindow = tk.Toplevel()

        # Window Size for Students
        self.studentWindow.geometry("800x640+300+0")

        # Title Name
        self.studentWindow.title("Manage Student Accounts")

        self.studentWindow.resizable(width=False, height=False)

        # Frame Design
        MainFrame = Frame(self.studentWindow, bd=10, width=770,
                          height=700, relief=RIDGE, bg='sky blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770,
                           height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400,
                          padx=2, bg="sky blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600,
                           height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100,
                            height=400, padx=2, bg="sky blue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90,
                             height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        # Variables
        self.StudentID = StringVar()
        self.StudentUserID = StringVar()
        self.StudentLevelSection = StringVar()

        # Label Title
        self.labelTitle = Label(TitleFrame, font=(
            'arial', 40, 'bold'), text="Student Manager", bd=7, fg="blue")
        self.labelTitle.grid(row=0, column=0, padx=132)

        # Entry for ID
        self.id = Label(LeftFrame1, font=(
            'arial', 12, 'bold'), text="No", bd=7)
        self.id.grid(row=0, column=0, sticky=W, padx=5)
        self.entID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                           textvariable=self.StudentID)
        self.entID.grid(row=0, column=1, sticky=W, padx=5)

        # Entry for FacultyID
        self.studentID = Label(LeftFrame1, font=(
            'arial', 12, 'bold'), text="Student ID", bd=7)
        self.studentID.grid(row=1, column=0, sticky=W, padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=self.StudentUserID)
        self.entStudentID.grid(row=1, column=1, sticky=W, padx=5)

        # Entry for Subject
        self.levelSection = Label(LeftFrame1, font=(
            'arial', 12, 'bold'), text="Section Level", bd=7)
        self.levelSection.grid(row=2, column=0, sticky=W, padx=5)
        self.entLevelSection = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                     textvariable=self.StudentLevelSection)
        self.entLevelSection.grid(row=2, column=1, sticky=W, padx=5)

        # Table TreeView
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=17,
                                            columns=("id", "user_id", "level_section", "date_updated"),
                                            yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("id", text="No")
        self.student_records.heading("user_id", text="Student ID")
        self.student_records.heading("level_section", text="Section Level")
        self.student_records.heading("date_updated", text="Date Updated")

        self.student_records['show'] = 'headings'

        self.student_records.column("id", width=70)
        self.student_records.column("user_id", width=100)
        self.student_records.column("level_section", width=100)
        self.student_records.column("date_updated", width=70)

        self.student_records.pack(fill=BOTH, expand=1)

        # Use for putting the information into the entry when you click the data
        self.student_records.bind(
            "<Button-1>", lambda event: self.studentInfo(event))
        # Calls the studentDisplay function to display the Data(s)
        self.studentDisplay()

        # Buttons
        # For displaying student data
        self.btnDisplay = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=0, height=2, command=self.studentDisplay)
        self.btnDisplay.grid(row=0, column=0, padx=1)
        # For adding new student data
        self.btnAddNew = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.studentAdd)
        self.btnAddNew.grid(row=1, column=0, padx=1)
        # For updating student data
        self.btnUpdate = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.studentUpdate)
        self.btnUpdate.grid(row=2, column=0, padx=1)
        # For deleting student data
        self.btnDelete = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.studentDelete)
        self.btnDelete.grid(row=3, column=0, padx=1)
        # For searching student data
        self.btnSearch = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.studentSearch)
        self.btnSearch.grid(row=4, column=0, padx=1)
        # For resetting the entries of student manager app
        self.btnReset = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=0, height=2, command=self.studentReset)
        self.btnReset.grid(row=5, column=0, padx=1)
        # For exiting the student manager app
        self.btnExit = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=0, height=2, command=self.studentExit)
        self.btnExit.grid(row=6, column=0, padx=1)

    # Function For Exiting Student Manager
    def studentExit(self):
        iExit = tkinter.messagebox.askyesno(
            "Student Manager Application", "Do you really want to exit?")
        if iExit > 0:
            self.studentWindow.destroy()
            return

    # Reset all the inputs
    def studentReset(self):
        self.entID.delete(0, END)
        self.entStudentID.delete(0, END)
        self.entLevelSection.delete(0, END)

    # Add student data
    def studentAdd(self):
        if self.StudentID.get() == "" or self.StudentUserID.get() == "" or self.StudentLevelSection.get() == "":
            tkinter.messagebox.showerror(
                "Student Manager Application", "Please Enter Correct Details")
        else:
            sqlCon = pymysql.Connect(
                host="localhost", user="root", password="", database="quiz_db")
            cur = sqlCon.cursor()
            cur.execute("INSERT INTO `students` (id, user_id, level_section) VALUES (%s, %s, %s)", (
                self.StudentID.get(),
                self.StudentUserID.get(),
                self.StudentLevelSection.get()
            ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Student Manager Application", "Record Entered Successfully")
            self.studentDisplay()
            self.studentReset()

    # Function for displaying the student data(s)
    def studentDisplay(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("SELECT * FROM `students`")
        result = cur.fetchall()
        if len(result) != 0:
            self.student_records.delete(*self.student_records.get_children())
            for row in result:
                self.student_records.insert('', END, values=row)
        sqlCon.commit()
        sqlCon.close()

    # Function for when you click a row, that row's data will be displayed on the entry
    def studentInfo(self, event):
        viewInfo = self.student_records.focus()
        learnerData = self.student_records.item(viewInfo)
        row = learnerData['values']
        if len(row) > 0:
            self.StudentID.set(row[0])
        if len(row) > 1:
            self.StudentUserID.set(row[1])
        if len(row) > 2:
            self.StudentLevelSection.set(row[2])

    # This Function allows you to update the student data
    def studentUpdate(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("UPDATE students SET user_id = %s, level_section = %s WHERE id = %s", (
            self.StudentUserID.get(),
            self.StudentLevelSection.get(),
            self.StudentID.get()
        ))
        sqlCon.commit()
        self.studentDisplay()
        sqlCon.close()
        tkinter.messagebox.showinfo(
            "Student Manager Application", "Record Updated Successfully")

    # This function allows you to delete a student data
    def studentDelete(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("DELETE from students where id=%s", self.StudentID.get())
        sqlCon.commit()
        self.studentDisplay()
        sqlCon.close()
        tkinter.messagebox.showinfo(
            "Student Manager Application", "Record Deleted Successfully")
        self.studentReset()

    # Allows you to search using student id
    def studentSearch(self):
        try:
            sqlCon = pymysql.Connect(
                host="localhost", user="root", password="", database="quiz_db")
            cur = sqlCon.cursor()
            cur.execute("SELECT * FROM students where id=%s",
                        self.StudentID.get())

            row = cur.fetchone()

            self.StudentID.set(row[0])
            self.StudentUserID.set(row[1])
            self.StudentLevelSection.set(row[2])

            sqlCon.commit()

        except:
            tkinter.messagebox.showinfo(
                "Student Manager Application", "No Such Record Found")
            self.studentReset()
        sqlCon.close()

        # Function for Creating Manage Student Window

    def window_account(self):
        # Creates a new Window for Managing Faculty
        self.accountWindow = tk.Toplevel()

        # Window Size for Faculty
        self.accountWindow.geometry("880x700+300+0")

        # Title Name
        self.accountWindow.title("Manage Accounts")

        self.accountWindow.resizable(width=False, height=False)

        # Frame Design
        MainFrame = Frame(self.accountWindow, bd=10, width=770, height=700, relief=RIDGE, bg='sky blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg="sky blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg="sky blue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        # Variables
        self.AccountID = StringVar()
        self.AccountName = StringVar()
        self.AccountType = StringVar()
        self.AccountUserName = StringVar()
        self.AccountPassword = StringVar()
        self.AccountStatus = StringVar()

        # Label Title
        self.labelTitle = Label(TitleFrame, font=('arial', 40, 'bold'), text="Account Manager", bd=7, fg="blue")
        self.labelTitle.grid(row=0, column=0, padx=132)

        # Entry for ID
        self.aid = Label(LeftFrame1, font=('arial', 12, 'bold'), text="ID", bd=7)
        self.aid.grid(row=0, column=0, sticky=W, padx=5)
        self.entaID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                            textvariable=self.AccountID)
        self.entaID.grid(row=0, column=1, sticky=W, padx=5)

        # Entry for Name
        self.aName = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Name", bd=7)
        self.aName.grid(row=1, column=0, sticky=W, padx=5)
        self.entaName = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                              textvariable=self.AccountName)
        self.entaName.grid(row=1, column=1, sticky=W, padx=5)

        # Entry for UserType
        self.aType = Label(LeftFrame1, font=('arial', 12, 'bold'), text="User Type", bd=7)
        self.aType.grid(row=2, column=0, sticky=W, padx=5)
        self.entaType = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=44, state='readonly',
                                     textvariable=self.AccountType)
        self.entaType['values'] = ('', '1', '2', '3')
        self.entaType.current(0)
        self.entaType.grid(row=2, column=1)

        # Entry for Username
        self.aUserName = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Username", bd=7)
        self.aUserName.grid(row=3, column=0, sticky=W, padx=5)
        self.entaUserName = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=self.AccountUserName)
        self.entaUserName.grid(row=3, column=1, sticky=W, padx=5)

        # Entry for Password
        self.aPassword = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Password", bd=7)
        self.aPassword.grid(row=4, column=0, sticky=W, padx=5)
        self.entaPassword = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=self.AccountPassword)
        self.entaPassword.grid(row=4, column=1, sticky=W, padx=5)

        # Entry for Status
        self.aStatus = Label(LeftFrame1, font=('arial', 12, 'bold'), text="User Status", bd=7)
        self.aStatus.grid(row=5, column=0, sticky=W, padx=5)
        self.entaStatus = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=44, state='readonly',
                                       textvariable=self.AccountStatus)
        self.entaStatus['values'] = ('', '0', '1')
        self.entaStatus.current(0)
        self.entaStatus.grid(row=5, column=1)

        # Table TreeView
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.account_records = ttk.Treeview(LeftFrame, height=17,
                                            columns=("id", "name", "user_type", "username", "password", "status",
                                                     "date_updated"),
                                            yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.account_records.heading("id", text="id")
        self.account_records.heading("name", text="Name")
        self.account_records.heading("user_type", text="User Type 2=Faculty 3=Student")
        self.account_records.heading("username", text="Username")
        self.account_records.heading("password", text="Password")
        self.account_records.heading("status", text="status")
        self.account_records.heading("date_updated", text="Date Updated")

        self.account_records['show'] = 'headings'

        self.account_records.column("id", width=70)
        self.account_records.column("name", width=100)
        self.account_records.column("user_type", width=100)
        self.account_records.column("username", width=100)
        self.account_records.column("password", width=100)
        self.account_records.column("status", width=100)
        self.account_records.column("date_updated", width=70)

        self.account_records.pack(fill=BOTH, expand=1)

        # Use for putting the information into the entry when you click the data
        self.account_records.bind(
            "<Button-1>", lambda event: self.accountInfo(event))
        # Calls the accountDisplay function to display the Data(s)
        self.accountDisplay()

        # Buttons
        # For displaying account data
        self.btnDisplay = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=0, height=2, command=self.accountDisplay)
        self.btnDisplay.grid(row=0, column=0, padx=1)
        # For adding new account data
        self.btnAddNew = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.accountAdd)
        self.btnAddNew.grid(row=1, column=0, padx=1)
        # For updating account data
        self.btnUpdate = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.accountUpdate)
        self.btnUpdate.grid(row=2, column=0, padx=1)
        # For deleting account data
        self.btnDelete = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.accountDelete)
        self.btnDelete.grid(row=3, column=0, padx=1)
        # For searching account data
        self.btnSearch = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=0, height=2, command=self.accountSearch)
        self.btnSearch.grid(row=4, column=0, padx=1)
        # For resetting the entries of account manager app
        self.btnReset = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=0, height=2, command=self.accountReset)
        self.btnReset.grid(row=5, column=0, padx=1)
        # For exiting the account manager app
        self.btnExit = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=0, height=2, command=self.accountExit)
        self.btnExit.grid(row=6, column=0, padx=1)

        # Function For Exiting account Manager

    def accountExit(self):
        iExit = tkinter.messagebox.askyesno(
            "Account Manager Application", "Do you really want to exit?")
        if iExit > 0:
            self.accountWindow.destroy()
            return

        # Reset all the inputs

    def accountReset(self):
        self.entaID.delete(0, END)
        self.entaName.delete(0, END)
        self.entaType.set("")
        self.entaUserName.delete(0, END)
        self.entaPassword.delete(0, END)
        self.entaStatus.set("")

        # Add Account data

    def accountAdd(self):
        if self.AccountID.get() == "" or self.AccountName.get() == "" or self.AccountType.get() == "" or self.AccountUserName == "" or self.AccountPassword == "" or self.AccountStatus == "":
            tkinter.messagebox.showerror(
                "Account Manager Application", "Please Enter Correct Details")
        else:
            sqlCon = pymysql.Connect(
                host="localhost", user="root", password="", database="quiz_db")
            cur = sqlCon.cursor()
            cur.execute("INSERT INTO `users` (id, name, user_type, username, password, status) VALUES (%s, %s, %s, "
                        "%s, %s, %s)", (
                            self.AccountID.get(),
                            self.AccountName.get(),
                            self.AccountType.get(),
                            self.AccountUserName.get(),
                            self.AccountPassword.get(),
                            self.AccountStatus.get()
                        ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Account Manager Application", "Record Entered Successfully")
            self.accountDisplay()
            self.accountReset()

        # Function for displaying the account data(s)

    def accountDisplay(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("SELECT * FROM `users`")
        result = cur.fetchall()
        if len(result) != 0:
            self.account_records.delete(*self.account_records.get_children())
            for row in result:
                self.account_records.insert('', END, values=row)
        sqlCon.commit()
        sqlCon.close()

        # Function for when you click a row, that row's data will be displayed on the entry

    def accountInfo(self, event):
        viewInfo = self.account_records.focus()
        learnerData = self.account_records.item(viewInfo)
        row = learnerData['values']
        if len(row) > 0:
            self.AccountID.set(row[0])
        if len(row) > 1:
            self.AccountName.set(row[1])
        if len(row) > 2:
            self.AccountType.set(row[2])
        if len(row) > 3:
            self.AccountUserName.set(row[3])
        if len(row) > 4:
            self.AccountPassword.set(row[4])
        if len(row) > 5:
            self.AccountStatus.set(row[5])

        # This Function allows you to update the account data

    def accountUpdate(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("UPDATE users SET name = %s, user_type = %s, username = %s, password = %s, status = %s WHERE id = "
                    "%s", (
                        self.AccountName.get(),
                        self.AccountType.get(),
                        self.AccountUserName.get(),
                        self.AccountPassword.get(),
                        self.AccountStatus.get(),
                        self.AccountID.get()
                    ))
        sqlCon.commit()
        self.accountDisplay()
        sqlCon.close()
        tkinter.messagebox.showinfo(
            "Account Manager Application", "Record Updated Successfully")

        # This function allows you to delete an account data

    def accountDelete(self):
        sqlCon = pymysql.Connect(
            host="localhost", user="root", password="", database="quiz_db")
        cur = sqlCon.cursor()
        cur.execute("DELETE from users where id=%s", self.AccountID.get())
        sqlCon.commit()
        self.accountDisplay()
        sqlCon.close()
        tkinter.messagebox.showinfo(
            "Account Manager Application", "Record Deleted Successfully")
        self.accountReset()

        # Allows you to search using account id

    def accountSearch(self):
        try:
            sqlCon = pymysql.Connect(
                host="localhost", user="root", password="", database="quiz_db")
            cur = sqlCon.cursor()
            cur.execute("SELECT * FROM users where id=%s",
                        self.AccountID.get())

            row = cur.fetchone()

            self.AccountID.set(row[0])
            self.AccountName.set(row[1])
            self.AccountType.set(row[2])
            self.AccountUserName.set(row[3])
            self.AccountPassword.set(row[4])
            self.AccountStatus.set(row[5])

            sqlCon.commit()

        except:
            tkinter.messagebox.showinfo(
                "Account Manager Application", "No Such Record Found")
            self.accountReset()
        sqlCon.close()


Admin()
