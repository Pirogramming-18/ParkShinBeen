num = 0
go = 0
player = True

while True:
    while True:
        go = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

        try:
            int(go)
        except ValueError:
            print("정수를 입력하세요")
        else:
            go = int(go)
            if 1 <= go <= 3:
                break
            else:
                print("1,2,3 중 하나를 입력하세요")

    for i in range(go):
        num += 1
        if player:
            print("playerA :", num)
        else:
            print("playerB :", num)
    player = not player
