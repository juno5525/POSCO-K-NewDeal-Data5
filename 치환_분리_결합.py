#replace -> 문자열을 바꾸거나 지우기
print(" 정 상 가 동".replace(" ", "-"))
print(" 정 상 가 동".replace(" ", "")) # 공백제거
print("falut".replace("falut", "고장"))

#"3,000" -> 숫자 3000
print(int("3,000".replace(",","")))
#010-1234 5678 -> 01012345678
print("010-1234 5678".replace("-","").replace(" ",""))

# 문자열.split(생략가능구분자)
list = [10, 20, 30, "hello", False]
print(list[3])
print(list[1])

coffee = "에스프레소 카페라떼 아메리카노"
print(coffee.split())
coffee_list = coffee.split()
print(coffee_list[2])

print("사과, 배, 감".split(","))
print("사과, 배, 감".split(",")[2])
date = '2026-11-19'
day = date.split("-")[2]
print(day)

coffee = "에스프레소 카페라떼 아메리카노"
print(coffee.split(" ", 1))

'''
#① '설비 정상 가동' 저장 → ② '정상'을 '점검'으로 바꿔 출력
#① 'PUMP A 03' 저장 → ② 공백 기준 분리하여 리스트 출력
#① 'a,b,c,d' 저장 → ② ','을 기준으로 분리
#① 'a,b,c,d' 저장 → ② 첫 번째 ','을 기준으로 한 번만 나누기
'''

# 1. '설비 정상 가동' 저장 → '정상'을 '점검'으로 바꿔 출력
equ = "설비 정상 가동"
print(equ.replace("정상", "점검"))

# 2. 'PUMP A 03' 저장 → 공백 기준 분리하여 리스트 출력
pump = "PUMP A 03"
print(pump.split())

# 3. 'a,b,c,d' 저장 → ','을 기준으로 분리
text = "a,b,c,d"
print(text.split(","))

# 4. 'a,b,c,d' 저장 → 첫 번째 ','을 기준으로 한 번만 나누기
text = "a,b,c,d"
print(text.split(",", 1))

# 구분자가 될 문자열 .join([리스트])
list = ['2026', '11','19']
#2026-11-19, 2026.11.19
print('-'.join(list))
print('.'.join(list))

'''
#1. ① ['2025','01','15'] 준비 → ② '-'으로 연결하여 합치기

#2. 2025·1·15 를 '-' 와 ','로 총 2가지 방법을 사용해 이어서 출력

# 3. ① '2025/01/15' 저장 → ② '/'을 기준으로 나눈 후 '-' 으로 합치기

#4. ① '1, NORMAL ,25.3' 저장
② ',' 기준으로 나누어 1번 인덱스를 공백 제거와 소문자로 변환해 출력
'''
#1
date = ['2025', '01', '15']
print('-'.join(date))
date = ['2025', '1', '15']

#2
print('-'.join(date))
print(','.join(date))

#3
date = '2025/01/15'
date_list = date.split("/")
print('-'.join(date_list))

#4
data = '1, NORMAL ,25.3'
data_list = data.split(",")
print(data_list[1].strip().lower())

'''
1. text = "   PyThOn   " ->"python"

2. phone = "  010 - 1234 - 5678  " -> "01012345678"

3. name = "   kIM    cHUL   sOO   " -> "Kim Chul Soo"

4. filename = "  Sensor Data 2026.CSV  " -> "sensor_data_2026.csv"

5. data = "TEMP----PRESSURE----STATUS" -> "TEMP-PRESSURE-STATUS"
'''

# 1. "   PyThOn   " -> "python"
text = "   PyThOn   "
print(text.strip().lower())


# 2. "  010 - 1234 - 5678  " -> "01012345678"
phone = "  010 - 1234 - 5678  "
print(phone.strip().replace(" ", "").replace("-", ""))


# 3. "   kIM    cHUL   sOO   " -> "Kim Chul Soo"
name = "   kIM    cHUL   sOO   "
print(name.strip().title())


# 4. "  Sensor Data 2026.CSV  " -> "sensor_data_2026.csv"
filename = "  Sensor Data 2026.CSV  "
print(filename.strip().lower().replace(" ", "_"))


# 5. "TEMP----PRESSURE----STATUS" -> "TEMP-PRESSURE-STATUS"
data = "TEMP----PRESSURE----STATUS"
print(data.replace("----", "-"))