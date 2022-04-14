import tkinter as tk
import pft_gui as gui
import pft_sql as sql


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # exercise list
        exercises = sql.get_exercises()
        self.ex_nav = gui.Exercise_Nav(self)
        self.ex_nav.populate_list(exercises)
        self.ex_nav.grid(row=0, column=0, sticky='NSEW')

        # frame to hold elements beside exercise list
        self.sideframe = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.sideframe.rowconfigure(0, weight=1)
        self.sideframe.columnconfigure(0, weight=1)
        self.sideframe.grid(row=0, column=1, sticky='NESW')

        # report type
        rep_type = gui.Report_Type(self.sideframe)
        rep_type.grid(row=0, column=0, sticky='NEW')

        # date chooser
        date_type = gui.Date_Type(self.sideframe)
        date_type.grid(row=1, column=0, sticky='NEW')

        # generate button
        generate_button = tk.Button(self.sideframe, text='Generate Report', command=generate_report)
        generate_button.grid(row=2, column=0, sticky='EW')


def main():
    pass


def generate_report():
    tk.messagebox.showinfo(title="Report Button Test", message="Here's your report")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PFT Report")
    MainApplication(root).grid(row=0, column=0)
    # MainApplication(root).pack(side='top', fill='both',expand=True)
    root.mainloop()
