# 변수 기본
n = 1
name = "Jaehyeon"
n = n + 2
value = 1.2 * n

print('{0} = 1.2 * {1}'.format(value, n))
print(name)

# 문자(배열) 인덱스 활용 방법
greeting = 'Hello World'
print(greeting[0])
print(greeting[5:8]) # 5번 인덱스 부터 8번 전까지만 출력
print(greeting[:2]) # 0~1인덱스 글자 출력
print(greeting[-2]) # 뒤에서 두번째 글자 출력

numbers = [0, 1, 2, 3]
names = ['kim', 'Lee', 'Park', 'Choi']
arry = numbers + names

print(numbers)
print(numbers[0])
print(numbers[0:2])

print(arry)
print(arry * 2)

# Tuple : 중간에 값을 변경하기 어렵다
person = ('Kim', 24, 'male')
print(person)
# person[1] = 45 --> 불가능
name, age, gender = person
print(gender)
print(name)
print(age)