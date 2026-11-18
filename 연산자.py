## 산술연산자
# + - * / // % **

print(10 + 3) # 13
print(10 - 3) # 7
print(10 * 3) # 30
print(10 / 3) # 3.3333333333333335
print(10 // 3) # 3 (몫)
print(10 % 3) # 1 (나머지)
print(10 ** 3) # 1000 (거듭제곱)

#### 연산자 우선순위
# 우선순위: ** > * / // % > + -
print(10 + 3 * 2) # 16 (곱셈이 먼저 수행됨)
print((10 + 3) * 2) # 26 (괄호 안의 연산이 먼저 수행됨)
print(10 + 3 * 2 ** 2) # 22 (거듭제곱이 먼저 수행됨)

#### 문자열 연산
print("메" + "롱") # 메롱A
print("메롱" * 10) # 메롱메롱메롱메롱메롱메롱메롱메롱메롱메롱

#### 복합 할당 연산자
score = 40
score = score + 10 # score = 40 + 10
score += 10 # score = score + 10
print("score", score) # 60

score = 70
score = score - 10 # score = 70 - 10
score -= 10 # score = score - 10
print("score", score) # 50
