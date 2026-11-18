##인덱싱

word = 'PYTHON'
print(word[0], word[2],word[5]) # P T N
print (word[-6], word[-4], word[-1]) # P T N
print ("python"[2]) # t

word ="Strawberry Moon ~!"
# Son!
print(word[0], word[12], word[14], word[17])
print(word[-18], word[-5], word [-4], word[-1])

word ="SIGNAL"
#SGL
print(word[0], word[2],word[5])

word ="안녕하세요!"
#안녕!(음수)
print(word[-6], word[-5], word[-1])

### 슬라이싱
word = "PYTHON"
# 양수
print(word[0:5])
print(word[:4])
print(word[1:])

#음수
print(word[-3:])
print(word[:-1])

# 문자열[시작:끝:간격] -step 
print(word[0::2])
print(word[::-1])

# ====실습=====
word = "SIGNAL"
print(word[:3])
print(word[2:5])

# 실습 2. 앞 4글자 추출
word = "temp_sensor"
print(word[:4])

# 실습 3. _ 이후 모든 글자 추출
word = "temp_sensor"
print(word[5:])

# 실습 4. 'icecream'에서 'crm' 추출
word = "icecream"
print(word[1::3])
