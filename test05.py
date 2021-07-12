import time  #시간을 처리하기 위해 추가
import Person # Person 클래스를 사용

# 클래스 객체
number = [10, 20, 30]
print(dir(number))

p = Person.Person('Heo', 28)
print(p.age)
print(p.name)

print(p.getAge())
print(p.total)
