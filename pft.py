import datetime
import time
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter.font import Font
from ttkthemes import ThemedTk
import pft_gui as gui
import pft_sql as sql


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.database = None
        #create menu bar
        menu_bar = gui.Top_Menu(self)
        self.parent.configure(menu=menu_bar)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        #intro screen blurb
        info_screen = gui.Intro_Screen(self)
        info_screen.grid(row=0,column=0)
        self.grid(row=0,column=0)
        self.var = tk.IntVar()

        # wait for database open
        self.wait_variable(name=self.var)
        info_screen.destroy()

        # set after to avoid resizing info screen
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3,weight=0)

        # self.database is updated with change_var on file open
        self.db = sql.PFT_Database(self,self.database)
        self.initialize_exercise_list()

        # frame to hold elements beside exercise list
        self.sideframe = ttk.Frame(self)
        self.sideframe.rowconfigure(0, weight=1)
        self.sideframe.columnconfigure(0, weight=1)
        self.sideframe.rowconfigure(1, weight=1)
        self.sideframe.columnconfigure(1, weight=0)
        self.sideframe.grid(row=1, column=1, sticky='NEWS')

        # report type
        self.rep_type = gui.Report_Type(self.sideframe)
        self.rep_type.grid(row=0, column=0, sticky='NEWS')

        # date chooser
        self.date_type = gui.Date_Type(self.sideframe)
        self.date_type.grid(row=1, column=0, sticky='NEWS')

        # generate button
        generate_button = ttk.Button(self.sideframe, text='Generate Report', command=self.generate_report)
        generate_button.grid(row=3, column=0, sticky='EW')

        # auto resize and lock window
        self.parent.geometry("")
        self.parent.resizable(width=False, height=False)


    def initialize_exercise_list(self):
        self.exercises = self.db.get_exercises()
        self.ex_nav = gui.Exercise_Nav(self)
        self.ex_nav.populate_list(self.exercises)
        self.ex_nav.grid(row=1, column=0, sticky='NEWS')


    # used for waiting until database is open
    def change_var(self,db):
        self.database = db
        self.update_database(self.database)
        #self.update_database(self.database)
        self.var.set(1)
        print("CHANGE VAL")


    def update_database(self,db):
        self.db = sql.PFT_Database(self,db)
        self.initialize_exercise_list()
        #self.destroy()
        #self.__init__(self.parent)


    def generate_report(self):

        # form input validation
        self.report_type = self.rep_type.get_report_type()
        if self.report_type:
            print(self.report_type)
        else:
            tk.messagebox.showwarning(title="Report Button Test", message="Invalid Report Selection")


        self.exercise_choice = self.ex_nav.get_selection()
        if self.exercise_choice or self.report_type == 1:
            print(self.exercise_choice)
        else:
            tk.messagebox.showwarning(title="Report Button Test", message="Invalid Exercise Selection")


        self.date_choice = self.date_type.get_date_choice()
        if self.date_choice:
            self.start, self.end = self.date_type.get_date_range()
            print(self.start)
            self.start_timestamp = time.mktime(datetime.datetime.strptime(str(self.start), "%Y-%m-%d").timetuple())*1000
            print(int(self.start_timestamp))
            self.end_timestamp = time.mktime(datetime.datetime.strptime(str(self.end), "%Y-%m-%d").timetuple())*1000
            print(int(self.end_timestamp))
            print(self.end)
        else:
            tk.messagebox.showwarning(title="Report Button Test", message="Invalid Date Selection")

        self.db.generate_report(self.report_type, self.exercise_choice, self.start_timestamp, self.end_timestamp)
        #self.db.pft_sql(exercise_choice)


def main():

    root = ThemedTk(theme='breeze')
    root.option_add('*Font',' Arial 10')
    root.title("PFT Report")
    #root.resizable(width=False, height=False)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("250x100")
    style = ThemedStyle(root)
    MainApplication(root).grid(row=0, column=0, sticky="NEWS", padx=2, pady=2)
    root.mainloop()

def entry():
    splash = ThemedTk(theme='breeze')
    splash.option_add('*Font','Arial 10')


if __name__ == "__main__":
    main()

