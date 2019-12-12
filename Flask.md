## FLASK

#### 1) Rendering

> 단순 문자열을 리턴해주지 않고 미리 준비해둔 템플릿을 사용자에게 보여주자.

* templates 폴더 생성

> app.py와 같은 경로에 템플릿 폴더를 생성한다.
>
> ``` 
> flask/
> 	templates/
> 		index.html
> 		...
> 	app.py
> ```

* app.py 코드 수정

  ```python
  from flask import Flask, render_template
  app = Flask(__name__)
  
  @app.route('/')
  def hello_world():
      return render_template('index.html')
  ```

#### 2) Variable Routing

> URL 요청을 통해 사용자에게 임의의 값을 입력받고 데이터를 적절하게 가공해서 사용자에게 응답을 해준다. 

```python
# 인사해주는 페이지
@app.route('/greeting/<string:name>')
def greeting(name):
   # return f'반갑습니다. {name}님! :)'
   return render_template('greeting.html', html_name = name)
```

```python
# 세제곱 돌려주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    # return f'{number}의 세제곱근의 값은 {number**3}입니다.'
    return render_template('cube.html', number=number,result=result)
```

###### 위와 같이 미리 준비해 둔 템플릿을 리턴해 줄 수 있음!

`render_template`

**import 해야하는 패키지 **

```python
from flask import Flask, render_template, request
app = Flask(__name__)
from datetime import datetime
import random
```

#### 3) jinja2 활용하기(템플릿 엔진)

> 함수 안에서 데이터를 가공한 뒤, HTML 태그 형태로 가공해서 보내주는 작업은 너무나 번거롭고 힘들다.

> 따라서 단순 문자면 문자, 리스트면 리스트 그대로 템플릿에 넘겨준 뒤,  Flask에 내장된 템플릿 단에서 제어문을 이용해서 데이터를 가공해보자.

* 조건문

  ```python
  @app.route('/greeting/<string:name>')
  def greeting(name):
     return render_template('greeting.html', html_name = name)
  ```

  ```html
  {% if html_name == '다솜' %}
  <h3>
      충성! {{html_name}} 관리자님 반가워요.
  </h3>
  {% else %}
  <h3>
      {{ html_name }} 님 즐거운 시간되세요.
  </h3>
  {% endif %}
  
  ```

* 반복문

```python

@app.route('/movie0')
def movie():
    movies = ["나이브스 아웃","조커","엔드게임"]
    return render_template('movies.html',movie_list=movies)
```

```html
<h2>
    movie list in 2019
</h2>
<ol>
    {% for movie in movie_list %}
    <li>{{ movie }}</li>
    {% endfor %}
</ol>
```

## Flask 잼잼

##### 1) 신이 나를 만들 때

> 사용자로부터 입력받을 페이지를 렌더링

```python
@app.route('/vonvon')

def vonvon():
  return render_template('vonvon.html')
```

> vonvon.html

```html
<h1><span style="color: tomato;">신이 나를 만들 때</span></h1>
    <form action="/godmademe">
        <br>
        <br>
        <input type="text" name="name"
        placeholder="이름을 입력해주세요"><br>
        <input type="submit" value="시작!">
    </form>
```

>요청 받은 데이터를 가공해서 사용자에게 응답해줌

```python
@app.route('/godmademe')
def godmademe():
  name = request.args.get('name')
  first_options = ['김','커피','오징어','바닐라','바닷물']
  second_options = ['용기','지혜','기억력','IQ','잔머리']
  third_options = ['키','운동신경','음악적 재능','악마의 재능','연기력']
  # 각 데이터 리스트 별로 요소를 하나씩 무작위로 뽑음
  first = random.choice(first_options)
  second = random.choice(second_options)
  third = random.choice(third_options)

  a_value = ['을/를 먹으면서','을/를 들고','을/를 넣고']
  b_value = ['을/를 깨알같이 넣고','을/를 쏟아서', '을/를 깜빡하고']
  c_value = ['을/를 뺐다','을/를 가득 채웠네', '만 줬네']

  a = random.choice(a_value)
  b = random.choice(b_value)
  c = random.choice(c_value)
  return render_template('godmademe.html',name = name, x = first, y = second, z = third, a=a,b=b,c=c)
```

> godmademe.html

```html
<h3> 신이 </h3>
    <h2><span style="color: tomato;"> {{ name }}님을 </span></h2> 
    <span>만들 때</span>
    <br>

    <ul>
       <b> {{x}}  {{a}} </b><br>
       <b> {{y}}  {{b}} </b> <br>
       <b> {{z}}  {{c}} </b> <br>
    </ul>
```























