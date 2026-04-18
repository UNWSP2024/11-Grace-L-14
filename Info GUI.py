'''Informational GUI Program
By Grace LeVoir
4 - 15 - 26'''


import tkinter
import tkinter.messagebox


class InfoGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('Fun Buttons')

        self.info_toggle = tkinter.Button(self.main_window, text = 'Info Here!', command = self.display_info)
        self.info_toggle.pack()

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)
        self.quit_button.pack()

        tkinter.mainloop()



    def display_info(self):
        tkinter.messagebox.showinfo('About Me', '''
        Name: Grace LeVoir
        Address:
        50736 Capri Blvd
        Lakeville, MN, 55234''')


if __name__ == '__main__':
    info_gui = InfoGUI()