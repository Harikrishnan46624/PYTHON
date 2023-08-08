from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk




class Bill_App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")


        #image1
        img = Image.open("billing\img3.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  # or Image.Resampling.LANCZOS
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=400, height=130)



        img_1 = Image.open("billing\website.jpg")
        img_1 = img_1.resize((500, 130), Image.LANCZOS)  # or Image.Resampling.LANCZOS
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1 = Label(self.root, image=self.photoimg_1)
        lbl_img_1.place(x=500, y=0, width=400, height=130)


        #image3
        img_2 = Image.open("billing\Sunflower_from_Silesia2.jpg")
        img_2 = img_2.resize((500, 130), Image.LANCZOS)  # or Image.Resampling.LANCZOS
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2 = Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=1000, y=0, width=520, height=130)




if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()