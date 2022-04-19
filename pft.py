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

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # exercise list
        self.exercises = sql.get_exercises()
        self.ex_nav = gui.Exercise_Nav(self)
        self.ex_nav.populate_list(self.exercises)
        self.ex_nav.grid(row=0, column=0, sticky='NSEW')

        # frame to hold elements beside exercise list
        self.sideframe = ttk.Frame(self)
        self.sideframe.rowconfigure(0, weight=1)
        self.sideframe.columnconfigure(0, weight=1)
        self.sideframe.grid(row=0, column=1, sticky='NESW')

        # report type
        self.rep_type = gui.Report_Type(self.sideframe)
        self.rep_type.grid(row=0, column=0, sticky='NEW')

        # date chooser
        self.date_type = gui.Date_Type(self.sideframe)
        self.date_type.grid(row=1, column=0, sticky='NEW')

        # generate button
        generate_button = ttk.Button(self.sideframe, text='Generate Report', command=self.generate_report)
        generate_button.grid(row=2, column=0, sticky='EW')

    def generate_report(self):
        # form input validation
        exercise_choice = self.ex_nav.get_selection()
        if exercise_choice:
            print(exercise_choice)
        else:
            tk.messagebox.showwarning(title="Report Button Test", message="Invalid Exercise Selection")

        report_type = self.rep_type.get_report_type()
        if report_type:
            print(report_type)
        else:
            tk.messagebox.showwarning(title="Report Button Test", message="Invalid Report Selection")

        date_choice = self.date_type.get_date_choice()
        if date_choice:
            print(date_choice)
            if date_choice == 3:
                start, end = self.date_type.get_date_range()
                print(start)
                start_timestamp = time.mktime(datetime.datetime.strptime(str(start), "%Y-%m-%d").timetuple())*1000
                print(int(start_timestamp))
                end_timestamp = time.mktime(datetime.datetime.strptime(str(end), "%Y-%m-%d").timetuple())*1000
                print(int(end_timestamp))
                print(end)
                # print(datetime.datetime.timestamp(start))
        else:
            tk.messagebox.showwarning(title="Report Button Test", message="Invalid Date Selection")

        sql.pft_sql(exercise_choice)


def main():

    root = ThemedTk(theme='breeze')
    root.option_add('*Font',' Arial 10')
    root.title("PFT Report")
    style = ThemedStyle(root)
    MainApplication(root).grid(row=0, column=0)
    root.mainloop()


if __name__ == "__main__":
    main()

