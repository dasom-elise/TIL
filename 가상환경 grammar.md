### 2.3 VSCode; 가상환경 진입 관련 설정

> 매번 source ~~ 적으려니 귀찮 -> VS code기능 사용해서 터미널 실행할 때 자동으로
>
> 해당 명령어가 실행되게 만들어보자.

* VScode 왼쪽 메뉴 최하단 Extensions 진입

  * Python 검색해서 제일 상단의 확장프로그램 설치

* ctrl + shift + p

* Python Select Interpreter 클릭

* 사용할 가상환경 목록 출력 -> 클릭 ...(venv)

  .venv/Scripts/activate ...

* 설정이 끝나면 앞으로 터미널을 켜면 자동으로 가상환경에 진입되는 것을 확인할 수 있다.

## 2.4 원격 저장소에 올려둔 가상환경 불러오기

> 기본적으로 원격 저장소에는 가상환경 폴더(`venv`)를 통째로 올리지 않는다.
>
> 그 이유는 가상환경 폴더에는 각종 라이브러리들이 설치되지 않는 장소이기 때문에 파일의 갯수가 많고 용량이 크다.
>
> 또한 개개인의 PC환경이 다르기 때문에 본인의 PC에서 잘 돌아가던 가상환경 세팅이라도 다른 사람에게 통째로 건네주면 그 사람의 환경과 충돌할 위험이 있다.
>
> 따라서 프로젝트 환경에 필요한 패키지 목록만 넘겨주고 이 프로젝트를 받아서 실행 혹은 개발하고 싶은 사람이 해당하는 패키지들을 설치해서 사용할 수 있게 한다. 

* 현재 상황

  * requirements.txt가 만들어져 있고 이 안에 가상환경에 필요한 패키지 목록들이 나열되어 있다. 
  * 내가 작업하고자 하는 환경에는 파이썬과 가상환경이 세팅되어 있다. 

  ###### 1. 원격 저장소 내용 가져오기

  * clone을 이미 받아두었을 경우

    $ git pull origin master

  * 아무것도 없는 경우

  * 원격 저장소의 내용과 내 포털환경의 내용이 동기화된것을 확인할 수 있다. 

```bash
$ git clone GithubURL
```

###### 		2. 가상환경을 설치할 폴더로 들어가서 Git Bash를 연다.

```bash
~/User/바탕화면/TIL/Chatbot
$ 
```

```
TIL/
	Chatbot/
		Python
```



###### 		3. 파이썬 가상환경을 설치한다.

```bash
$ python -m venv venv(가상환경이름)
```

###### 4. 가상환경 폴더 생성확인

```bash
TIL/
	ChatBot/
		venv/
		Python-recap/
		.gitignore
		requirements.txt
```

###### 		5. 가상환경 진입해서 패키지 목록 확인

```bash
$ source venv/Scripts/activate

(venv)

$ pip list
---
---
```

###### 6. 전해받은 requirements에 있는 패키지들을 설치한다. 

* 필요한 패키지들은 Requirements.txt에 저장되어 있다.

  ```bash
  $ pip install -r requirements.txt
  ...
  ... # 설치중
  ```

  ```bash
  $ pip list 
  # requirements에 나열되어 있는 패키지들이 설치된 것을 확인할 수 있다.
  ```

  

