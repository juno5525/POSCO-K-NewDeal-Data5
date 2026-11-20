###
#실습 1. 
# ① 나이 입력받기
age = int(input("나이를 입력하세요: "))

# ② 20세 이상인지 조건 확인
condition = age >= 20

# ③ 조건에 따라 출력
if condition:
    print("성인입니다")
else:
    print("미성년자입니다")

##

score = int(input("점수를 입력해주세요: "))

# 점수에 따라 학점 판정
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


###########========
###삼항 연산자
# number가 짝수인지 홀수인지 판단하는 프로그램
# if-elsr 문을 통해서 작성
number = int(input("숫자를 입력해주세요: "))

if number % 2 == 0:
    print("짝수")
else:
    print("홀수")

# number가 짝수인지 홀수인지 판단하는 프로그램
# if-else 문을 통해서 작성해보기
result1=""
number = 555

if number%2 == 0:
    result1 = "짝수"
else:
    result1 = "홀수"

print(result1) # 홀수 or 짝수 출력

# 참일때값 if 조건 else 거짓일때값
result2 = "짝수" if number%2 == 0 else "홀수"
print(result2)
# print("짝수입니다.") if number%2 == 0 else print("홀수입니다.")


#### match ~ case 문
color = input("red, yellow, green 중 하나를 작성해주세요.").strip()
# red -> 퇴장입니다.
# yellow -> 경고입니다.
# green -> 통과입니다.
# 위 세개에 해당하지 않는다면 -> 잘못된 값이 들어왔습니다.
match color:
    case "red" | "RED":
        print("퇴장입니다.")
    case "yellow":
        print("경고입니다.")
    case "green":
        print("통과입니다.")
    case _:
        print("잘못된 값이 들어왔습니다!")

# 설비코드, 온도, 상태
data = ["PUMP-01", 85, "WARNING"]
# {설비명}: 온도 {}도, 주의상태입니다.

match data:
    case [name, temp, "WARNING"]:
        print(f'{name}: 온도 {temp}도, 주의상태입니다.')
    case [name, temp, "NORMAL"]:
        print(f'{name}: 온도 {temp}도, 정상상태입니다.')

'''
match 변수:
    case 변수값1:
        변수==변수값1일 때 실행할 문장
    case 변수값2:
        변수==변수값2일 때 실행할 문장
    case 변수값3:
        변수==변수값3일 때 실행할 문장
    case _:
        변수가 변수값1, 변수값2, 변수값3 모두 아닐때 실행할 문장
        if-else 문에서 else 에 해당하는 조건
'''

# 올바른 아이디와 비밀번호 저장
correct_id = "admin"
correct_pw = "1234"

# 사용자 입력 받기
user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

# 아이디와 비밀번호를 모두 확인
if user_id == correct_id and user_pw == correct_pw:
    print("로그인 성공")
else:
    print("로그인 실패")