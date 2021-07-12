# 복잡한 함수 학습하기

m = 0
n = 1

def func():
    global m, n  # 전역변수 m, n 선언
    m = m + 1
    n = n + 1

func()
print(m, n)

# 중첩함수
def counter(max):
    t = 0

    def output(): # 중첩되어 있으므로 따로 쓸 수 가 없다.
        print('t = {0}'.format(t))

    while t < max:
        output()
        t += 1

counter(10)

# 재귀함수(함수 내에서 자기 자신을 다시 불러서 사용)
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n -1)

print(factorial(10))

# lambda
a = lambda x, y : x * y
print(a(2, 8))

# Closure

def calc(a):
    def add(b):
        return a + b
    return add  # 중첩되어 있는 함수 자체를 리턴

sum = calc(1)
print(sum(2))

@deco 
def encre(x):
    return x + 2

def 