data1 = " pump-07 | 08:30 |  TEMP=085.5C | STATUS=normal "
data2 = "PUMP_07,09:00,92.0C,WARNING"

# 1. 두 데이터를 구분자에 맞춰 분리
data1_list = data1.split("|")
data2_list = data2.split(",")

# 2. 설비 코드 정리
eqp1 = data1_list[0].strip().upper().replace("-", "_")
eqp2 = data2_list[0].strip().upper().replace("-", "_")

# 3. 시간 정리
time1 = data1_list[1].strip()
time2 = data2_list[1].strip()

# 4. 온도 정리
temp1 = data1_list[2].strip().replace("TEMP=", "").replace("C", "")
temp2 = data2_list[2].strip().replace("C", "")

temperature1 = float(temp1)
temperature2 = float(temp2)

# 5. 상태 정리
status1 = data1_list[3].strip().replace("STATUS=", "").lower()
status2 = data2_list[3].strip().lower()

# 6. 설비 코드 일치 여부
same_eqp = eqp1 == eqp2

# 7. 온도 변화량
temp_difference = temperature2 - temperature1

# 8. 온도 상승률
increase_rate = (temp_difference / temperature1) * 100

# 9. 온도 급상승 여부
temp_increase = same_eqp and temp_difference >= 6

# 10. 결과 출력
print("====센서 데이터 비교====")
print(f"설비코드: {eqp1}")
print(f"최초측정: {time1} / {temperature1}℃ / {status1}")
print(f"최근측정: {time2} / {temperature2}℃ / {status2}")
print()
print(f"동일 설비 여부: {same_eqp}")
print(f"온도 변화량: {temp_difference}℃")
print(f"온도 상승률: {increase_rate:.2f}%")
print(f"온도 급상승 여부: {temp_increase}")
