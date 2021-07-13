# 파일 열고 내용 출력하기
try:
    f = open('./data/readme.txt', mode = 'r', encoding='UTF-8') 
    f2 = open('./data/writeme.txt', mode = 'w', encoding='utf-8') # 작성파일 오픈
    line = f.read() # readline() : 한줄씩 띄워서 출력
    while line:
        print(line)
        f2.write(line)
        line = f.read() 

    f2.write('\n추가 내용입니다.')
    # 파일을 오픈하면 무조건 닫아줘야한다.
    f.close() # 파일 닫기
    f2.close()

    print('파일 작성 완료')
except Exception as e:
    print('예외 발생 : {0}'.format(e))

