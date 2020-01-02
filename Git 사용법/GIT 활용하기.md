# Github를 통한 work-home 

## 1. 준비사항

* local memory(A - 집)

```bash
$ git clone 원격저장소 URL
```

* local(B - 멀캠)

```bash
$ git init
```

* 원격저장소(github)

## 2. 시나리오

> 작업 전에 pull 작업 후에 push
>
> 작업 과정에서 충돌이 발생할 수 있으니(crash!) 잘못한 것이 아니라 내가 수정하면 된다!

#### 0) 집에서 pull (원격저장소에서 작업하던 파일 불러오기)

```bash
$ git pull origin master
```

#### 1) working in home(commit)

```bash
$ touch a.txt
$ git add .
$ git commit -m '집 - a.txt 추가'
```

#### 2) 원격저장소로 push

```bash
$ git push -u origin master
```

#### 3) 멀캠에서 pull(원격 저장소에서 불러오기)

```bash
$ git pull -u origin master
```

#### 4) 멀캠에서 작업

```bash
$ touch b.txt
$ git add
$ git commit -m '멀티캠퍼스 작업 업로드'
```

#### 5) 원격저장소 Push

```bash
$ git push -u origin master
```

