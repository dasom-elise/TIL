# Git Branch

> Git 개발 흐름에서 branch는 매우 중요하다.
>
> 독립적인 개발환경을 제공하여 동시에 다양한 작업을 진행할 수 있도록
>
> 만들어 준다.
>
> 일반적으로 branch의 이름은 해당 작업을 나타낸다.

## 1. 기초 명령어

#### - 브랜치 생성하기

```bash
$ git branch # 목록 확인
$ git branch {브랜치 이름} # 브랜치 생성
$ git checkout {브랜치 이름} # 해당 브랜치로 이동
$ git branch -d {브랜치 이름} # 브랜치 삭제하기
```

```bash
$ git checkout -b {브랜치 이름} # {브랜치이름} 생성 및 이름
```

#### - Branch 병합

```bash
(master) $ git merge feature
# master branch로 feature 브랜치 이력 가져오기(병합)
```

