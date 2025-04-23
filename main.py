import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode



class App(ctk.CTk):

    def __init__(self):
        # window config
        super().__init__()
        self.title('QR Generator')
        self.width, self.height = 500, 450
        self.geometry(f'{self.width}x{self.height}')
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)
        self._set_appearance_mode('light')

        # top frame
        self.top_bar = TopFrame(self)



        # bottom frame
        self.bottom_frame = BottomFrame(self)



class TopFrame(ctk.CTkFrame):
    def __init__(self, parent):
        # config
        super().__init__(parent, height=85, fg_color='#6aabd2')
        self.configure(corner_radius=0)
        self.place(relx=0,rely=0, relwidth=1)

        # grid
        self.columnconfigure((0,2), weight=2, uniform='a')
        self.columnconfigure(1, weight=8, uniform='a')




class BottomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, height=85, border_width=0, fg_color='#6aabd2')
        self.configure(corner_radius=0)
        self.place(relx=0,rely=1, relwidth=1, anchor='sw')




if __name__ == '__main__':
    qr_generator = App()
    qr_generator.mainloop()
