from logging import root
import pymysql as mq
from tkinter import ttk, messagebox

def create_db(db_name=None):
    my_obj = mq.connect(host="localhost", user="root", password="")  # crate connection with database
    cursor_obj = my_obj.cursor()  # 3 create object of cursor
    # start use of try and except
    try:
        # db = f"create database if not exists {db_name}"
        db = f"create database {db_name}"
        cursor_obj.execute(db)
        # print(f"{db_name} database created")

    except:
        print("database error")


# ====== this function is used to create new table ===========
def create_table(table_name, labels):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        # cr_table = f"create table if not exists {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)"
        cr_table = f"create table {table_name} ({labels})"
        cursor_obj.execute(cr_table)
        # print(f"{table_name} table created")
    except:
        print("table error")


# ========= this function will insert data in the table ==========
def insert_data(table_name, labels, input_data):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        ins_data = f"INSERT INTO {table_name} {labels} VALUES {input_data}"
        cursor_obj.execute(ins_data)     # it will execute the command but not show data into the tabel
        conn_obj.commit()     # this command will show the data into the table
        # messagebox.showinfo("Success","Record Entered Successfully") 
        # print(f"{table_name} data inserted")
        # print(cursor_obj)
    except Exception as ex:
        print(ex)


#======= this function will fetch the all data form table ========== 
def fetch_tabel_data(table_name):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        cursor_obj.execute(f"select * from {table_name}")    # will execute the statment
        all_data = cursor_obj.fetchall()    # fetch all data of table
        # print(all_data)
        return all_data         # return the data 
    except Exception as ex:
        print(ex)
        
# ======== this function will fetch one record ==========
def fetch_tabel_data_one(table_name, cl_name, conndition):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        cursor_obj.execute(f'''select * from {table_name} where {cl_name}="{conndition}"''')    # will execute the statment
        one_data = cursor_obj.fetchone()    # fetch all data of table
        # print(one_data)
        return one_data         # return the data 
    except Exception as ex:
        # print(ex)
        return None
        

# ========== this function is for update data from table / row =========
def update_data(table_name, input_data):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        ins_data = f'''UPDATE {table_name} SET duration="%s", charges="%s", description="%s" WHERE name="%s"''' % input_data
        cursor_obj.execute(ins_data)     # it will execute the command but not show data into the tabel
        conn_obj.commit()     # this command will show the data into the table
        # messagebox.showinfo("Success","Record Updated Successfully") 
        # print(f"{table_name} data inserted")
        print("cursor_obj")
    except Exception as ex:
        print(ex)


# =========== this function will work for delete record form database ======
def delete_record(table_name,by_name):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        del_data = f'''DELETE from {table_name} WHERE name="{by_name}"'''
        cursor_obj.execute(del_data)
        conn_obj.commit()
        print("data deleted")
    except Exception as ex:
        print(ex)

# ========= this will retrive data by searching in search box ==========
def search_data(table_name, search_txt):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        srch_data = f"SELECT * FROM {table_name} WHERE name like '%{search_txt}%'"
        cursor_obj.execute(srch_data)
        retrive_data = cursor_obj.fetchall()   # fetch all exist data / rows
        return retrive_data
    except Exception as ex:
        print(ex)

# create_db("project_lms")
# create_table("course", "cid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), duration VARCHAR(255), charges VARCHAR(255), description TEXT")
# # insert_data("course", '''(name, duration, charges, description)''', '''("faisal","3 months","4500","abc")''')
# # fetch_tabel_data("course")
# h = "faisal"
# exname = str(h)
# fetch_tabel_data_one("course", "name", exname)
# tup = ("John",36,"jdkjf","faisal")
# update_data("course", tup)
