
with open('score.txt','a') as f:
    name = input("이름 입력 : ")
    kor = int(input("국어 점수 : "))
    math = int(input("수학 점수 : "))
    avg = (kor + math) / 2

    f.write(name + ' ')
    f.write(str(kor) + ' ')
    f.write(str(math) + ' ')
    f.write(str(avg) + '\n')

with open('scorelist.txt','a') as f:
    key = ' '
    while True:
        try :
            key = input("성적을 저장할까요?<y/n>: ")
            if key == 'n' or key == 'N':
                break
            elif key == 'y' or key == 'Y':
                name = input("이름 입력 : ")
                kor = int(input("국어 점수 : "))
                math = int(input("수학 점수 : "))
                avg = (kor + math) / 2

                f.write(name + ' ')
                f.write(str(kor) + ' ')
                f.write(str(math) + ' ')
                f.write(str(avg) + '\n')
            else:
                print("잘못된 입력입니다. 다시입력해")
        except ValueError:
              print("잘못된 입력입니다. 다시 입력해")
    print("입력을 종료합니다.")
