import tkinter as tk 
from tkinter import *
import sys
import time

class Main:

    def __init__(self):       
        self.wn = tk.Tk()
        self.wn.title("Clicker")
        self.wn.attributes("-fullscreen", True)
        self.wn.resizable(False, False)
        self.wn.configure(bg="darkblue")
        self.points = 0
        self.pointplus = 1
        self.cost = 1
        #self.ovenCost = 30
        #self.ovenPoints = 0

    def run(self):
        self.buttons()
        self.config_grid()
        self.labels()
        self.grid_widgets_main()
        self.wn.mainloop()    

    def buttons(self):
        self.mainclick = tk.Button(self.wn, width=20, height=5, bg="blue", fg="white", font=("Arial", 18), text="Cookie", activebackground="cyan", command=self.scorepoint)
        self.menu = tk.Button(self.wn, width=10, height=3, bg="blue", fg="white", font=("Arial", 18), text="Menu", activebackground="cyan", command=self.up_menu)
        self.exit = tk.Button(self.wn, width=10, height=3, bg="blue", fg="white", font=("Arial", 18), text="Exit", activebackground="cyan", command=lambda: sys.exit())
        self.upgrade = tk.Button(self.wn, height=3, bg="blue", fg="white", font=("Arial", 18), text=f"Upgrade: {self.cost}", activebackground="cyan", command=self.incr_points)
        self.back = tk.Button(self.wn, width=10, height=3, bg="blue", fg="white", font=("Arial", 18), text="Back", activebackground="cyan", command=self.grid_widgets_main)
        #self.oven = tk.Button(self.wn, width=10, height=3, bg="blue", fg="white", font=("Arial", 18), text="Oven", activebackground="cyan", command=self.bakeUp)


    def labels(self):
        self.score = tk.Label(self.wn, width=10, height=3, bg="blue", fg="white", font=("Arial", 18), text=self.points)

    def grid_widgets_main(self):
        for n in self.wn.winfo_children():
            n.grid_forget()
        self.mainclick.grid(row=2, column=2, padx=5, pady=5)
        self.menu.grid(row=0, column=4, padx=5, pady=5)
        self.exit.grid(row=0, column=0, padx=5, pady=5)
        self.score.grid(row=4, column=2, padx=5, pady=5)

    def grid_widgets_menu(self):
        self.upgrade.grid(row=2, column=2, padx=5, pady=5)
        self.back.grid(row=0, column=2, padx=5, pady=5)
        #self.oven.grid(row=4, column=2, padx=5, pady=5)

    def up_menu(self):
        for n in self.wn.winfo_children():
            n.grid_forget()
        self.grid_widgets_menu()

    def scorepoint(self):
        self.points += self.pointplus   
        self.score.configure(text=round(self.points))

    def incr_points(self):
        if self.points >= self.cost:
            self.pointplus += self.cost * 0.99
            self.points -= self.cost
            self.cost *= 10
            self.upgrade.configure(text=f"Upgrade: {self.cost}")
            self.score.configure(text=round(self.points))

    #def bakeUp(self):
    #    if self.points >= self.ovenCost:
    #        self.ovenPoints += 10
    #        self.ovenCost *= 30

    def config_grid(self):
        self.wn.rowconfigure(0, weight=1)
        self.wn.rowconfigure(1, weight=1)
        self.wn.rowconfigure(2, weight=1)
        self.wn.rowconfigure(3, weight=1)
        self.wn.rowconfigure(4, weight=1)
        self.wn.columnconfigure(0, weight=1)
        self.wn.columnconfigure(1, weight=1)
        self.wn.columnconfigure(2, weight=1)
        self.wn.columnconfigure(3, weight=1)
        self.wn.columnconfigure(4, weight=1)

if __name__ == "__main__":
    app = Main()
    app.run()
