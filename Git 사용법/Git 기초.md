# Git 기초

> Git은 분산형 버전관리시스템(DVCS)이다. 
>
> 소스코드의 이력을 학인하고 협업단계에서 활용 가능 하다.

## 0. 기본설정

윈도우에서 git을 활용하기 위해서는 git bash가 필요하다. [설치링크](https://gitforwindows.org/)

맥에서는 그냥 하면 됨

설치 이후에 commit을 작성하는 author 설정이 필요하다.

```bash
$ git config --global user.name {github username}
$ git config --global user.email {github email}
```

설정 내용을 확인하기 위해서는 아래의 명령어를 입력한다.

```bash
$ git config --global -l
user.email = # my email
user.name = # my name
```

## 로컬 저장소에서 활용하기

gitignore

프로젝트를 진행할 때, git으로 관리하지 않을 파일 혹은 폴더들을 설정할 수 있다.

```
*.xlsx
a.txt
.ipynb_checkpoints/
```

프로젝트 시작시 어떠한 내용을 담아야 할지 모르겠다면

[gitignore](http://gitignore.io/)에서 검색한다.

예) python, r, jupyter notebook

### 1. git 저장소 설정

특정 프로젝트 폴더에서 git을 활용하기 위해서는 아래의 명령어를 입력한다.

```bash
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/my/.git/
student@M160424 MINGW64 ~/Desktop/my (master)

```

* 해당 디렉토리 내에 .git 이라는 숨김폴더가 생성되며, 모든 git과 관련된 동작은 해당 폴더에 기록됨.
* git bash에서 (master)라는 브랜치 정보가 표기된다.

### 2. add

git에서 commit할 대상 파일을 `staging area`로 이동시키는 명령어 이다. 

```bash
$ git add a.txt # 특정 파일을 stage
$ git add images/ # 특정 폴더를 stage
$ git add . # 모든 디렉토리 파일 및 폴더를 stage
```

* add 전 상태

```bash
$ git status
On branch master

No commits yet

Untracked files: # git 이력에 담기지 않은 파일 생성
  (use "git add <file>..." to include in what will be committed)
  # git add 명령어를 통해서 commit될 곳에 추가 
        a.txt
        b.txt

nothing added to commit but untracked files present (use "git add" to track)

```

* add 후 상태

```bash
$ git add a.txt

student@M160424 MINGW64 ~/Desktop/my (master)
$ git status
On branch master

No commits yet

Changes to be committed: # coommit을 변경 사항
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

Untracked files: # tracking 되고 있지 않은 파일들
  (use "git add <file>..." to include in what will be committed)
        b.txt
```

항상 git status 명령어를 통해 현재  상태를 확인하는 것이 중요하다.

## 3. commit

git에서 이력을 남기기 위해서는 commit을 통해 진행

commit 을 남길 때에는 항상 커밋 메시지를 작성

메시지는 해당 이력에 대한 정보를 담는다.

```bash
$ git commit -m 'Add files'
[master (root-commit) eafa4cb] Add files
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt

student@M160424 MINGW64 ~/Desktop/my (master)
$ git log
commit eafa4cb6bef4773ab429f56de6e7a2ac23242ce5 (HEAD -> master)
Author: dasom-elise <addict52@naver.com>
Date:   Mon Dec 9 14:26:26 2019 +0900

    Add files
    
$ git status
On branch master
nothing to commit, working tree clean 

```

이후 변경 사항이 생기면 add -> commit 을 반복하여 저장

 add: commit할 대상 파일 선정

commit: 이력의 확정

## 원격저장소(Remote Repository) 활용하기

> 원격 저장소를 제공해주는 서비스는 다양하다.
>
> 우리는 github를 기준으로 활용



## 0. 기본 설정

Git hub에 비어있는 저장소 생성

## 1. 원격 저장소 설정

```bash
$ git remote add origin https://~
```

원격저장소를 origin이라는 이름으로 https://~ 로 설정한다.

```bash
$ git remote -v
origin  https://github.com/dasom-elise/git-test.git (fetch)
origin  https://github.com/dasom-elise/git-test.git (push)

```

혹시 잘못되었다면 아래의 명령어를 통해 삭제 가능

```bash
$ git remote rm origin
$ git remote -v
```



## 2. Push

원격 저장소에 업로드하기 위해서는 push 명령어가 필요

```bash
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 2.14 KiB | 2.14 MiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/dasom-elise/TIL.git
   e8d63f9..f9c0e9a  master -> master
```

origin으로 설정된 원격 저장소에 push한다.

이후에 변경된 사항(commit)이 발생하였을 때 git push origin master  명령어를 통해서

매번 업로드를 해줄 수 있다.