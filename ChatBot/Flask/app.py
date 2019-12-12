from flask import Flask, render_template, request
app = Flask(__name__)
from datetime import datetime
import random
# @app.route('/')
# def hello_world():
#     return 'Hello^-^!♡'

@app.route('/')
def hello_world():
    return render_template('index.html')

## 폴더명은 반드시 templates(스펠링이 틀리면 작동하지 않음)


@app.route('/mulcam')
def mulcam():
    return '20층 스카이라운지 맛집!'

@app.route('/dday')
def dday():
    today = datetime.now()
    new_year = datetime(2020, 1, 1)
    result = new_year - today
    return f'<h1>한 살 더 먹기까지{result.days}일 남았습니다. 시간이 벌써..!</h1>'


@app.route('/greeting/<string:name>')
def greeting(name):
   # return f'반갑습니다. {name}님! :)'
   return render_template('greeting.html', html_name = name)

@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    # return f'{number}의 세제곱근의 값은 {number**3}입니다.'
    return render_template('cube.html', number=number,result=result)

# 인원 수에 맞게 메뉴를 추천해주는 페이지
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['보쌈수육정식',"고추잡채덮밥",'돼지불백',"샐러드","연어덮밥"]
    order = random.sample(menu,people)
    return str(order)


@app.route('/movie0')
def movie():
    movies = ["나이브스 아웃","조커","엔드게임"]
    return render_template('movies.html',movie_list=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age =  request.args.get('age')
    return render_template('pong.html',age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')





## app.py 가장 하단에 위치
# 1. 앞으로 flask run으로 서버를 켜는게 아니라 python app.py로 서버를 실행
# 2. 내용이 바뀌어도 서버를 껐다켜지 않아도 반영된다.

if __name__== '__main__':
    app.run(debug=True)

