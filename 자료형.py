#int > 정수형
#float > 실수형
#str > 문자열
#bool > 불린형

count = 3 #int
temp = 25.5 #float
name = "센서A" #str
empty = "" #str
ok = True #bool
no = False #bool
print(count > temp) #False
print(count < temp) #True

##type() 함수 : 자료형 확인
print(type(3)) #<class 'int'>
print(type(25.5)) #<class 'float'>
print(type("센서A")) #<class 'str'>
print(type("")) #<class 'str'>
print(type(3>25.5)) #<class 'bool'>
print(type(3<25.5)) #<class 'bool'>
print(type(count)) #<class 'int'>
print(type(temp)) #<class 'float'>
print(type(name)) #<class 'str'>

### 문자열, 숫자형의 더하기 연산자 사용
print(3 + 5) #8
print(3.5 + 5.2) #8.7
print("센서" + "A") #센서A
print("센서" + str(3)) #센서3
print("80"+"70") #8070
print(type("80"+"70")) #<class 'str'>
print(type(3+5)) #<class 'int'>

### 실수형의 더하기
print(0.1+0.2) #0.30000000000000004 (실수의 연산은 작은오차 발생가능)
round(0.1+0.2, 2) #0.3 (소수점 2자리까지 반올림)
round(0.1+0.2, 3) #0.3 (소수점 3자리까지 반올림)
round(0.1+0.2, 4) #0.3 (소수점 4자리까지 반올림)
print(round(0.1+0.2, 2)) #0.3 (소수점 2자리까지 반올림)
print(round(0.1+0.2, 3)) #0.3 (소수점 3자리까지 반올림)
print(round(0.1+0.2, 4)) #0.3 (소수점 4자리까지 반올림)

### 숫자와 문자열의 계산
a = 3
print(a + 5) #8
print(str(a) + "5") #35
# print(a + "5") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10/4) #2.5 나누기 연산의 결과는 정수형이 아닌 실수형
print(10//4) #2 (정수 나눗셈)

# 실습 1. 여러 자료형 변수 만들기
count = 50       # int
temp = 76.0      # float
name = "변압기"   # str
ok = True        # bool
no = False       # bool
is_ok = True     # bool

print(count > temp)  # False
print(count < temp)  # True
print(count)
print(temp)
print(name)
print(ok)
print(no)
print(is_ok)

# 실습 2. type()으로 자료형 확인하기
print(type(count))
print(type(temp))
print(type(name))
print(type(is_ok))

# 실습 3. 자료형 맞히기 퀴즈
# 100의 자료형 예측: int
# 100.0의 자료형 예측: float
# "100"의 자료형 예측: str

print(type(100))
print(type(100.0))
print(type("100"))

# 실습 4. 문자열 숫자와 숫자 비교하기

num1 = 10
num2 = 20
print(num1 + num2)

str1 = "10"
str2 = "20"
print(str1 + str2)

str3 = "100"
str4 = "200"
print(str3 + str4)

print(10 + 20)       # 숫자 덧셈
print("10" + "20")   # 문자열 연결

# 실습 5. bool 값 만들어 확인하기
# 3이 2보다 큰지 확인 >
print(3 > 2)  # True

# 5와 5가 같은지 확인 ==
print(5 == 5)  # True

# 값을 비교하는 자료형 출력하기
print(type(3 > 2))
print(type(5 == 5))

# 실습 6. 변수의 자료형 변경하기
num = 100
print(num)
print(type(num))

num = 100
num = 101.1
print(num)
print(type(num))

num = 100
num = "100"
print(num)
print(type(num))

# 실습 7. 직접 자료형 표현하기
device_temp = 76.0
check_count = 50
device_name = "변압기"
is_normal = True

print(type(device_temp))
print(type(check_count))
print(type(device_name))
print(type(is_normal))

print(device_temp)
print(check_count)
print(device_name)
print(is_normal)

print(check_count < device_temp)  # False
print(check_count > device_temp)  # False
print(check_count == device_temp) # False
print(device_temp > 70)           # True
print(check_count == 50)           # True