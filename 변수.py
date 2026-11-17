# 변수 선언 모양
# 변수_이름 = 할당 값
# = 등호 표시가 같다는 의미가 아닌 대입을 의미
temp = 25
name = "센서A"
print(temp)
print(name)

x = 10
print("처음 할당된 x:", x)
x = 15
print("재할당된 후의 x:", x)

x= x + 5
print("직전의 x에 5를 더한 후의 x:\n", x)

## 변수이름 규칙
# 숫자로 시작되면 안됨. 특수문자는 언더바만 적용됨
# 파이썬에서는 변수명 규칙을 snake_case로 권장함
# 변수명엔 공백이 들어가면 안됨. 띄어쓰기를 대신해 언더바(_)를 사용함
# 2sensor = 10 # -> 에러 발생
# 2sensor = 10 # -> 숫자부터 시작되면 안됨
sensor_2 = 10 # -> 올바른 변수명
sensor_count = 3
sensorCount = 3 # -> 카멜케이스도 가능하지만 권장하지 않음
print(sensor_count, sensorCount)

temp2 = 25
print(temp2)

# if = 10 # -> if는 예약어이므로 변수명으로 사용 불가
# print(if) # -> 에러 발생

## 대소문자도 변수명에서 구분됨
temp = 40 # 재할당
Temp = 100
print("temp, Temp", temp, Temp) # 40 100

score = 50
score = 70
score = 90
print("score:", score) # 90


## 다른 변수의 값 담기
a = 10
b = a
a = 99

print("a:", a) # 99
print("b:", b) # 10

## 변수 선언 한줄에 여러개 하기
width, height, depth = 10, 20, 30
print("가로: ", width, "세로:", height, "깊이:", depth)
print("직사각형의 넓이:", width*height)
print("직육면체의 부피:", width*height*depth)

# x,y = 10, 20, 30 #ValueError: too many values to unpack (expected 2, got 3)

# NameError
# print(value) # -> NameError: name 'value' is not defined
value = 100
print(value) # -> 정상 출력


# 실습1. 변수 만들고 출력하기
temp = 25
print(temp)
name = "센서A"
print(name)

# 실습2. 앞 코드 수정하기
temperature = 30
print(temperature)
name = "센서A"
print(name)

# 실습3. 직접 변수 만들어 출력하기
my_number = 100
print(my_number)
mood = "잠옴"
print(mood)

# 실습4. 나이, 점수,개수 변수로 표현
age = 26
score = 85
count = 5
label = "나이"
label2 = "점수"
label3 = "개수"
print(label, age)
print(label2, score)
print(label3, count)
