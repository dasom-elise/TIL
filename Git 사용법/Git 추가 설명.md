# Git 추가 설명

### 1. commit

> commit을 통해 이력을 확정하면 bash값이 부여되며
>
> 이 값을 통해 동일한 커밋인지를 확인한다.

```bash
# WD 변화 X, staging area 변화 X
# 변경사항 X
$ git commit
nothing to commit working tree clean
```

```bash
# WD 변화 O, staging area 비어있을때
$ touch lee.txt
$ git commit
Untracked files:
		lee.txt
nothing added to commit but ntracked files present

```

## commit message 작성하기

> VIM 활용법

```bash
$ git commit

```

* 편집모드( i )
  * 문서 편집 가능

* 명령모드( esc )
  * dd: 해당 줄 삭제
  * :wq: 저장 및 종료
    * w: write(저장)
    * q: quit(종료)
  * :q!: 강제종료
    * ! 강제

## log 활용하기

```bash
$ git log      # 언제 누가 full name의 hash값 제공
$ git log --oneline # 가장 첫줄, 요약된 hash값
$ git log -1 # 
$ git log -1 --oneline
$ git log --oneline --graph
```

* HEAD: 현재 작업하고 있는 상태의 커밋 이려 및 브랜치에 대한 포인터

```bash
4c06b8c (HEAD -> feature/message, origin/feature/message) here
# 나는 현재 f/m 브랜치에 있고
#4c06b8c 커밋의 상태에 있다.
```

* 예시

```bash
$ git log  --oneline
# 나는 master 브랜치에서 # ~~~커밋을 했고

# f/s 브랜치는 #~~~ 이력이고

# 원격저장소(o/m)는 #~~ 이력이다 
```

#### ※ 직전 커밋 메시지 수정

> 아래의 명령어는 커밋이력을 변경하기 때문에 조심해야 한다.
>
> 공개된 저장소에(원격저장소) 이미 push된 이력이라면 절대 해서는 안된다.

```bash
$ git commit --amend
```

##### 커밋 시 특정 파일을 빼먹었을 때

> 만약 staging area에 특정 파일(omit_file.txt)을 올리지 않아서
>
> commit 되지 않았을 때

```bash
$ git add omit_file.txt
$ git commit --amend
```

### 2. Staging Area

* commit 이력이 있는 파일을 수정한 경우

```bash
$ git status
On branch master # 마스터 브랜치에 있다.
Your branch is ahead of 'origin/master' by 5 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit: # commit X staged가 아닌 변경사항 
		# stage로 바꾸려면
  (use "git add/rm <file>..." to update what will be committed)
  		# WD에 있는 변화를 바꾸려면-> 고양이가 다 지움
  		# commit 이후 변경된 사항을 모두 없앰
  		# $ git restore {}
  (use "git restore <file>..." to discard changes in working directory)
        modified:   lunch.txt
        deleted:    master.txt
        deleted:    new.txt
        deleted:    signout.txt
        deleted:    test.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        1001/
# staging area가 비어있습니다. commit에 추가될 변화가 없다.
no changes added to commit (use "git add" and/or "git commit -a")
```

```bash
$ git add 12.txt
$ git status
On branch master
# commit이 될 변화
# commit 명령-> 아래 이력이 남음
Your branch is up to date with 'origin/master'.
Changes to be committed:
		# unstage 하기 위해
  (use "git restore --staged <file>..." to unstage)
        new file:   12.txt
```



* commit 이력이 없는 파일의 경우

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.
# tracking 되고 있지 않는 파일 -> commit(이력)에 한번도 관리된 적 없다.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        12.txt
# 커밋할 것도 없고 (staging area가 비어있고)
# 트래킹 되고 있지 않는 파일도 없다.
nothing added to commit but untracked files present (use "git add" to track) 
```



### Add 취소하기

```bash
$ git restore --staged <file>
```

* 구버전에서는 아래의 명령어 사용

```bash
$ git reset HEAD <file>

```

### Working Directory

> git 에서 모든 commit은 되돌릴 수 없다.
>
> 다만 아래의 WD 내용을 삭제하는 것은 되돌릴 수 있다. 

```bash
$ git restore <file>
```

* 구버전 에서는 아래의 명령어를 사용해야 한다.

```bash
$ git checkout -- <file>
```

## Stash

> stash는 변경사항을 임시로 저장 해놓는 공간이다.

###### >예시상황

1. test branch에서 a.txt 변경 후 commit
2. master branch에서 a.txt 수정(add / commit 하지 않음)
3. 이후 merge > error

```bash
$ git merge test
# 현재 merge 명령어로 인해 아래의 파일이 덮어쓰여질 수 있다.
error: Your local changes to the following files would be overwritten by merge:
        a.txt
# commit -> 이력 확장을 해서 merge시 충돌 나는 상황으로 
# stash -> working directory를 잠시 비워놓고
Please commit your changes or stash them before you merge.
Aborting
Updating b75b4a1..d2cefc1
```

#### 명령어

```bash
$ git stash  # stash 공간에 저장
Saved working directory and index state WIP on master: b75b4a1 a.txt
$ git stash list  # stash 공간 내용 확인
stash@{0}: WIP on master: b75b4a1 a.txt
$ git stash pop     # stash 공간에서 적용(apply)하고 목록에서 삭제(drop)
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (afee39ef18b85756e448873e285433a88033c944)
```

###### >예시상황 해결

```bash
$ git stash
$ git merge test
$ git stash pop
# 충돌 해결 후 작업 이어나가기
```

### Reset   &   Revert

reset은 공개된 저장소에 push이력이 있으면 하면 안됨.

이미 push 이력이 있기 때문

주로 revert로 돌아갔습니다 commit을 새로 올려줘야함

> commit 이력을 되돌리는 작업을 한다.

* Reset: 이력을 삭제
  * --mixed: 기본옵션,  지금 작성된 내용을 유지, commit이후 변경사항 staging area에 보관
  * --hard: 해당 commit 이후 변경사항 모두 삭제 `**주의**  ` 
  * --soft:  해당 commit이후 변경사항 및 wd 내용까지 모두 보관

```bash
$ git log --oneline
f70d3de (HEAD -> master) b.txt
893a37d test
1ac1b87 a.txt
d2cefc1 (test) b.txt
b75b4a1 a.txt
$ git reset 893a37d
$ git log --oneline
893a37d (HEAD -> master) test # b.txt 가 지워짐
1ac1b87 a.txt
d2cefc1 (test) b.txt
b75b4a1 a.txt
```

* Revert: 되돌렸다는 이력을 남김

```bash
$ git log --oneline
3df75d5 (HEAD -> master) b.txt
60b3948 Revert "a.txt"
893a37d test
1ac1b87 a.txt
d2cefc1 (test) b.txt
b75b4a1 a.txt
$ git revert 60b3948
[master fb63df2] Revert "Revert "a.txt""
 1 file changed, 4 deletions(-)
$ git log --oneline
fb63df2 (HEAD -> master) Revert "Revert "a.txt""
3df75d5 b.txt
60b3948 Revert "a.txt"
893a37d test
1ac1b87 a.txt
d2cefc1 (test) b.txt
b75b4a1 a.txt

```

