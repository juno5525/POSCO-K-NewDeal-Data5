word = 'python'
sentence = 'I Love python'

# upper(), lower() -> 전체 변경
#capitalize(), title() -> 앞글자만 대문자로 변경
print(word.upper())
print(sentence.upper())
print(word.count('p'))

print("normal".upper())
print("WARNING".lower())
print("WARNING 경고".lower())
print("python is good. i have an apple".capitalize())
# Python is good. i have an apple.

print("python is good. i have an apple".title())
# Python Is Good. I Have An Apple
print("hong gil-dong".title())

print('apple'.lower() =='Apple'.lower())


# isupper(), islower()
print('Apple'.islower(),'Apple'.islower())
print('apple'.islower())
print('APPLE'.isupper())

# 1. 'ready'대문자 바꾸기
word = 'ready'
print(word.upper())

# 2. 'WARNING' 소문자로 바꾸기
word2 = 'WARNING'
print(word2.lower())

# 3. 'kim chul soo' 성과 이름 각각 첫자 대문자로 바꾸기
name = 'kim chul soo'
print(name.title())

# 4. 'fault', 'FAULT' 각각 저장 후 동등비교하여 같다는결과 확인
f1 = 'fault'
f2 = 'FAULT'
print(f1.lower() == f2.lower())
print(f1.upper() == f2.upper()) 

# 5. 'ABC', 'abc' 'Abc' -> isupper, islower 각각 검사
print("ABC".isupper())
print("ABC".islower())
print("abc".isupper())
print("abc".islower())
print("Abc".isupper())
print("Abc".islower())

# 6. Sensor_LOG.CSV (소문자 변경후) sensor로 시작하는지, .csv로 끝나는지 확인
sensor = "Sensor_LOG.CSV"
sensor = sensor.lower()
print(sensor.startswith("sensor"))
print(sensor.endswith(".csv"))


######## 문자열 공백 처리########33
#stripp()-> 전체 공백제거, lstrip()-> 앞 공백제거, rstrip()-> 뒤 공백제거
sentence = '  ㅎㅇ 나는 juno.                '
print(sentence+"!!")
print(sentence.strip()+"!!")
print(sentence.lstrip()+"!!")
print(sentence.rstrip()+"!!")

print("============= !절취선! =======".strip("="))

# juno를 대문자로
# 앞뒤공백 제거
# 문자 개수 세기
print(sentence.upper())
print(sentence.upper().strip())
print(len(sentence.upper().strip()))

''' ~11:40
7. '  가동중 ' 변수로 저장 후 -> [가동중] 출력해보기
8. ' 대기 ' 변수로 저장 후 -> [대기 ]/[ 대기] 각각 출력
9. ***경고**** 저장 후 * 제거 후 `경고`만 출력
10. '  WARNING ' -> 'warning' 체이닝으로 출력하기
'''
# 7.
status = "  가동중 "
print("[" + status.strip() + "]")
# 8.
status1 = " 대기 "
print("[" + status1.lstrip() + "]")
print("[" + status1.rstrip() + "]")
# 9.
warning = '***경고****'
print(warning.strip("*"))
# 10.
warning = "  WARNING "
print(warning.strip().lower())
