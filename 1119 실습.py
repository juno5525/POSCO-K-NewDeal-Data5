##실습

# 1. " [WARNing] " → "WARNING"
title = " [WARNing] "
print(title.strip().strip("[]").upper())


# 2. "temp,pressure,vibration" → "VIBRATION / PRESSURE / TEMP"
sensors = "temp,pressure,vibration"
print(" / ".join(sensors.split(",")[::-1]).upper())


# 3. " EQP-01 , NORMAL , 85.5 " → "normal"
data = " EQP-01 , NORMAL , 85.5 "
print(data.strip().split(",")[1].strip().lower())


# 4. " ###[ PUMP-07 ]### " → "pump_07"
text = " ###[ PUMP-07 ]### "
print(text.strip().strip("#[] ").replace("-", "_").lower())


# 5. " TEMP / Pressure | vibration " → "temp,pressure,vibration"
data = " TEMP / Pressure | vibration "
print(data.strip().replace("/", ",").replace("|", ",").replace(" ", "").lower())


### 실습제출 ###

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
print(f"동일 설비 여부: {same_eqp}")
print(f"온도 변화량: {temp_difference}℃")
print(f"온도 상승률: {increase_rate:.2f}%")
print(f"온도 급상승 여부: {temp_increase}")

#실습2 #|
log = " 2026/11/19 23:58:45 | DELAY=135s | EQP-09 "

# 1. 로그 데이터 분리
log_list = log.strip().split("|")
print(log_list)

# 2. 날짜, 시작 시간, 소요시간, 설비코드 추출
date = log_list[0].strip().split(" ")[0]
start_time = log_list[0].strip().split(" ")[1]
delay = log_list[1].strip().replace("DELAY=", "").replace("s", "")
equipment = log_list[2].strip()
print(date)
print(start_time)
print(delay)
print(equipment)

# 3. 시작 시간을 시, 분, 초로 분리하고 정수형으로 변환
time_list = start_time.split(":")
hour = int(time_list[0])
minute = int(time_list[1])
second = int(time_list[2])
print(hour)
print(minute)
print(second)

# 4. 소요시간 정수형으로 변환
delay = int(delay)
print(delay)

# 5. 시작 시간을 초 단위로 변환
start_seconds = hour * 3600 + minute * 60 + second
print(start_seconds)

# 6. 완료 시간 계산
end_seconds = start_seconds + delay
print(end_seconds)

# 7. 자정 경과 여부 확인
date_changed = end_seconds >= 86400
print(date_changed)

# 8. 완료 시간을 시, 분, 초로 재계산
end_hour = (end_seconds // 3600) % 24
end_minute = (end_seconds % 3600) // 60
end_second = end_seconds % 60
print(end_hour)
print(end_minute)
print(end_second)

# 9. 결과 출력
print("=====설비 작업 정보=====")
print(f"설비코드: {equipment}")
print(f"작업날짜: {date}")
print(f"작업 시작 시간: {hour}시 {minute}분 {second}초")
print(f"소요시간: {delay}초")
print(f"완료시각: {end_hour}시 {end_minute}분 {end_second}초")
print(f"날짜 변경 여부: {date_changed}")

###실습 3.
line1 = " LOT-A | 1,200 | 36 | 8h "
line2 = "lot_a,850,17,5h"

# 1. 두 데이터 분리
line1_list = line1.split("|")
line2_list = line2.split(",")
print(line1_list)
print(line2_list)

# 2. 생산라인 코드 정리
code1 = line1_list[0].strip().upper().replace("-", "_")
code2 = line2_list[0].strip().upper()
print(code1)
print(code2)

# 3. 생산량 정리 및 정수형 변환
production1 = int(line1_list[1].strip().replace(",", ""))
production2 = int(line2_list[1].strip())
print(production1)
print(production2)

# 4. 불량품 수 정리 및 정수형 변환
불량1 = int(line1_list[2].strip())
불량2 = int(line2_list[2].strip())
print(불량1)
print(불량2)

# 5. 가동시간 정리 및 정수형 변환
hour1 = int(line1_list[3].strip().replace("h", ""))
hour2 = int(line2_list[3].strip().replace("h", ""))
print(hour1)
print(hour2)

# 6. 각 데이터의 불량률 계산
불량률1 = 불량1 / production1 * 100
불량률2 = 불량2 / production2 * 100
print(불량률1)
print(불량률2)

# 7. 2차 불량률이 1차보다 낮은지 확인
비교 = 불량률2 < 불량률1
print(비교)

# 8. 라인 코드 일치 여부 확인
same_line = code1 == code2
print(same_line)

# 9. 전체 생산량 및 불량품 수 계산
total_production = production1 + production2
total_불량 = 불량1 + 불량2
print(total_production)
print(total_불량)

# 10. 통합 불량률 계산
total_불량률 = total_불량 / total_production * 100
print(total_불량률)

# 11. 전체 가동시간 및 시간당 평균 생산량 계산
total_hour = hour1 + hour2
average_production = total_production / total_hour
print(total_hour)
print(average_production)

# 12. 최종 판정
final_result = same_line and 비교
print(final_result)

# 13. 결과 출력 (소수점 2째자리)
print("=====생산 데이터 분석====")
print(f"생산라인 코드: {code1}")
print(f"라인 코드 일치: {same_line}")
print(f"[1차 생산] 생산량 {production1}개 / 불량품 {불량1}개")
print(f"불량률: {불량률1:.2f}%")
print(f"[2차 생산] 생산량 {production2}개 / 불량품 {불량2}개")
print(f"불량률: {불량률2:.2f}%")
print(f"[통합분석] 생산량 {total_production}개 / 불량품 {total_불량}개")
print(f"통합 불량률: {total_불량률:.2f}%")
print(f"시간당 평균 생산량: {average_production:.2f}개")
print(f"불량률 개선 여부: {비교}")
print(f"최종판정: {final_result}")