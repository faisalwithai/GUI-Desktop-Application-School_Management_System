from cProfile import label
from tkinter import *      # python library used of GUI programming
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql as mq
from project_db import *


class CourseCls:
    # default constructor of LMS class having orguments of self(bydefault) & root
    def __init__(self, root):
        self.root = root  # re-initilize the root ,, attribute
        # change the title of of application
        self.root.title("LMS")
        # change the size and (height, width, margan pading)
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")     # color of background
        self.root.focus_force()

        # ==== Title bar ======
        # set the title bar.. heading... darkblue background         "fg used for font"
        title_bar = Label(self.root, text="Manage Course Details", font=(
            "goudy old style", 20, "bold"), bg="#0b5377", fg="white").place(x=10, y=15, width=1180, height=35)

        # ======= Variables ==========   will store the given value form user
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # =========== Label of input fields (fields titles) =============
        Course_Name = Label(self.root, text="Course Name", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=80)
        Course_Duration = Label(self.root, text="Duration", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=120)
        Course_Charges = Label(self.root, text="Charges", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=160)
        Course_Description = Label(self.root, text="Description", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=200)

        # =========== input fields ============  textvariable is keyword
        self.input_Name = Entry(self.root, textvariable=self.var_course, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        # will show input fields
        self.input_Name.place(x=150, y=80, width=200)
        input_Duration = Entry(self.root, textvariable=self.var_duration, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black").place(x=150, y=120, width=200)
        input_Charges = Entry(self.root, textvariable=self.var_charges, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black").place(x=150, y=160, width=200)
        self.input_Description = Text(self.root, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        self.input_Description.place(x=150, y=200, height=120, width=470)

        # ========== operational buttons ============
        self.btn_save = Button(self.root, text="Save", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.save)
        self.btn_save.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=(
            "goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2")
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=(
            "goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2")
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2")
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # ========== Search Area ============
        self.var_search = StringVar()
        Course_Name = Label(self.root, text="Course Name", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=660, y=80)
        input_Course_Name = Entry(self.root, textvariable=self.var_search, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black").place(x=810, y=80, width=250)
        btn_Course_Search = Button(self.root, text="Search", font=(
            "goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2").place(x=1090, y=80, width=100, height=27)

        # ======= content / record of courses ========
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=660, y=120, height=320, width=530)

        # ========= create table frame inside the course content ========
        # make scroll bar inside table frame
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)

        # ======= create table layout ========
        self.courseTable = ttk.Treeview(self.C_Frame, columns=(
            "cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)    # showing side bar
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.courseTable.xview)   # for view x and y of scrol bar
        scrolly.config(command=self.courseTable.yview)   # this will move up and down, left and right easily

        self.courseTable.heading("cid", text="ID")       # create table heading
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("duration", text="Duration")
        self.courseTable.heading("charges", text="Charges")
        self.courseTable.heading("description", text="Description")

        # show only heading colomn not extra one
        self.courseTable["show"] = "headings"

        self.courseTable.column("cid", width=10)       # create table colomn
        self.courseTable.column("name", width=50)
        self.courseTable.column("duration", width=50)
        self.courseTable.column("charges", width=50)
        self.courseTable.column("description", width=130)

        self.courseTable.pack(fill=BOTH, expand=1)    # show create table layout

        self.courseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    #==========  backend functions start ============

    def save(self):
        # conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
        # cursor_obj = conn_obj.cursor()
        try:
            if self.var_course.get() == "":    # validation
                messagebox.showerror("Error","Course name should be required", parent=self.root)
            else:
                name_val = self.var_course.get()    # values getting form different fields
                duration_val = self.var_duration.get()
                charges_val = self.var_charges.get()
                description_val = self.input_Description.get("1.0", END)    # direct value get by varialbe
                input_tuple = (name_val, duration_val, charges_val, description_val)
                # labels = (name, duration, charges, description)

                #========= calling functions of insert_data =======
                insert_data("course", '''(name, duration, charges, description)''', input_tuple) 
                self.show()  
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # ===== This will show the data in the table ========
    def show(self):   # 1st
        try:
            rows = fetch_tabel_data("course")
            # print(rows)
            self.courseTable.delete(*self.courseTable.get_children())     # will delete all pre childern element of table 
            for row in rows:    # will show the data in tabel by itreating
                self.courseTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    # =========== this is for show table data in the fields for update ========
    def get_data(self, evnt):    #2nd
        r=self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        # print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])

        self.input_Description.delete('1.0', END)
        self.input_Description.insert(END, row[4])




if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = CourseCls(root)

    root.mainloop()   # it for stop the window secren of tkinter
