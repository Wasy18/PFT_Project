import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class Exercise_Nav(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # set up elements
        label_title = ttk.Label(self, text="Exercises", relief='ridge')
        self.scrollbar = ttk.Scrollbar(self, orient='vertical')
        self.ex_box = ttk.Treeview(self, height=15, yscrollcommand=self.scrollbar.set, show='tree')
        self.scrollbar.config(command=self.ex_box.yview)

        # place in grid
        self.scrollbar.grid(row=1, column=1, sticky='NS')
        self.ex_box.grid(row=1, column=0, sticky='NS')
        label_title.grid(row=0, column=0, sticky='NEWS')

    def populate_list(self, items):
        for i, el in enumerate(items):
            # self.ex_box.insert(el[0], el[1])
            self.ex_box.insert('', 'end', iid=str(i + 1), text=el[1])

    def get_selection(self):
        return self.ex_box.focus()


class Report_Type(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        rep_label = ttk.Label(self, text="Report Type", borderwidth=2, relief='ridge')
        rep_label.grid(row=0, column=0, sticky='NEW')

        # Radio Buttons for report type
        self.v = tk.IntVar()
        self.one_plus = ttk.Radiobutton(self, text="1+ Set Report", variable=self.v, value=1)
        self.weight = ttk.Radiobutton(self, text="Bodyweight Report", variable=self.v, value=2)
        self.one_plus.grid(row=1, column=0, sticky='NW')
        self.weight.grid(row=2, column=0, sticky='NW')

    def get_report_type(self):
        return self.v.get()


class Date_Type(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        rep_label = ttk.Label(self, text="Date Range", borderwidth=2, relief='ridge')
        rep_label.grid(row=0, column=0, sticky='NEW', columnspan=4)

        # Radio Buttons for report type
        self.v = tk.IntVar()
        self.thirty = ttk.Radiobutton(self, text="30 Days", variable=self.v, value=1)
        self.sixty = ttk.Radiobutton(self, text="60 Days", variable=self.v, value=2)
        self.custom = ttk.Radiobutton(self, text="Custom", variable=self.v, value=3)

        # buttons for custom date + label
        self.date_start = DateEntry(self)
        self.date_end = DateEntry(self)
        self.range_label = ttk.Label(self, text="to")

        # placements
        self.thirty.grid(row=1, column=0, sticky='NW')
        self.sixty.grid(row=2, column=0, sticky='NW')
        self.custom.grid(row=3, column=0, sticky='NW')
        self.date_start.grid(row=3, column=1)
        self.range_label.grid(row=3, column=2)
        self.date_end.grid(row=3, column=3)

        # methods for date choice

    def get_date_choice(self):
        return self.v.get()

    def get_date_range(self):
        return self.date_start.get_date(), self.date_end.get_date()
