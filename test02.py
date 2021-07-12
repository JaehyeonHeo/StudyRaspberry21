# 구문 테스트

# initialize (초기화)
n = 0

# Loop (반복문)
while True:
    n = n + 1
    if (n >= 100):  # 100 넘으면 중단
        break
    # n이 짝수라면 출력할것
    if (n % 2 == 0):
        print(n)

a = 100
b = 80

if(a > b):
    print('max is {0}'.format(a))
else:
    print('max is {0}'.format(b))

i = -45

if i > 0:
    print('{0} is positive'.format(i))
elif i == 0:
    print('{0} is zero'.format(i))
else:
    print('{0} is negative'.format(i))

for u in [0, 1, 2, 3, 4]:
    print('{0} * 3 = {1}'.format(u, u*3))

for i in range(5):
    print(i * 2)

m = 0
while True:
    m = m + 2
    if (m == 20):  
        continue   # 20 출력 안하고 22로 넘어감
    if (m == 26):
        break       # 반복문 종료

    print(m)

for i in range(5):
    pass            # 아무것도 안하고 지나감


