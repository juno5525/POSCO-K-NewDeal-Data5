numbers = input("숫자 5개 입력: ").split()

numbers[0] = int(numbers[0])
numbers[1] = int(numbers[1])
numbers[2] = int(numbers[2])
numbers[3] = int(numbers[3])
numbers[4] = int(numbers[4])

print("원래 리스트:", numbers)

# 리스트 슬라이싱으로 복사
sorted_numbers = numbers[:]
print("복사한 리스트:", sorted_numbers)

# 정렬
sorted_numbers.sort()
print("정렬한 리스트:", sorted_numbers)

# 중앙값
mid = sorted_numbers[2]

print("중앙값:", mid)
print("원래 리스트:", numbers)
