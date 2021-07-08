# 데이터베이스에 접속

import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/webdb.db")
    return conn

''' # 전체 불러오기
def select_book():
    conn = getconn()     # 접속
    cur = conn.cursor()
    sql = "SELECT * FROM t_book"
    cur.execute(sql)
    rs = cur.fetchall()  # 검색한 내용 리스트
    for i in rs:
        print(i)
    conn.close()          # 접속 해제
'''

# 하나만 추출해 불러오기
def select_one():
    conn = getconn()     # 접속
    cur = conn.cursor()
    sql = "SELECT * FROM t_book WHERE book_no=?"
    cur.execute(sql,(3,))
    rs = cur.fetchall()  # 검색한 내용 리스트
    print(rs)
    conn.close()          # 접속 해제

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO t_book(title, publisher, page) VALUES (?, ?, ?)"
    cur.execute(sql, ('천개의 파랑', '천선란', 300))
    conn.commit()
    conn.close()

def update_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE t_book SET page=? WHERE book_no=?"
    cur.execute(sql, (400, 2))
    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM t_book WHERE book_no=?"
    cur.execute(sql, (1, ))  # 하나를 삭제하지만 콤마를 찍어준다고 함
    conn.commit()
    conn.close()

# 실행 구간
if __name__ == "__main__":
    #insert_book()  # 이미 한번했으면 주석처리해야함
    #update_book() # 이미 한번했으면 주석처리해야함
    #delete_book()
    #select_book()
    select_one()
