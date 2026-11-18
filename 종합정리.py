'''
0. 아이디, 비밀번호, 이메일을 받아서 계정 검증을 하는 프로그램.
1. 아이디 길이는 6자 이상 12자 이하입니다.
2. 아이디는 user_로 시작해야 합니다.
3. 비밀번호는 8자 이상이어야 합니다.
4. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
5. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
6. 이메일은 @가 정확히 한 번 등장해야 합니다.
7. 이메일은 .com으로 끝나야 합니다.
모든 조건을 만족해야 최종 회원가입 가능 여부가 True가 됩니다.
'''



id = "juno5525"
password = "qwer1234!@"

# 3. 비밀번호는 8자 이상이어야 합니다.
pw_length = len(password) >= 8
print(pw_length)

# 4. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
pw_word = "!" in password or "@" in password
print(pw_word)

# 5. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
pw_no_id = id not in password
print(pw_no_id)


# 다시

# 아이디, 비밀번호, 이메일 직접 정의
user_id = "juno5525"
password = "qwer1234!@"
email = "juno5525@gmail.com"

### 아이디 조건
# 1. 아이디 길이는 6자 이상 12자 이하입니다.
id_length = len(user_id) >= 6 and len(user_id) <= 12
print("1번 조건 만족? ", id_length)

# 2. 아이디는 user_로 시작해야 합니다.
id_start = user_id.startswith("user_")
print("2번 조건 만족? ", id_start)

### 비밀번호 조건
# 3. 비밀번호는 8자 이상이어야 합니다.
pw_length = len(password) >= 8
print("3번 조건 만족? ", pw_length)

# 4. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
pw_word = ("!" in password) or ("@" in password)
print("4번 조건 만족? ", pw_word)

# 5. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
pw_no_id = user_id not in password
print("5번 조건 만족? ", pw_no_id)

### 이메일 조건
# 6. 이메일은 @가 정확히 한 번 등장해야 합니다.
email_at = email.count("@") == 1
print("6번 조건 만족? ", email_at)

# 7. 이메일은 .com으로 끝나야 합니다.
email_end = email.endswith(".com")
print("7번 조건 만족? ", email_end)

### 최종 회원가입 가능 여부
result = id_length and id_start and pw_length and pw_word and pw_no_id and email_at and email_end
print("최종 회원가입 가능 여부: ", result)


####

# 문자열 검색 종합 실습
word = "NORMAL-WARNING-NORMAL-ERROR-WARNING"

# 1. WARNING이 몇 번 나타나는지 출력
print(word.count("WARNING"))

# 2. NORMAL이 몇 번 나타나는지 출력
print(word.count("NORMAL"))

# 3. ERROR가 몇 번 나타나는지 출력
print(word.count("ERROR"))

# 4. 첫 번째 WARNING의 시작 위치 구하기
first_warning = word.find("WARNING") # maybe 7
print(first_warning)

# 5. 두 번째 WARNING의 시작 위치 구하기
second_warning = word.find("WARNING", first_warning + 1) #maybe 28
print(second_warning)

# 6. 첫 번째 WARNING의 끝 위치와 두 번째 WARNING의 시작 위치 사이 글자 수
first_end = first_warning + len("WARNING") 
print(second_warning - first_end) # 28-14 = 14

# 7. 두 WARNING 사이에 들어있는 문자열 추출
between = word[first_end:second_warning]
print(between)

# 8. 7번에서 추출한 문자열에 ERROR가 포함되어 있는지 확인
print("ERROR" in between)



### 실습제출
# 실습1. 사칙연산 계산기
a = 17
b = 5
print(a + b)
print(a - b) 
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 실습2.평균과 도형 계산
x = 10
y = 20
z = 30
print((x+y+z)/3)
print(x*y*z)

# 실습5. 설비 지표 계산
# 1. 불량률 계산
total = 500
jjinbba = 23

불량률 = (jjinbba / total) * 100
print("불량률:", 불량률, "%")

# 2. 가동률 계산
가동시간 = 21
전체시간 = 24

가동률 = (가동시간 / 전체시간) * 100
print("가동률:", 가동률, "%")

# 실습6. 시간 변환
time = 500
h = time // 60 # 48...2
min = time % 60 #...2
print(h,"시간", min,"분")

# 실습7. 프로그램 실행시간 계산해보기 (NN초를 시간으로)
s = 98765  # 1min=60s 1h=3600s 1d=86400s
d = s // 86400
h = (s % 86400) // 3600
min = (s % 3600) // 60
seconds = s % 60

print(d, "일", h, "시간", min, "분", seconds, "초")

# 실습8. 정상범위와 다중센서 판정
# 온도 정상범위 판정
temp = 85
temp_normal = 60 <= temp and temp <= 90 # 60~90

# 압력 정상범위 판정
pre = 5
pre_normal = 3 <= pre and pre <= 7 # 3~7

# 모든 센서 정상 여부
all_normal = temp_normal and pre_normal

print("온도정상:", temp_normal,"압력정상:", pre_normal,"모두정상:", all_normal)

#심화
#코드설정 SEC-2026-5525-Y
code = input("인증 코드를 입력하세요: ")

# 1. SEC-로 시작하는지
check1 = code.startswith("SEC-")

# 2. 전체 길이가 15자인지
check2 = len(code) == 15

# 3. 연도가 2026인지
check3 = code[4:8] == "2026"

# 4. 마지막 문자가 X 또는 Y인지
check4 = code[-1] == "X" or code[-1] == "Y"

# 5. 세 번째 항목이 1000~9999 사이인지
check5 = 1000 <= int(code[9:13]) <= 9999

# 6. 하이픈이 정확히 3개인지
check6 = code.count("-") == 3

# 최종 결과
result = check1 and check2 and check3 and check4 and check5 and check6

print("1번 검증:", check1)
print("2번 검증:", check2)
print("3번 검증:", check3)
print("4번 검증:", check4)
print("5번 검증:", check5)
print("6번 검증:", check6)
print("최종 인증 결과:", result)