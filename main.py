import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import qrcode


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('QR Generator')
        self.geometry('400x400')
        self.resizable(False, False)

        # variables
        self.qr_text = ctk.StringVar(value='')
        self.prefix = ctk.StringVar(value='')
        self.prefix_dict = {'Default':'','Email':'mailto:','Phone Number':'tel:'}


        # layout
        TopFrame(self, self.qr_text, self.prefix_dict, self.prefix)
        self.qr = QR(self, self.qr_text, self.prefix)
        BottomFrame(self, self.qr_text, self.qr.create_qr)



class TopFrame(ctk.CTkFrame):
    def __init__(self, parent, qr_text, values, prefix):
        super().__init__(parent, corner_radius=0)
        self.qr_text = qr_text
        self.prefix = prefix

        # grid config
        self.columnconfigure((0,3), weight=1, uniform='a')
        self.columnconfigure(1, weight=2, uniform='a')
        self.columnconfigure(2, weight=3, uniform='a')
        self.rowconfigure(0, weight=1)

        # widgets
        self.option_menu = ctk.CTkOptionMenu(self,font=('Calibri',10),command=lambda c: self.prefix.set(values[c]), values=list(values.keys()),fg_color='#343638', dropdown_fg_color='#343638', button_color='#242424', button_hover_color='#17191b').grid(column=1,row=0, padx=5)
        self.entry = ctk.CTkEntry(self, textvariable=self.qr_text).grid(column=2,row=0, sticky='ew', padx=5)


        # place
        self.place(relx=0, rely=0, relheight=0.15, relwidth=1)




class QR(ctk.CTkFrame):
    def __init__(self, parent, qr_text, prefix):
        super().__init__(parent, width=175, height=175)
        self.prefix = prefix
        self.qr_text = qr_text

        # image
        self.qr_image = Image.open('qr_def.png').resize((175,175))
        self.qr = ImageTk.PhotoImage(self.qr_image)

        # widget
        self.qr_canvas = tk.Canvas(self, width=175, height=175)
        self.qr_canvas.create_image(0,0,image=self.qr, anchor='nw')
        self.qr_canvas.pack()


        self.place(relx=0.5, rely=0.45, anchor='center')

    def create_qr(self, *args):
        prefix = self.prefix.get()
        qr_text = self.qr_text.get()
        if qr_text:
            qr = qrcode.make(prefix + qr_text)
            qr.save('qr.png')
            self.qr_image = Image.open('qr.png').resize((175,175))
            self.qr = ImageTk.PhotoImage(self.qr_image)
            self.qr_canvas.create_image(0,0,image=self.qr, anchor='nw')


class BottomFrame(ctk.CTkFrame):
    def __init__(self, parent, qr_text, create_qr):
        super().__init__(parent, corner_radius=0)

        # variables
        self.qr_text = qr_text

        # main frame config
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # layout
        self.left_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.left_frame.columnconfigure((0,1,2), weight=1)
        self.left_frame.rowconfigure((0,1), weight=1)
        self.left_frame.grid(row=0, column=0, sticky='news')

        self.right_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.right_frame.grid(row=0, column=1, sticky='ew')

        # widgets
        # style buttons
        self.button1 = QRTypeButton(self.left_frame, img_path='bt_style/st.png').grid(row=0, column=0)
        self.button2 = QRTypeButton(self.left_frame, img_path='bt_style/st.png').grid(row=0, column=1)
        self.button3 = QRTypeButton(self.left_frame, img_path='bt_style/st.png').grid(row=0, column=2)

        self.button4 = QRTypeButton(self.left_frame, img_path='bt_style/st.png').grid(row=1, column=0)
        self.button5 = QRTypeButton(self.left_frame, img_path='bt_style/st.png').grid(row=1, column=1)
        self.button6 = QRTypeButton(self.left_frame, img_path='bt_style/st.png').grid(row=1, column=2)


        # menu button
        self.generate = ctk.CTkButton(self.right_frame, text='Generate', command=create_qr).pack(expand=True, fill='both', padx=30, pady=2)
        self.save = ctk.CTkButton(self.right_frame, text='save').pack(expand=True,fill='both', padx=30, pady=2)


        self.place(relx=0,rely=1, relwidth=1, relheight=0.25, anchor='sw')




class QRTypeButton(ctk.CTkButton):
    def __init__(self, parent, img_path):
        w = 46
        h = w
        self.image = ctk.CTkImage(Image.open(img_path), size=(w,h))
        super().__init__(parent, text='', width=w, height=h, image=self.image, fg_color='transparent', hover=False)



if __name__ == '__main__':
    qr_generator = App()
    qr_generator.mainloop()