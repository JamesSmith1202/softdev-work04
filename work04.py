from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "<hr>This is my root page \n My second page can be found <a href=""http://127.0.0.1:5000/page1""> HERE </a><hr>"

@app.route('/page1')
def p1():
    return "<hr>This is my 2nd page \n My third page can be found <a href=""http://127.0.0.1:5000/page2""> HERE </a><hr>"

@app.route('/page2')
def p2():
    return "<hr>This is my 3rd and final page \n<hr>"

if __name__ == '__main__':
    app.run()