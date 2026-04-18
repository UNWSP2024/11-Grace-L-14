'''Favorite Saying GUI Program
By Grace LeVoir
4 - 15 - 26'''


import tkinter

class SayingGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('My Favorite Saying')
        saying = tkinter.Label(self.main_window, text="You've got to dig deep!")
        saying.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    saying = SayingGUI()