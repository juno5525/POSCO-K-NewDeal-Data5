print("hello")
print(101010)

# 주석
print(75)
print(2,33)

# 여러 값 함께 출력
print("온도:",75)
print("설비",1,"번 상태:","정상")

# 숫자 연산 해보기
print(75+120)
print(75-120)
print(75*120)
print(75/120)
print((75+80)/2)

print("=== 1번 설비 설정값====")
print("온도(°C): 75")
print("진동(mm/s): 2.3")
print("압력(MPa): 1.5")

# 에러 발생시키기
# 1) NameError: 정의되지 않은 변수 사용
# print(abc) # -> NameError: name 'abc' is not defined
#
print("abc") #-> 정상 출력

# 2) SyntaxError: 잘못된 문법
# print("hello) # -> SyntaxError: EOL while scanning string literal
#
print("hello") # -> 정상 출력

# print(온도, 75) > 
print("온도", 75)
# print("진동", 2.3 >
print("진동", 2.3)
# print("압력": 4.0) >
print("압력", 4.0)

temp = 25
temp = 30
print(temp)
print("온도:", temp)
print("온도:", temp, "°C")
print("온도:", temp, "°C", "진동:", 2.3, "압력:", 4.0)

a = 10
b = a
a = 99
print(b) # 10
