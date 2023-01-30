from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognization_System")
        
        
        
        
        
        #============variable declaration==============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()       
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        
         #first photo
        img=Image.open(r"E:\Photos_Project\s1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second photo
        
        img2=Image.open(r"E:\Photos_Project\s2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        #third photo
        
        img3=Image.open(r"E:\Photos_Project\s3.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #bg image
        
        img4=Image.open(r"E:\Photos_Project\bg.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDNET MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1500,height=650)
        
        #left side lable frame
        Left_Frame=LabelFrame(main_frame,bd=2,bg="grey",relief=RIDGE,text="Student Deatails",font=("times new roman",12,"bold"))
        Left_Frame.place(x=10,y=10,width=660,height=580)
        
        
        img5=Image.open(r"E:\Photos_Project\11.jpg")
        img5=img5.resize((500,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        f_lbl=Label(Left_Frame,image=self.photoimg5)
        f_lbl.place(x=5,y=0,width=650,height=130)
        
        
        #current course
        Current_course_Frame=LabelFrame(Left_Frame,bd=2,bg="grey",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_Frame.place(x=5,y=135,width=650,height=130)
        
        
        #department
        dep_label=Label(Current_course_Frame,text="Department",font=("times new roman",12,"bold"),bg="grey")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(Current_course_Frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","EnTC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)
        
        
        
        #course
        course_label=Label(Current_course_Frame,text="Course",font=("times new roman",12,"bold"),bg="grey")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(Current_course_Frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)
        
        
        #year
        year_label=Label(Current_course_Frame,text="Year",font=("times new roman",12,"bold"),bg="grey")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(Current_course_Frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)
        
        #semester
        semester_label=Label(Current_course_Frame,text="Semester",font=("times new roman",12,"bold"),bg="grey")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(Current_course_Frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select semster","sem-1","sem-2","sem-3","sem-4")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)
        
        
        
        
        #class student information
        class_Student_Frame=LabelFrame(Left_Frame,bd=2,bg="grey",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_Frame.place(x=5,y=250,width=650,height=300)
        
        
        #student id label
        studentId_label=Label(class_Student_Frame,text="Student Id",font=("times new roman",12,"bold"),bg="grey")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        
        studentId_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name label
        studentname_label=Label(class_Student_Frame,text="Student Name",font=("times new roman",12,"bold"),bg="grey")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        studentname_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #student division label
        studentdivision_label=Label(class_Student_Frame,text="Student Division",font=("times new roman",12,"bold"),bg="grey")
        studentdivision_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        division_combo=ttk.Combobox(class_Student_Frame,font=("times new roman",12,"bold"),width=13,state="readonly")
        division_combo["values"]=("Select","A","B","C","D","E","F")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #studentdivision_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        #studentdivision_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #student gender label
        studentgender_label=Label(class_Student_Frame,text="Student Gender",font=("times new roman",12,"bold"),bg="grey")
        studentgender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_Student_Frame,font=("times new roman",12,"bold"),width=13,state="readonly")
        gender_combo["values"]=("Select","Male","Female","Prefer not ro say")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
      #  studentgender_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
       # studentgender_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #student rollno label
        studentrollno_label=Label(class_Student_Frame,text="Student Roll No",font=("times new roman",12,"bold"),bg="grey")
        studentrollno_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        
        studentrollno_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        studentrollno_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        #student email label
        studentemail_label=Label(class_Student_Frame,text="Student Email",font=("times new roman",12,"bold"),bg="grey")
        studentemail_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        
        studentemail_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        studentemail_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #student phoneno label
        studentphone_label=Label(class_Student_Frame,text="Student Phone Number",font=("times new roman",12,"bold"),bg="grey")
        studentphone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        
        studentphone_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        studentphone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #student address label
        studentadd_label=Label(class_Student_Frame,text="Student Address",font=("times new roman",12,"bold"),bg="grey")
        studentadd_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        
        studentadd_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        studentadd_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
         #student DOB
        dob_label=Label(class_Student_Frame,text="Student's DOB",font=("times new roman",12,"bold"),bg="grey")
        dob_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        
        dob_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
         
        #Teacher label
        teacher_label=Label(class_Student_Frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="grey")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        
        teacher_entry=ttk.Entry(class_Student_Frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_Frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_Student_Frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #buttons frame
        btn_frame=Frame(class_Student_Frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=675,height=52)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=10,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=2)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=10,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=10,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2,padx=2)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=10,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3,padx=2)
        
        take_btn=Button(btn_frame,text="Take Sample",command=self.generate_dataset,width=10,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_btn.grid(row=0,column=4,padx=2)
        
        upd_btn=Button(btn_frame,text="Update Sample",command=self.generate_dataset,width=12,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        upd_btn.grid(row=0,column=5,padx=2)
        
        
        #right side lable frame
        Right_Frame=LabelFrame(main_frame,bd=2,bg="grey",relief=RIDGE,text="Student Deatails",font=("times new roman",12,"bold"))
        Right_Frame.place(x=680,y=10,width=660,height=580)
        
        imgrt=Image.open(r"E:\Photos_Project\s1.jpg")
        imgrt=imgrt.resize((500,130),Image.ANTIALIAS)
        self.photoimgrt=ImageTk.PhotoImage(imgrt)
        
        f_lbl=Label(Right_Frame,image=self.photoimgrt)
        f_lbl.place(x=5,y=0,width=650,height=130)
        
        
        # ======SEARCH SYSTEM============
        
        Search_Frame=LabelFrame(Right_Frame,bd=2,bg="grey",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_Frame.place(x=5,y=135,width=640,height=70)
        
         #Search label
        search_label=Label(Search_Frame,text="Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_Frame,font=("times new roman",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select","Roll-No","Phone No","sem-3","sem-4")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_Frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Search_Frame,text="Search",width=10,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)
        
        showall_btn=Button(Search_Frame,text="Show All",width=10,height=1,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=2)
        
        
        
        #===========table frame=================
        table_Frame=Frame(Right_Frame,bd=2,bg="grey",relief=RIDGE)
        table_Frame.place(x=5,y=210,width=640,height=250)
        
        
        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)
        
        self.Student_table=ttk.Treeview(table_Frame,columns=("dep","course","year","sem","id","name","div","roll","teacher","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        
        self.Student_table.heading("dep",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("sem",text="Semester")
        self.Student_table.heading("id",text="ID")
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("teacher",text="Teacher")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("div",text="Division")
        self.Student_table.heading("dob",text="Date Of Birth")
        self.Student_table.heading("email",text="E-mail")
        self.Student_table.heading("phone",text="Phone Number")
        self.Student_table.heading("address",text="Address")
        self.Student_table.heading("photo",text="Photo")
        self.Student_table["show"]="headings"
        
        self.Student_table.pack(fill=BOTH,expand=1)
        
        self.Student_table.column("dep",width=100)
        self.Student_table.column("course",width=100)
        self.Student_table.column("year",width=100)
        self.Student_table.column("sem",width=100)
        self.Student_table.column("id",width=100)
        self.Student_table.column("roll",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("teacher",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("div",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("phone",width=100)
        self.Student_table.column("address",width=100)
        self.Student_table.column("photo",width=150)
        
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    #============function declaration==========================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recongnizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        #self.var_photo.get(),
                                                                                                        self.var_radio1.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succesful","Student data is inserted Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    
    
    #=================== FETCH DATA FROM DATABASE =============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recongnizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
          
    
    #==================Get Cursor===========================
    def get_cursor(self,event=""):
        cursor_focus=self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),        
        self.var_roll.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_teacher.set(data[7]),
        self.var_std_name.set(data[8]),
        self.var_div.set(data[9]),      
        self.var_dob.set(data[10]),        
        self.var_email.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_address.set(data[13]),
        #self.var_photo.set(data[14]),
        self.var_radio1.set(data[14])
        
    #================Update Function==================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recongnizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,roll=%s,gender=%s,teacher=%s,name=%s,division=%s,dob=%s,email=%s,phone=%s,address=%s,photosample=%s where student_ID=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                #self.var_photo.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()                           
                                                                                                                                                                                                            ))
                else: 
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details updated succesfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        
    
    
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delte this student from the system",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recongnizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()   
                messagebox.showinfo("Success","Succesfully deleted student details from the system",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        
                                    
    #======================RESET FUNCTION======================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_teacher.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        #self.var_photo.get(),
        self.var_radio1.set("")
        
    #==========================Generate Data Set or Take photo sample========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
               messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recongnizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1 
                my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,roll=%s,gender=%s,teacher=%s,name=%s,division=%s,dob=%s,email=%s,phone=%s,address=%s,photosample=%s where student_ID=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                 self.var_address.get(),
                                                                                                                                                                                                                #self.var_photo.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()==id+1                           
                                                                                                                                                                                                            ))   
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #============load predefined data on face frontals from openCV===============
                face_classifier=cv.CascadeClassifier("haarcascade_frontalface_default.xml") 
                
                def face_cropped(img):
                    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) 
                    
                    #scalling factor = 1.3
                    #Minimum neighbout = 5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                video = cv.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=video.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv.resize(face_cropped(my_frame),(450,450))
                        face=cv.cvtColor(face,cv.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv.imwrite(file_name_path,face)
                        cv.putText(face,str(img_id),(50,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv.imshow("Crooped Face",my_frame)
                    
                    if cv.waitKey(10)== ord('q') or int(img_id)==100: 
                        break
                    
                video.release()
                cv.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!",parent=self.root)
                          
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
        
















if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 