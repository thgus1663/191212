from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/') #앞에있는 서버주소 생략됨
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    return 'hi'

@app.route('/thgus')
def thgus():
    return 'hello thgus'

if __name__ == '__main__' :
    app.run(debug=True)