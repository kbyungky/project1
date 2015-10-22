__author__ = 'kbyungky'

print("안녕하세요 미친넘아ㅋㅋㅋ")

qwer = -1
while qwer != 0:
    qwer = int(input("양의 정수 입력, 끝나면 0 : "))
    print("배출한 값의 두배", qwer * 2)

loop = -1
while loop != 0:
    loop = int(input("type positive number, if you are done, type 0 : "))
    if(loop != 0):
        print(loop)
    else:
        print("It is over")
