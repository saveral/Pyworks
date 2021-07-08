import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/test2.db")
    return conn

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM t_book"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO t_book(title, publisher, page) VALUES (?, ?, ?)"
    cur.execute(sql, ('천개의 파랑', '천선란', 300))
    conn.commit()
    conn.close()


select_book()
insert_book()


물리          허브,리피터
데이터링크    브릿지, 스위치
네트워크      라우터
전송          tcp/IP UDP
응용          호스트(Pc) 웹,이메일등