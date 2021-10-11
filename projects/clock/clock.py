from tkinter import *
from datetime import *
import  time
import bg as bg
from math import *
from PIL import ImageDraw,Image,ImageTk


class clock:
    def __init__(self,root):
        self.root=root
        self.root.title("clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        title=Label(self.root, text="Abhijeet Clock", font=("", 50),bg="#E6E6FA", fg="#021e2f").place(x=0,y=50, relwidt=1)

        self.lbl=Label(self.root, bg="#E6E6FA")
        self.lbl.place(x=450, y=150, height=400, width=400)
     #   self.clock_img()
        self.working()


    def clock_img(self,hr,mins,sec):
        clock=Image.new("RGB", (400, 400), (0, 0, 0))
        draw= ImageDraw.Draw(clock)

        #=========for Clock Image
        bg=Image.open("cl.png")
        bg=bg.resize((300, 300),Image.ANTIALIAS)
        clock.paste(bg,(50, 50))

        #============hur line image
        origrn=200,200
        draw.line((origrn, 200+60*sin(radians(hr)), 200-60*cos(radians(hr))), fill="#6E470B", width=4)
        # ============min line image
        draw.line((origrn, 200+80*sin(radians(mins)), 200-80*cos(radians(mins))), fill="#6E470B", width=4)
        # ============sec line image
        draw.line((origrn, 200+80*sin(radians(sec)), 200-100*cos(radians(sec))), fill="black", width=4)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")

    def working(self):
            h=datetime.now().time().hour
            m=datetime.now().time().minute
            s=datetime.now().time().second
           # print(h,m,s)

            hr=(h/12)*360
            mins=(m/60)*360
            sec=(s/60)*360
            #print(hr,mins,sec)
            self.clock_img(hr,mins,sec)
            self.img=ImageTk.PhotoImage(file="clock_new.png")
            self.lbl.config(image=self.img)
            self.lbl.after(200,self.working)
root=Tk()
obj=clock(root)
root.mainloop()