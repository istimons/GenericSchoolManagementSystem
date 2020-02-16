"""
_istimons

This File Contains the user interface only.
Database tests and logic is yet to be added.

"""

__version__ = "1.0"

import tkinter as tk
from tkinter import *
from tkinter import ttk
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
    """ Start the main GUI.
        It encapsulates all the classes that are called as UI methods
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "%s Management System" % school_name)

        self.mainContainer = tk.Frame(self)
        self.mainContainer.pack(side='top', fill='both', expand='yes')
        self.mainContainer.grid_rowconfigure(0, weight=1)
        self.mainContainer.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, StartPage, ChangeSchoolName, ManageClasses, SearcResults):
            frame = F(self.mainContainer, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.trigger_frame(Login)

    def trigger_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        self.nameEnterV = tk.StringVar()
        self.passEnterV = tk.StringVar()

        self.date = datetime.datetime.now().date()

        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class

        self.colorLabel = ttk.Label(self, background='blue', font=SchoolLabelFont)
        self.colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        self.choolNameLabel = ttk.Label(self, text="%s \n""Management System" % school_name, background='blue',
                                        font=SchoolLabelFont)
        self.choolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        self.imLabel = ttk.Label(self, text=self.date, foreground='black', background='blue', font=EntryFont)
        self.imLabel.place(relx=0.89, rely=0.35, relheight=0.05, relwidth=0.099)

        self.customizationViewLabel = ttk.Label(self, background='forestgreen')
        self.customizationViewLabel.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        self.xf = tk.Frame(self.customizationViewLabel, relief=tk.SUNKEN, borderwidth=5)
        self.xf.place(relx=0.33, rely=0.120, relheight=0.65, relwidth=0.39)

        tk.Label(self.customizationViewLabel, text="User Log In ").place(relx=0.498, rely=0.120, anchor=tk.W)
        self.Username = tk.Label(self.xf, text="Username", font=("Verdana", 11))
        self.Username.place(relx=0.13, rely=0.07, relheight=0.10, relwidth=0.71)
        self.nameEnter = tk.Entry(self.xf, bd=2, font=EntryFont, textvariable=self.nameEnterV)
        self.nameEnter.place(relx=0.18, rely=0.18, relheight=0.14, relwidth=0.61)

        self.Password = tk.Label(self.xf, text="Password", font=("Verdana", 11))
        self.Password.place(relx=0.18, rely=0.39, relheight=0.10, relwidth=0.61)
        self.passEnter = tk.Entry(self.xf, bd=2, show='*', font=EntryFont, textvariable=self.passEnterV)
        self.passEnter.place(relx=0.18, rely=0.50, relheight=0.14, relwidth=0.61)

        self.Loginbutton = ttk.Button(self.xf, text="Log in", command=lambda: [controller.trigger_frame(StartPage)])
        self.Loginbutton.place(relx=0.39, rely=0.87, relheight=0.10, relwidth=0.23)

        self.footerLabel = ttk.Label(self, text='\tAdds Here -->',
                                     background='blue', relief=tk.SOLID, font=footerFont)
        self.footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class StartPage(tk.Frame):
    """
    This widgets will be added to class methods, instead of class instances.
    This will make it easy to summarize each widget object functionality in multiprocessing, subprocessing or threading.
    (Widgets)

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.color_label = ttk.Label(self, background='blue',
                                     font=SchoolLabelFont)
        self.color_label.place(relx=0.0, rely=0.0, relheight=0.42, relwidth=4)

        self.school_name_label = ttk.Label(self, text="%s\n"
                                                      "Management System" % school_name, background='blue',
                                           font=SchoolLabelFont)
        self.school_name_label.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        self.search_bar_entry = ttk.Entry(self, font=EntryFont)
        self.search_bar_entry.place(relx=0.72, rely=0.12, relheight=0.05, relwidth=0.2)

        self.search_button_label = ttk.Button(self, text="Search",
                                              command=lambda: [controller.trigger_frame(SearcResults)])
        self.search_button_label.place(relx=0.77, rely=0.193, relheight=0.045, relwidth=0.1)

        self.button_change_schoolName = ttk.Button(self, text='Change Name',
                                                   command=lambda: [controller.trigger_frame(ChangeSchoolName)])
        self.button_change_schoolName.place(relx=0.010, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_add_classes = ttk.Button(self, text='Classes',
                                             command=lambda: [controller.trigger_frame(ManageClasses)])
        self.button_add_classes.place(relx=0.11, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_add_lecturer = ttk.Button(self, text='Students')
        self.button_add_lecturer.place(relx=0.21, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_add_worker = ttk.Button(self, text='Lecturers')
        self.button_add_worker.place(relx=0.31, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_subjects_update = ttk.Button(self, text='Update subjets')
        self.button_subjects_update.place(relx=0.41, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_hostels = ttk.Button(self, text='Hostels')
        self.button_hostels.place(relx=0.51, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_food = ttk.Button(self, text='Kitchen & Cafe')
        self.button_food.place(relx=0.61, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_other_workers = ttk.Button(self, text='Employees')
        self.button_other_workers.place(relx=0.71, rely=0.34, relheight=0.06, relwidth=0.093)

        self.button_accounts = ttk.Button(self, text='Accounts')
        self.button_accounts.place(relx=0.81, rely=0.34, relheight=0.06, relwidth=0.093)

        self.search_bar_label = Button(self, text='Log out', borderwidth=0,
                                       command=lambda: [controller.trigger_frame(Login)])
        self.search_bar_label.place(relx=0.934, rely=0.34, relheight=0.06, relwidth=0.06)

        # ---------------------------- status Labels -----------------------------------------------------------

        self.customization_view_label = ttk.Label(self, relief=tk.GROOVE, background='forestgreen', borderwidth=1)
        self.customization_view_label.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        self.school_status_label = ttk.Label(self.customization_view_label, font=StatusProgressLabel, relief=tk.SOLID,
                                             text='Current Status', background='grey')
        self.school_status_label.place(relx=0.4, rely=0.07)

        self.classes_status_label = ttk.Label(self.customization_view_label, text='Classes     :  \t 23',
                                              relief=tk.SOLID,
                                              font=statusLabelFonts, background='grey')
        self.classes_status_label.place(relx=0.11, rely=0.25, relheight=0.06, relwidth=0.15)

        self.lectures_status_label = ttk.Label(self.customization_view_label, text='Lectures   :  \t 103',
                                               relief=tk.SOLID,
                                               font=statusLabelFonts, background='grey')
        self.lectures_status_label.place(relx=0.11, rely=0.35, relheight=0.06, relwidth=0.15)

        self.classesStatusLabel = ttk.Label(self.customization_view_label, text='Workers   :  \t 300', relief=tk.SOLID,
                                            font=statusLabelFonts, background='grey')
        self.classesStatusLabel.place(relx=0.11, rely=0.45, relheight=0.06, relwidth=0.15)

        self.classesStatusLabel = ttk.Label(self.customization_view_label, text='Hostels     :  \t 359',
                                            relief=tk.SOLID,
                                            font=statusLabelFonts, background='grey')
        self.classesStatusLabel.place(relx=0.11, rely=0.55, relheight=0.06, relwidth=0.15)

        # ---------------------------- status Labels -----------------------------------------------------------

        self.footerLabel = ttk.Label(self, text='\tAdds Here -->',
                                     background='blue', relief=tk.SOLID, font=footerFont)
        self.footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class ChangeSchoolName(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        self.nameEnterV = tk.StringVar()
        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class

        self.colorLabel = ttk.Label(self, background='blue', font=SchoolLabelFont)
        self.colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        self.schoolNameLabel = ttk.Label(self, text="%s \n""Management System" % school_name, background='blue',
                                         font=SchoolLabelFont)
        self.schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        self.customizationViewLabel = ttk.Label(self, background='forestgreen')
        self.customizationViewLabel.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        self.xf = tk.Frame(self.customizationViewLabel, relief=tk.SUNKEN, borderwidth=5)
        self.xf.place(relx=0.33, rely=0.120, relheight=0.65, relwidth=0.39)

        tk.Label(self.customizationViewLabel, text="Change School Name ").place(relx=0.47, rely=0.120, anchor=tk.W)

        self.change_school_name_entry = tk.Entry(self.xf, bd=2, font=EntryFont, textvariable=self.nameEnterV)
        self.change_school_name_entry.place(relx=0.18, rely=0.18, relheight=0.14, relwidth=0.61)

        self.nameNote = ttk.Label(self.xf, text='Note : Your School Name Should Not Be More Than 40 Characters',
                                  font=SchoolNameWarningFont, foreground='red')
        self.nameNote.place(relx=0.1, rely=0.48, relheight=0.14, relwidth=0.9)

        self.updateSchool_name_button = ttk.Button(self.xf, text="Update",
                                                   command=lambda: [controller.trigger_frame(StartPage)])
        self.updateSchool_name_button.place(relx=0.35, rely=0.87, relheight=0.10, relwidth=0.23)

        self.footerLabel = ttk.Label(self, text='\tAdds Here -->',
                                     background='blue', relief=tk.SOLID, font=footerFont)
        self.footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class ManageClasses(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        self.nameEnterV = tk.StringVar()
        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class

        self.colorLabel = ttk.Label(self, background='blue', font=SchoolLabelFont)
        self.colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        self.schoolNameLabel = ttk.Label(self, text="%s \n""Management System" % school_name, background='blue',
                                         font=SchoolLabelFont)
        self.schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        self.backButtonLabel = ttk.Button(self, text="Back", command=lambda: [controller.trigger_frame(StartPage)])
        self.backButtonLabel.place(relx=0.77, rely=0.20, relheight=0.05, relwidth=0.1)

        self.customizationViewLabel = ttk.Label(self, background='forestgreen')
        self.customizationViewLabel.place(relx=0.0, rely=0.40, relheight=0.57, relwidth=0.9999)

        self.footerLabel = ttk.Label(self, text=' \t\tAdds Here -->',
                                     background='blue', relief=tk.SOLID, font=footerFont)
        self.footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


class SearcResults(tk.Frame):  # Inheriting every frame we used
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # Parent Class is the GUI class
        self.re = 'Entry Search From Database'

        self.colorLabel = ttk.Label(self, background='blue',
                                    font=SchoolLabelFont)
        self.colorLabel.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=4)

        self.schoolNameLabel = ttk.Label(self, text="%s \n"
                                                    "Management System" % school_name, background='blue',
                                         font=SchoolLabelFont)
        self.schoolNameLabel.place(relx=0.0123, rely=0.02, relheight=0.2, relwidth=0.7)

        self.searchResultsLabel = ttk.Label(self, text="Search Results : %s" % self.re, background='forestgreen',
                                            relief=tk.GROOVE,
                                            font=SearchResultsFont)
        self.searchResultsLabel.place(relx=0.0, rely=0.4, relheight=0.06, relwidth=3)

        self.backButtonLabel = ttk.Button(self, text="Back", command=lambda: [controller.trigger_frame(StartPage)])
        self.backButtonLabel.place(relx=0.77, rely=0.20, relheight=0.05, relwidth=0.1)

        self.footerLabel = ttk.Label(self, text='\tAdds Here -->',
                                     background='blue', relief=tk.SOLID, font=footerFont)
        self.footerLabel.place(relx=0.0, rely=0.96, relheight=0.05, relwidth=1.0)


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
app.update_idletasks()
app.update()
app.mainloop()
