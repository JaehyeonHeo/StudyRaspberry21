from flask import Flask

app = Flask(__name__)

@app.route('/') # controller
def index():
    return '''
        <html>
        <head>
            <meta charset='utf-8'>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
            <title>Page Title</title>
            <meta name='viewport' content='width=device-width, initial-scale=1'>
            <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
            <script src='main.js'></script>
        </head>
        <body>
            
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)