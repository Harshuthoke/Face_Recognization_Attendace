from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from time import strftime
from datetime import datetime
import tkinter
from face_recognition import Face_Recogntion
import os



class Face_Recognizatio_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognization_System")
        
        #first photo
        img=Image.open(r"E:\Photos_Project\1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second photo
        
        img2=Image.open(r"E:\Photos_Project\3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        #third photo
        
        img3=Image.open(r"E:\Photos_Project\2.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #bg image
        
        img4=Image.open(r"E:\Photos_Project\bg.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #============TIME=====================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font=("times new roman",14,"bold"),bg="white",fg="red")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
            
        
        #student button
        img5=Image.open(r"E:\Photos_Project\student.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details ,cursor="hand2")
        b1.place(x=200,y=100,width=190,height=190)
        
        b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details ,font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=190,height=40)
        
        
        #detect face button
        img6=Image.open(r"E:\Photos_Project\face.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b2=Button(bg_img,image=self.photoimg6,command=self.face_data,cursor="hand2")
        b2.place(x=500,y=100,width=190,height=190)
        
        b2_2=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b2_2.place(x=500,y=300,width=190,height=40)
        
        #attendace face button
        img7=Image.open(r"E:\Photos_Project\attendance.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b3=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b3.place(x=800,y=100,width=190,height=190)
        
        b3_3=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b3_3.place(x=800,y=300,width=190,height=40)
        
        #Help Desk button
        img8=Image.open(r"E:\Photos_Project\helpdesk.jpeg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b4=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b4.place(x=1100,y=100,width=190,height=190)
        
        b4_4=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b4_4.place(x=1100,y=300,width=190,height=40)
        
        
        
        #Train button
        img9=Image.open(r"E:\Photos_Project\train.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b5=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b5.place(x=200,y=350,width=190,height=190)
        
        b5_5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="black",fg="white")
        b5_5.place(x=200,y=550,width=190,height=40)
        
        
        #Photos button
        img10=Image.open(r"E:\Photos_Project\photos.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=350,width=190,height=190)
        
        b6_6=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b6_6.place(x=500,y=550,width=190,height=40)
        
        #Developer button
        img11=Image.open(r"E:\Photos_Project\developer.jpeg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=800,y=350,width=190,height=190)
        
        b7_7=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b7_7.place(x=800,y=550,width=190,height=40)
        
        
        #Exit button
        img12=Image.open(r"E:\Photos_Project\eixt.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        b8=Button(bg_img,image=self.photoimg12,command=self.iExit,cursor="hand2")
        b8.place(x=1100,y=350,width=190,height=190)
        
        b8_8=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",20,"bold"),bg="black",fg="white")
        b8_8.place(x=1100,y=550,width=190,height=40)
        
    #============open image function=========================
    def open_img(self):
        os.startfile("data")
        
        
        
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are you sure exit this project",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        
        else:
            return
        
        #===============Function buttons===============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recogntion(self.new_window)
        
        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognizatio_system(root)
    root.mainloop() 