user_input = ""
X = 0
Y = 0

while user_input != "EXIT":
    while user_input != "EXIT" and user_input != "UP" and user_input != "DOWN" and user_input != "LEFT" and user_input != "RIGHT":
        user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")
    print(user_input)

    if user_input == "UP":
        if Y < 100:
            Y = Y + 1
        else:
            print("범위를 벗어날 수 없습니다.")
    elif user_input == "DOWN":
        if Y > 0:
            Y = Y - 1
        else:
            print("범위를 벗어날 수 없습니다.")
    elif user_input == "LEFT":
        if X > 0:
            X = X - 1
        else:
            print("범위를 벗어날 수 없습니다.")
    elif user_input == "RIGHT":
        if X < 100:
            X = X + 1
        else:
            print("범위를 벗어날 수 없습니다.")
    user_input = ""
print("프로그램을 종료합니다.")