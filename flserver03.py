# index.html 로딩서버
from flask import Flask, render_template
from werkzeug import datastructures

# flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #접속하는 최초 url
def index():
    # 백엔드에서 데이터를 프론트엔드로 전달!! dictionary ==> key값+value값 
    return render_template('index.html', user='허재현', data={'userid':'jhheo06', 'gender':'male', 'age':'28'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
