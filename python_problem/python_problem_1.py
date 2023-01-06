num = 0
go = 0
player = False

while num < 31:
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

    player = not player

    for i in range(go):
        num += 1
        if player:
            print("playerA :", num)
        else:
            print("playerB :", num)
        if num == 31:
            break
