# 함수 이름은 변경 가능합니다.

# menu 1
def Menu1(name, score1, score2):
    # 사전에 학생 정보 저장하는 코딩
    stuList[name] = score(score1, score2)

# menu 2


def Menu2():
    # 학점 부여 하는 코딩
    for stuScore in stuList.values():
        if stuScore.grade == 0:
            avg = (stuScore.mid + stuScore.final) / 2
            if avg >= 90:
                stuScore.grade = 'A'
            elif avg >= 80:
                stuScore.grade = 'B'
            elif avg >= 70:
                stuScore.grade = 'C'
            else:
                stuScore.grade = 'D'


# menu 3
def Menu3():
    # 출력 코딩
    print()
    print("-" * 31)
    print("name    mid    final    grade")
    print("-" * 31)
    for name, score in stuList.items():
        print("{:<7}{:>4}    {:>4}    {:>4}".format(
            name, score.mid, score.final, score.grade))


# menu 4
def Menu4(name):
    # 학생 정보 삭제하는 코딩
    del stuList[name]


# 학생 정보를 저장할 변수 초기화
stuList = {}


class score:
    def __init__(self, mid, final):
        self.mid = mid
        self.final = final
        self.grade = 0


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    # 입력값 예외 처리
    try:
        int(choice)
    except ValueError:
        choice = 0

    if choice == "1":
        # 학생 정보 입력받기
        # 예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        # 예외사항이 아닌 입력인 경우 1번 함수 호출
        inputString = input("Enter name mid-score final-score : ")
        if len(inputString.split()) != 3:
            print("Num of data is not 3!")
            continue
        else:
            name, score1, score2 = inputString.split()

        if name in stuList:
            print("Already exist name!")
            continue

        else:
            pint1 = True
            pint2 = True
            try:
                int(score1)
            except ValueError:
                pint1 = False
            else:
                score1 = int(score1)
            try:
                int(score2)
            except ValueError:
                pint2 = False
            else:
                score2 = int(score2)
            if pint1 and pint2:
                if score1 <= 0:
                    pint1 = False
                if score2 <= 0:
                    pint2 = False
                if pint1 and pint2:
                    Menu1(name, score1, score2)
                else:
                    print("Score is not positive integer!")
            else:
                print("Score is not positive integer!")

    elif choice == "2":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우 2번 함수 호출
        # "Grading to all students." 출력
        if len(stuList) == 0:
            print("No student data!")
        else:
            Menu2()
            print("Grading to all students")

    elif choice == "3":
        # 예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        # 예외사항이 아닌 경우 3번 함수 호출
        if len(stuList) == 0:
            print("No student data!")
        else:
            allGraded = True
            for stuScore in stuList.values():
                if stuScore.grade == 0:
                    print("There is a student who didin't get grade.")
                    allGraded = False
                    break
            if allGraded:
                Menu3()

    elif choice == "4":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        if len(stuList) == 0:
            print("No student data!")
        else:
            name = input("Enter the name to delete : ")
            if name in stuList:
                Menu4(name)
                print(name, "student information is deleted.")
            else:
                print("Not exist name!")

    elif choice == "5":
        # 프로그램 종료 메세지 출력
        # 반복문 종료
        print('Exit Program!')
        break

    else:
        # "Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")
