import random
import string

target_phrase = "whyam"
count = 0

while True:
    # 17글자의 랜덤 문자열 생성
    random_string = ''.join(random.choices(string.ascii_lowercase + ' ', k=5))
    count += 1
    print(f"생성된 문자열: {random_string}")

    if target_phrase in random_string:
        print(f"'{target_phrase}'가 포함된 문자열이 나올 때까지 {count}번 시도했습니다.")
        break