import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import filedialog as fd

class Exercise_Nav(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        # set to 0 so scrollbar does not get padded when stretching window
        self.columnconfigure(1, weight=0)

        # set up elements
        label_title = ttk.Label(self, text="Exercises", relief='flat')
        self.scrollbar = ttk.Scrollbar(self, orient='vertical')
        self.ex_box = ttk.Treeview(self, height=15, yscrollcommand=self.scrollbar.set, show='tree')
        self.scrollbar.config(command=self.ex_box.yview)

        # place in grid
        self.scrollbar.grid(row=1, column=1, sticky='NS')
        self.ex_box.grid(row=1, column=0, sticky='NEWS')
        label_title.grid(row=0, column=0, sticky='N')

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

        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)

        rep_label = ttk.Label(self, text="Report Type", borderwidth=2, relief='flat')
        rep_label.grid(row=0, column=0, sticky='N')

        # Radio Buttons for report type
        self.v = tk.IntVar()
        self.one_plus = ttk.Radiobutton(self, text="1+ Set Report", variable=self.v, value=1)
        self.weight = ttk.Radiobutton(self, text="Bodyweight Report", variable=self.v, value=2)
        self.whole = ttk.Radiobutton(self, text="Whole Set", variable=self.v, value=3)
        self.one_plus.grid(row=1, column=0, sticky='NEW')
        self.weight.grid(row=2, column=0, sticky='NEW')
        self.whole.grid(row=3, column=0, sticky='NEW')

    def get_report_type(self):
        return self.v.get()


class Date_Type(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        rep_label = ttk.Label(self, text="Date Range", borderwidth=2, relief='flat')
        rep_label.grid(row=0, column=0, sticky='SEW', columnspan=4)

        # Radio Buttons for report type
        self.v = tk.IntVar()
        self.thirty = ttk.Radiobutton(self, text="30 Days", variable=self.v, value=1, command=self.update_selection)
        self.sixty = ttk.Radiobutton(self, text="60 Days", variable=self.v, value=2, command=self.update_selection)
        self.custom = ttk.Radiobutton(self, text="Custom", variable=self.v, value=3, command=self.update_selection)

        # buttons for custom date + label
        self.date_start = DateEntry(self)
        self.date_end = DateEntry(self)

        self.range_label = ttk.Label(self, text="to")

        # placements
        self.thirty.grid(row=1, column=0, sticky='SEW')
        self.sixty.grid(row=2, column=0, sticky='SEW')
        self.custom.grid(row=3, column=0, sticky='SEW')
        self.date_start.grid(row=4, column=0)
        self.range_label.grid(row=4, column=1)
        self.date_end.grid(row=4, column=2)

        # methods for date choice
    def update_selection(self):
        print("UPDATING DATES")
        choice = self.get_date_choice()

        if choice == 1:
            self.date_start.set_date(datetime.datetime.now() - datetime.timedelta(days=30))
            self.date_end.set_date((datetime.datetime.now()))

        if choice == 2:
            self.date_start.set_date(datetime.datetime.now() - datetime.timedelta(days=60))
            self.date_end.set_date((datetime.datetime.now()))

        if choice ==3:
            dates = self.get_date_range()
            self.date_start.set_date(dates[0])
            self.date_end.set_date((dates[1]))
    def get_date_choice(self):
        return self.v.get()

    def get_date_range(self):
        return self.date_start.get_date(), self.date_end.get_date()


class Top_Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.configure(tearoff=False)
        self.database = None

        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(label="Open Database File", command=self.open_database)

        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(label="About", command=self.about)

        self.add_cascade(label="File", menu=file_menu)
        self.add_cascade(label="Help", menu=help_menu)

    def open_database(self):
        filetypes=[("Database Files", "*.db")]
        self.database = fd.askopenfilename(filetypes=filetypes)
        print("OPEN DATABASE BUTTON")
        print(self.database)


    def about(self):
        print("ABOUT BUTTON")

