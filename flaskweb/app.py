from flask import Flask,render_template   # html 연동을 위해 반드시 ,render template을 추가기입

app = Flask(__name__)

@app.route('/') # 루트 경로 - 기본 주소/xxxx
def index():
    return render_template("index.html")   # html 불러오기

@app.route('/register')  # 루트 경로 - 기본 주소/register
def register():
    return "<h1>회원가입 페이지 입니다<h1>"

@app.route('/board')
def board():
    return "<h1>게시판 목록 페이지입니다.<h1>"


if __name__=="__main__":
    app.run()