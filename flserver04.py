# index.html 로딩서버
from flask import Flask, render_template, request
from werkzeug.exceptions import MethodNotAllowed

# flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #접속하는 최초 url, GET방식사용
def index():
    return render_template('login.html')

@app.route('/post', methods=['POST'])
def post():
    userid = request.form.get('userid')
    password = request.form.get('password')
    msg = "{0} / {1}".format(userid, password)
    return msg

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
