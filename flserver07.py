# index.html 로딩서버
from flask import Flask, render_template, request
import MySQLdb as mysql

# flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #접속하는 최초 url, GET방식사용
def index():    # 원하는 인덱스파일을 templates폴더에서 선택
    db = mysql.connect('localhost', 'root', '12345', 'test', charset='utf8')
    cur = db.cursor(mysql.cursors.DictCursor)
    cur.execute('SELECT * FROM student')
    result = []
    while True:
        student = cur.fetchone()
        if not student: break

        result.append(student) # 리스트를 추가
        #print(student)
    
    cur.close()
    db.close()
    # 백앤드의 데이터를 프론트앤드로 전달
    return render_template('mysqldata.html', row=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
