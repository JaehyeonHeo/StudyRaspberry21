# index.html 로딩서버
from flask import Flask, render_template, request

# flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #접속하는 최초 url, GET방식사용
def index():    # 원하는 인덱스파일을 templates폴더에서 선택
    return render_template('login.html')

@app.route('/get', methods=['GET'])  # get방식
def get():
    user = request.args.get('user')
    msg = "{0}".format(user)
    return msg

@app.route('/post', methods=['POST'])  # post방식
def post():
    userid = request.form.get('userid')
    password = request.form.get('password')
    msg = "{0} / {1}".format(userid, password)
    friends = ['Lee', 'Park', 'Kim']
    return render_template('result.html', result=msg, friends=friends)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
