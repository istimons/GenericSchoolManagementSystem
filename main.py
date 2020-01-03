"""
_istimons

This File Contains the user interface only.
Database tests and logic is yet to be added.
"""

__version__ = "1.0"

import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import datetime

school_name = "My School Name"

footerFont = "-family {Times New Roman} -size 11 -weight bold -slant roman -underline 0 -overstrike 0"
statusLabelFonts = "-family {Times New Roman} -size 13 -weight bold -slant roman -underline 0 -overstrike 0"
SchoolNameWarningFont = "-family {Times New Roman} -size 12 -weight normal -slant roman -underline 0 -overstrike 0"
StatusProgressLabel = "-family {Times New Roman} -size 35 -weight bold -slant roman -underline 0 -overstrike 0"
EntryFont = "-family {Perpetua Titling MT} -size 17 -weight normal -slant roman -underline 0 -overstrike 0"
SearchResultsFont = "-family {Perpetua Titling MT} -size 20 -weight normal -slant roman -underline 0 -overstrike 0"
SchoolLabelFont = "-family {Perpetua Titling MT} -size 40 -weight normal -slant roman -underline 0 -overstrike 0"


class AppUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "%s Management System" % school_name)

        mainContainer = tk.Frame(self)
        mainContainer.pack(side='top', fill='both', expand='yes')
        mainContainer.grid_rowconfigure(0, weight=1)
        mainContainer.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, StartPage, ChangeSchoolName, ManageClasses, SearcResults):
            frame = F(mainContainer, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.trigger_frame(Login)

    def trigger_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        nameEnterV = tk.StringVar()
        passEnterV = tk.StringVar()

        date = datetime.datetime.now().date()

        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class

        colorLabel = ttk.Label(self, background='blue', font=SchoolLabelFont)
        colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        schoolNameLabel = ttk.Label(self, text="%s \n""Management System" % school_name, background='blue',
                                    font=SchoolLabelFont)
        schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        timLabel = ttk.Label(self, text=date, foreground='black', background='blue', font=EntryFont)
        timLabel.place(relx=0.89, rely=0.35, relheight=0.05, relwidth=0.099)

        customizationViewLabel = ttk.Label(self, background='forestgreen')
        customizationViewLabel.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        xf = tk.Frame(customizationViewLabel, relief=tk.SUNKEN, borderwidth=5)
        xf.place(relx=0.33, rely=0.120, relheight=0.65, relwidth=0.39)

        tk.Label(customizationViewLabel, text="User Log In ").place(relx=0.498, rely=0.120, anchor=tk.W)

        Username = tk.Label(xf, text="Username", font=("Verdana", 11))
        Username.place(relx=0.13, rely=0.07, relheight=0.10, relwidth=0.71)
        nameEnter = tk.Entry(xf, bd=2, font=EntryFont, textvariable=nameEnterV)
        nameEnter.place(relx=0.18, rely=0.18, relheight=0.14, relwidth=0.61)

        Password = tk.Label(xf, text="Password", font=("Verdana", 11))
        Password.place(relx=0.18, rely=0.39, relheight=0.10, relwidth=0.61)
        passEnter = tk.Entry(xf, bd=2, show='*', font=EntryFont, textvariable=passEnterV)
        passEnter.place(relx=0.18, rely=0.50, relheight=0.14, relwidth=0.61)

        Loginbutton = ttk.Button(xf, text="Log in", command=lambda: [controller.trigger_frame(StartPage)])
        Loginbutton.place(relx=0.39, rely=0.87, relheight=0.10, relwidth=0.23)

        footerLabel = ttk.Label(self, text='  Contact Developer For Assistacne +254 100 354 263',
                                background='blue', relief=tk.SOLID, font=footerFont)
        footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        colorLabel = ttk.Label(self, background='blue',
                               font=SchoolLabelFont)
        colorLabel.place(relx=0.0, rely=0.0, relheight=0.42, relwidth=4)

        schoolNameLabel = ttk.Label(self, text="%s\n"
                                               "Management System" % school_name, background='blue',
                                    font=SchoolLabelFont)
        schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        searchBarLabel = ttk.Entry(self, font=EntryFont)
        searchBarLabel.place(relx=0.72, rely=0.12, relheight=0.05, relwidth=0.2)

        searchButtonLabel = ttk.Button(self, text="Search", command=lambda: [controller.trigger_frame(SearcResults)])
        searchButtonLabel.place(relx=0.77, rely=0.193, relheight=0.045, relwidth=0.1)

        buttonChangeSchoolName = ttk.Button(self, text='Change Name',
                                            command=lambda: [controller.trigger_frame(ChangeSchoolName)])
        buttonChangeSchoolName.place(relx=0.010, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonAddClasses = ttk.Button(self, text='Manage Classes',
                                      command=lambda: [controller.trigger_frame(ManageClasses)])
        buttonAddClasses.place(relx=0.11, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonAddLecturer = ttk.Button(self, text='Manage Students')
        buttonAddLecturer.place(relx=0.21, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonAddWorker = ttk.Button(self, text='Lecturers')
        buttonAddWorker.place(relx=0.31, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonSubjectsUpdate = ttk.Button(self, text='School Library')
        buttonSubjectsUpdate.place(relx=0.41, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonLibarary = ttk.Button(self, text='Hostels')
        buttonLibarary.place(relx=0.51, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonLibarary = ttk.Button(self, text='Kitchen & Cafeteria')
        buttonLibarary.place(relx=0.61, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonLibarary = ttk.Button(self, text='Other Workersxncv,m')
        buttonLibarary.place(relx=0.71, rely=0.34, relheight=0.06, relwidth=0.093)

        buttonSubjectsUpdate = ttk.Button(self, text='Accounts')
        buttonSubjectsUpdate.place(relx=0.81, rely=0.34, relheight=0.06, relwidth=0.093)

        searchBarLabel = Button(self, text='Log out', borderwidth=0, command=lambda: [controller.trigger_frame(Login)])
        searchBarLabel.place(relx=0.934, rely=0.34, relheight=0.06, relwidth=0.06)

        # ---------------------------- status Labels -----------------------------------------------------------

        customizationViewLabel = ttk.Label(self, relief=tk.SUNKEN, background='forestgreen', borderwidth=7)
        customizationViewLabel.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        schoolStatusLabel = ttk.Label(customizationViewLabel, font=StatusProgressLabel, relief=tk.SOLID,
                                      text='Current Status', background='grey')
        schoolStatusLabel.place(relx=0.4, rely=0.07)

        classesStatusLabel = ttk.Label(customizationViewLabel, text='Classes     :  \t 23', relief=tk.SOLID,
                                       font=statusLabelFonts, background='grey')
        classesStatusLabel.place(relx=0.11, rely=0.25, relheight=0.06, relwidth=0.15)

        classesStatusLabel = ttk.Label(customizationViewLabel, text='Lectures   :  \t 103', relief=tk.SOLID,
                                       font=statusLabelFonts, background='grey')
        classesStatusLabel.place(relx=0.11, rely=0.35, relheight=0.06, relwidth=0.15)

        classesStatusLabel = ttk.Label(customizationViewLabel, text='Workers   :  \t 300', relief=tk.SOLID,
                                       font=statusLabelFonts, background='grey')
        classesStatusLabel.place(relx=0.11, rely=0.45, relheight=0.06, relwidth=0.15)

        classesStatusLabel = ttk.Label(customizationViewLabel, text='Hostels     :  \t 359', relief=tk.SOLID,
                                       font=statusLabelFonts, background='grey')
        classesStatusLabel.place(relx=0.11, rely=0.55, relheight=0.06, relwidth=0.15)

        # ---------------------------- status Labels -----------------------------------------------------------

        footerLabel = ttk.Label(self, text='  Contact Developer For Assistacne +254 100 354 263',
                                background='blue', relief=tk.SOLID, font=footerFont)
        footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class ChangeSchoolName(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        nameEnterV = tk.StringVar()
        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class

        colorLabel = ttk.Label(self, background='blue', font=SchoolLabelFont)
        colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        schoolNameLabel = ttk.Label(self, text="%s \n""Management System" % school_name, background='blue',
                                    font=SchoolLabelFont)
        schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        customizationViewLabel = ttk.Label(self, background='forestgreen')
        customizationViewLabel.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        xf = tk.Frame(customizationViewLabel, relief=tk.SUNKEN, borderwidth=5)
        xf.place(relx=0.33, rely=0.120, relheight=0.65, relwidth=0.39)

        tk.Label(customizationViewLabel, text="Change School Name ").place(relx=0.47, rely=0.120, anchor=tk.W)

        changeShoolNameEntry = tk.Entry(xf, bd=2, font=EntryFont, textvariable=nameEnterV)
        changeShoolNameEntry.place(relx=0.18, rely=0.18, relheight=0.14, relwidth=0.61)

        nameNote = ttk.Label(xf, text='Note : Your School Name Should Not Be More Than 40 Characters',
                             font=SchoolNameWarningFont, foreground='red')
        nameNote.place(relx=0.1, rely=0.48, relheight=0.14, relwidth=0.9)

        updateSchoolNamebutton = ttk.Button(xf, text="Update", command=lambda: [controller.trigger_frame(StartPage)])
        updateSchoolNamebutton.place(relx=0.35, rely=0.87, relheight=0.10, relwidth=0.23)

        footerLabel = ttk.Label(self, text='  Contact Developer For Assistacne +254 100 354 263',
                                background='blue', relief=tk.SOLID, font=footerFont)
        footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class ManageClasses(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        nameEnterV = tk.StringVar()
        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class

        colorLabel = ttk.Label(self, background='blue', font=SchoolLabelFont)
        colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        schoolNameLabel = ttk.Label(self, text="%s \n""Management System" % school_name, background='blue',
                                    font=SchoolLabelFont)
        schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        backButtonLabel = ttk.Button(self, text="Back", command=lambda: [controller.trigger_frame(StartPage)])
        backButtonLabel.place(relx=0.77, rely=0.20, relheight=0.05, relwidth=0.1)

        customizationViewLabel = ttk.Label(self, background='forestgreen')
        customizationViewLabel.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        footerLabel = ttk.Label(self, text='  Contact Developer For Assistacne +254 100 354 263',
                                background='blue', relief=tk.SOLID, font=footerFont)
        footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class SearcResults(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class
        re = 'This will be oepning database directly to check for Entry Data'

        colorLabel = ttk.Label(self, background='blue',
                               font=SchoolLabelFont)
        colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        schoolNameLabel = ttk.Label(self, text="%s \n"
                                               "Management System" % school_name, background='blue',
                                    font=SchoolLabelFont)
        schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        searchResultsLabel = ttk.Label(self, text="Search Results : %s" % re, background='forestgreen',
                                       relief=tk.GROOVE,
                                       font=SearchResultsFont)
        searchResultsLabel.place(relx=0.0, rely=0.4, relheight=0.06, relwidth=3)

        backButtonLabel = ttk.Button(self, text="Back", command=lambda: [controller.trigger_frame(StartPage)])
        backButtonLabel.place(relx=0.77, rely=0.20, relheight=0.05, relwidth=0.1)

        footerLabel = ttk.Label(self, text='  Contact Developer For Assistacne +254 100 354 263',
                                background='blue', relief=tk.SOLID, font=footerFont)
        footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


app = AppUI()

# Get the root window screen width and height
w = 800  # width for the Tk root
h = 500  # height for the Tk root

# get screen width and height
ws = app.winfo_screenwidth()  # width of the screen
hs = app.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

app.geometry('%dx%d+%d+%d' % (w, h, x, y))

app.mainloop()



