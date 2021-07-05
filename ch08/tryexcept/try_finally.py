# try~except~finally

def divide(x, y):
    try :
        div = x / y
    except ZeroDivisionError:
        print("0으로 나눌수 없어요")
    else:
        print(div)
    finally:
        print("여기는 꼭 수행하는 구간입니다")

divide(3, 5)