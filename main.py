import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode



class App(ctk.CTk):
    def __init__(self):
        # config
        super().__init__()
        self.title('QR Generator')
        self.geometry('500x450')











if __name__ == '__main__':
    generator = App()
    generator.mainloop()
