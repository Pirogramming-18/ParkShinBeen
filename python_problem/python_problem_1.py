from random import randint


def printPlayer(player):
    if player:
        print("computer", end=' ')
    else:
        print("player", end=' ')


def printWinner(player):
    printPlayer(player)
    print("win!")


def brGame():
    num = 0
    go = 0
    player = False
    while num < 31:
        player = not player
        if player:
            go = randint(1, 3)
        else:
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
            printPlayer(player)
            print(num)
            if num == 31:
                break

    printWinner(not player)


brGame()
