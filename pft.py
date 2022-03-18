import sqlite3
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates
import datetime
import numpy as np
import tkinter as tk

import pft_gui as gui
import pft_sql as sql



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        exercises = sql.get_exercises()
        self.ex_nav = gui.Exercise_Nav(self)
        self.ex_nav.populate_list(exercises)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.ex_nav.grid(row=0,column=0,sticky='NS')
        
        self.rep_type = gui.Report_Type(self)
        self.rep_type.grid(row=0,column=1)
        
        self.cal = gui.Date_Chooser(self)
        self.cal.grid(row=0,column=0,sticky='W')

        
        
        
        

def main():
    pass
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PFT Report")
    MainApplication(root).grid(row=0,column=0)
    #MainApplication(root).pack(side='top', fill='both',expand=True)
    root.mainloop()

