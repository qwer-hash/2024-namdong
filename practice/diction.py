vending_machine = {
    "콜라": 1000,
    "사이다": 1200,
    "과자": 1500,
    "물": 800
}

while True:
    mode = input("\n1. 사용자 모드\n2. 관리자 모드\n3. 종료\n모드를 선택하세요: ")

    if mode == '1':  # 사용자 모드
        item_choice = input("\n구매할 물건을 입력하세요 (콜라, 사이다, 과자, 물): ")

        if item_choice in vending_machine:
            print("잔액이 부족합니다.")
        else:
            print("다시 입력해주세요.")

    elif mode == '2':
        pass

    elif mode == '3':
        print("일이 끝났습니다.")
        break
    else:
        print("잘못된 선택입니다.")
