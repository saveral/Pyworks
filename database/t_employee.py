from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    #sql - select
    sql = "select * from employee"
    cur.execute(sql)
    rs = cur.fetchall()  # 데이터 목록 반환
    for i in rs:
        print(i)
    conn.close()
def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql ="select * from employee where emp_id='e102'"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)

def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into employee values('e103','손흥민',29,30000)"
    sql = "insert into employee values(emp_id, name, age, salary) values(?, ?, ?, ?)"
    cur.execute(sql, ('e104','김산',22, 5000))
    conn.commit()
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "update employee set age = 30 where emp_id='e103'"
    cur.execute(sql)
    conn.commit()
    conn.close()

update_emp()
#insert_emp()
#select_emp()
select_one()