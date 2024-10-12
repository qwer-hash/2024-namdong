# 사용자에게 수학 점수를 입력받아
#상/중/하 반으로 분류해주기
#상 - 90점 이상
#중 - 70점 이상
#하 - 나머지

size = input("수학 점수를 입력해주세요")
print(size)

if size >=90:
    print("당신은 상반입니다")
elif size >= 70:
    print("당신은 중반입니다")
elif size >100:
    print("잘못된 점수입니다.")
elif size < 0:
    print("잘못된 점수입니다.")
else:
    print("당신은 하반입니다")






