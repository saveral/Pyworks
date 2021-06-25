import turtle as t
import random


def turn_right():  #오른쪽 화살키
    t.setheading(0)

def turn_up(): # 위쪽 화살키
    t.setheading(90)

def turn_left(): # 왼쪽 화살키
    t.setheading(180)

def turn_down():  # 아래쪽 화살키
    t.setheading(270)

def play():
    t. forward(10)
    te.forward(9)

    # 적 거북이가 주인공을 쫓아감
    ang = te.towards(t.pos())
    te.setheading(ang)

    # 주인공 거북이가 먹이에 닿으면 먹이 랜덤하게 이동
    if t.distance(tf) < 12:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)

    # 12보다 작으면 잡혀서 게임 종료
    if t.distance(te) >= 12:
        t.ontimer(play, 100)  # 0.1초 간격으로 작동

# 메인 영역
t.setup(500,500) #너비, 높이
t.title("달려라 거북아")
t.bgcolor("lightpink")
t.shape("turtle")
t.speed(0)
t.up()
t.color("blue")

# 적 거북이
te = t.Turtle() # Turtle() 클래스에서 te 인스턴스 생성
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200)

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.listen()
play()

t.mainloop()