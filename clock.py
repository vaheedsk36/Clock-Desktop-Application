from tkinter import *
from time import strftime
CLOCK_FONT = ("DS-DIGITAL",80)
BG_COLOR = 'black'
CLOCK_TEXT = '#43F500'
class Clock:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x100')
        self.window.resizable(0,0)
        self.window.config(bg = BG_COLOR)
        self.window.title('Digital Clock')
        self.label()

    def label(self):
        self.label = Label(self.window,font=CLOCK_FONT, bg=BG_COLOR, fg=CLOCK_TEXT)
        self.label.pack(anchor='center')
        self.time()

    def time(self):
        self.string = strftime('%I:%M:%S %p')
        self.label.config(text=self.string)
        self.label.after(1000,self.time)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    clock = Clock()
    clock.run()
