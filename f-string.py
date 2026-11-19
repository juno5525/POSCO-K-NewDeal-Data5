name = '홍길동'
age = 25
# 홍길동님은 25살입니다.
sentence = name+'님은 '+str(age) + "살입니다."
print(name+'님은 '+str(age) + "살입니다.")

print(sentence)
sentence2 = f"{name}님은 {age}살입니다."
print(sentence2)

code ='EQP-001'

print(f'설비 코드 {code} 점검 완료: 온도 {25}도')
hours = 3
print(f'총 가동시간(분): {hours*60}분')
value =3.141592
print(f"PI 소수점 둘째 자리까지: {value:.2f}")
print(f"PI 소수점 넷째 자리까지: {value:.4f}")

# 1.
equipment = "변압기"
temperature = 85
print(f"{equipment} 온도: {temperature}도")

#2.
score1 = 80
score2 = 90
score3 = 100
print(f"평균 점수: {(score1 + score2 + score3) / 3}")

#3.
value = 87.456
print(f"소수점 첫째 자리: {value:.1f}")
print(f"소수점 둘째 자리: {value:.2f}")

#4.
data = '  5 , sensor_2 , WARNING , 0.78912  '
data_list = data.strip().split(",")
number = data_list[0].strip()
sensor = data_list[1].strip()
status = data_list[2].strip().lower()
value = float(data_list[3].strip())
print(f"번호: {number}")
print(f"센서: {sensor}")
print(f"상태: {status}")
print(f"측정값: {value:.2f}")