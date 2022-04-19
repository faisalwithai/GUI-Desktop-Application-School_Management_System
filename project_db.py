import pymysql as mq

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
        pass

def create_table(table_name, labels):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        # cr_table = f"create table if not exists {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)"
        cr_table = f"create table {table_name} ({labels})"
        cursor_obj.execute(cr_table)
        # print(f"{table_name} table created")
    except:
        pass

create_db("project_lms")
create_table("course", "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255)")
