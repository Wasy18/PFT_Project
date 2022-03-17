import tkinter as tk



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
    
