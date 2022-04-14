import tkinter as tk

from tkcalendar import DateEntry


class Exercise_Nav(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # frame for listbox and scroll
        self.config(highlightbackground="black")
        self.config(highlightthickness=2)

        # set up elements
        label_title = tk.Label(self, text="Exercises", relief='ridge')
        self.scrollbar = tk.Scrollbar(self, orient='vertical', troughcolor="#abab33")
        self.ex_box = tk.Listbox(self, width=38, height=15, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.ex_box.yview)

        # place in grid
        self.scrollbar.grid(row=1, column=1, sticky='NS')
        self.ex_box.grid(row=1, column=0, sticky='NS')
        label_title.grid(row=0, column=0, sticky='NEWS')

    def populate_list(self, items):
        for el in items:
            self.ex_box.insert(el[0], el[1])


class Report_Type(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        rep_label = tk.Label(self, text="Report Type", borderwidth=2, relief='ridge')
        rep_label.grid(row=0, column=0, sticky='NEW')

        # Radio Buttons for report type
        self.v = tk.IntVar()
        self.one_plus = tk.Radiobutton(self, text="1+ Set Report", variable=self.v, value=1)
        self.weight = tk.Radiobutton(self, text="Bodyweight Report", variable=self.v, value=2)
        self.one_plus.grid(row=1, column=0, sticky='NW')
        self.weight.grid(row=2, column=0, sticky='NW')
        # self.grid(row=0,column=0,sticky='NEW')


class Date_Type(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        rep_label = tk.Label(self, text="Date Range", borderwidth=2, relief='ridge')
        rep_label.grid(row=0, column=0, sticky='NEW', columnspan=4)

        # Radio Buttons for report type
        self.v = tk.IntVar()
        self.thirty = tk.Radiobutton(self, text="30 Days", variable=self.v, value=1)
        self.sixty = tk.Radiobutton(self, text="60 Days", variable=self.v, value=2)
        self.custom = tk.Radiobutton(self, text="Custom", variable=self.v, value=3)

        # buttons for custom date + label
        self.date_start = DateEntry(self)
        self.date_end = DateEntry(self)
        self.range_label = tk.Label(self, text="to")

        # placements
        self.thirty.grid(row=1, column=0, sticky='NW')
        self.sixty.grid(row=2, column=0, sticky='NW')
        self.custom.grid(row=3, column=0, sticky='NW')
        self.date_start.grid(row=3, column=1)
        self.range_label.grid(row=3, column=2)
        self.date_end.grid(row=3, column=3)

        # methods for date choice

    def pick_start(self):
        # TODO
        pass

    def pick_end(self):
        # TODO
        pass
