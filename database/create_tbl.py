# 데이터베이스 연결 파일
from libs.db.dbconn import getconn
def create_table():
    conn = getconn() #dbconn 모듈에서 getconn 호출 (객체 생성)
    cur = conn.cursor()  # db작업을 하는 객체(cur)
    #테이블 생성 -sql언어 DDL
    sql = """
         create table member(
         name char(20),
         age int
        )
    """

    cur.execute(sql)

    conn.commit()  # 트랜잭션 완료(수행)
    conn.close()   # 네트워크 종료

if __name__=="__main__":
    create_table()