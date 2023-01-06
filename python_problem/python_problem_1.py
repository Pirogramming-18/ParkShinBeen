num = 0

while True:
    go = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    try:
        int(go)
    except ValueError:
        print("정수를 입력하세요")
    else:
        go = int(go)
        if 1 <= go <= 3:
            for i in range(go):
                num += 1
                print("playerA :", num)
            break
        else:
            print("1,2,3 중 하나를 입력하세요")
