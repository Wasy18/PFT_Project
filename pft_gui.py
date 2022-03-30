import tkinter as tk
from tkcalendar import Calendar
import datetime


class Exercise_Nav(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.rowconfigure(0,weight = 1)
        self.columnconfigure(0,weight=1)
        
        #frame for listbox and scroll
        self.frame = tk.Frame(highlightbackground="black", highlightthickness=2)
        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0,weight=1)
        
        #set up elements
        label_title = tk.Label(self.frame,text = "Exercises")
        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical',troughcolor="#abab33")
        self.ex_box = tk.Listbox(self.frame,width = 38,height = 15, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.ex_box.yview)
 
        #place in grid
        self.scrollbar.grid(row=1,column=1, sticky='NS')
        self.ex_box.grid(row=1,column=0,sticky ='NS')
        label_title.grid(row=0,column=0)
        self.frame.grid(row=1,column=0)
   
    def populate_list(self,items):
        for el in items:
            self.ex_box.insert(el[0],el[1])
        

class Report_Type(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        
        self.rowconfigure(0,weight = 1)
        self.columnconfigure(0,weight=1) 
        
        
        #frame for RadioButtons and scroll
        self.frame = tk.Frame(highlightbackground="black", highlightthickness=2)
        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0,weight=1)
        rep_label = tk.Label(self.frame,text="Report Type")
        rep_label.grid(row=0,column = 0,sticky = 'NW')
        
        
        # Radio Buttons for report type
        self.v = tk.IntVar()
        self.one_plus = tk.Radiobutton(self.frame, text="1+ Set Report", variable = self.v, value = 1)
        self.weight =  tk.Radiobutton(self.frame, text="Bodyweight Report",variable = self.v, value = 2)
        self.one_plus.grid(row=1,column=0,sticky='NW')
        self.weight.grid(row=2,column=0,sticky='NW')
        #frame.grid(row=1,column=1,sticky='NW')
        self.frame.grid(row=1,column=1,sticky='NEW')
        
class Date_Chooser(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        
        
        self.frame = tk.Frame(highlightbackground="black", highlightthickness=2)
        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0,weight=1)
        
        self.cal = Calendar(self.frame, selectmode='day',year = 2020, month = 5, day = 22)
        self.cal.grid(row = 1, column=0)
        
        
        self.rowconfigure(0,weight = 1)
        self.columnconfigure(0,weight=1)
        
        self.date_label = tk.Label(self.frame,text = "Default")
        #self.end_label = tk.Label(self.frame, text = "End Date")
        
        self.date_label.grid(row = 0, column = 0)
        #self.end_label.grid(row = 0, column = 1)








def ButtonGUI():
    screen = tk.Tk()

    #screen size
    screen.geometry('300x300')

    #alert for button press
    def alert():
        print("button has been pressed")

    #button
    button_tk = tk.Button(screen, text = "Hello", command=alert)

    button_tk.pack(side='top')

    screen.mainloop()

def CanvasGUI():
    screen = tk.Tk()

    screen.geometry('300x300')

    canvas_tk = tk.Canvas(screen, bg='yellow',width=250,height=250)

    

    oval = canvas_tk.create_oval(50,50,100,100, fill='red')
    canvas_tk.pack()
    screen.mainloop()
    
    CanvasGUI()
    
