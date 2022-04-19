from tkinter import *      # python library used of GUI programming
from PIL import Image, ImageTk


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
        title_bar = Label(self.root, text="Manage Course Details",font=(
            "goudy old style", 20, "bold"), bg="#0b5377", fg="white").place(x=10, y=15, width=1180, height=35)

        # ======= Variables ==========
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # =========== Label of input fields =============
        Course_Name = Label(self.root, text="Course Name",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=60)
        Course_Duration = Label(self.root, text="Duration",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=100)
        Course_Charges = Label(self.root, text="Charges",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=140)
        Course_Description = Label(self.root, text="Description",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=180)

        # =========== input fields ============
        input_Name = Entry(self.root, font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=60)
        input_Duration = Entry(self.root, font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=100)
        input_Charges = Entry(self.root, font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=140)
        input_Description = Text(self.root, font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=180)



if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = CourseCls(root)

    root.mainloop()   # it for stop the window secren of tkinter