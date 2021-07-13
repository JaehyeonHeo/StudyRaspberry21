# index.html 로딩서버
from flask import Flask, render_template

# flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #접속하는 최초 url
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

# Flask는 Python으로 서버를 만들어서 Html로 만든 페이지를 띄우는 것 !