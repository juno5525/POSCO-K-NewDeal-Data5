##실습1.

# 온도, 진동, 전류 입력받기
temperature = float(input("온도를 입력하세요: "))
vibration = float(input("진동을 입력하세요: "))
current = float(input("전류를 입력하세요: "))

# 설비 상태 판정
if temperature > 80 or vibration > 4.0:
    print("위험: 즉시정지")

elif current > 60 and temperature > 70:
    print("주의: 부하 점검")

elif vibration > 2.5:
    print("주의: 진동 관찰")

else:
    print("정상")


### 실습2. 두 번째로 큰 숫자 찾기

# 1. 숫자 5개 입력받기
numbers = input("숫자 5개를 입력하세요: ").split()
print("입력한 숫자:", numbers)

# 2. 문자열을 정수로 변환
numbers[0] = int(numbers[0])
numbers[1] = int(numbers[1])
numbers[2] = int(numbers[2])
numbers[3] = int(numbers[3])
numbers[4] = int(numbers[4])
print("정수로 변환:", numbers)

# 3. 리스트 정렬
numbers.sort()
print("오름차순 정렬:", numbers)

# 4. 가장 큰 숫자와 두 번째 숫자 비교
if numbers[4] != numbers[3]:
    second = numbers[3]
    print("가장 큰 숫자가 중복되지 않음")

elif numbers[3] != numbers[2]:
    second = numbers[2]
    print("가장 큰 숫자가 2개 중복됨")

elif numbers[2] != numbers[1]:
    second = numbers[1]
    print("가장 큰 숫자가 3개 중복됨")

else:
    second = numbers[0]
    print("가장 큰 숫자가 4개 중복됨")

# 5. 최종 결과
print("두 번째로 큰 숫자:", second)

##실습.3

# 1. 숫자 2개 입력받기
num1 = float(input("첫번째 숫자: "))
num2 = float(input("두번째 숫자: "))

# 2. 연산자 입력받기
operator = input("연산자(+,-,*,/): ")

print("첫번째 숫자:", num1)
print("두번째 숫자:", num2)
print("선택한 연산자:", operator)


# 3. 연산자에 따라 계산하기
match operator:
    case "+":
        result = num1 + num2

    case "-":
        result = num1 - num2

    case "*":
        result = num1 * num2

    case "/":
        if num2 == 0:
            print("오류: 0으로 나눌 수 없습니다.")
        else:
            result = num1 / num2

    case _:
        print("오류: 지원하지 않는 연산자입니다.")


# 4. 계산 결과 출력하기
if operator in ["+", "-", "*"] or (operator == "/" and num2 != 0):
    print("계산 결과:", result)

##실습.4
# 1. 현재 잔액과 출금 금액 입력
balance = int(input("현재 잔액: "))
withdraw = int(input("출금 금액: "))

print("현재 잔액:", balance)
print("출금 금액:", withdraw)

# 2. 출금 가능 여부 확인
if withdraw < 1000:
    print("출금 실패: 최소 출금 금액은 1,000원입니다.")

elif withdraw > 100000:
    print("출금 실패: 최대 출금 금액은 100,000원입니다.")

elif withdraw % 1000 != 0:
    print("출금 실패: 1,000원 단위로 출금해야 합니다.")

elif withdraw > balance:
    print("출금 실패: 잔액이 부족합니다.")

else:
    print("출금 성공")
    balance = balance - withdraw
    print("남은 잔액:", balance)

#실습4.
numbers = input("숫자 5개 입력: ").split()
# 30 10 20 50 40

numbers[0] = int(numbers[0])
numbers[1] = int(numbers[1])
numbers[2] = int(numbers[2])
numbers[3] = int(numbers[3])
numbers[4] = int(numbers[4])

print("원래 리스트:", numbers)

# 리스트 슬라이싱으로 복사
sorted_numbers = numbers[:]
print("복사한 리스트:", sorted_numbers)

# 정렬
sorted_numbers.sort()
print("정렬한 리스트:", sorted_numbers)

# 중앙값
mid = sorted_numbers[2]

print("중앙값:", mid)
print("원래 리스트:", numbers)
