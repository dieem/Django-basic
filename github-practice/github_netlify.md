# Github & 배포
---
## Github와 Netlify  
#### Git
* 파일의 변천사를 저장하는 역할
* 코드의 변화를 기록

#### Github
* git과 코드를 저장하고 관리하는 서비스
* 개발자의 포트폴리오 역할

#### Netlify
* https://www.netlify.com/
* 배포과정

  > 작성한 코드 업로드 -> (Github) -> Github 연동 호스팅 -> Netlify를 통해 배포
  
---
## Github 협업
#### 자주 쓰는 Git 명령어
|명령어|설명|
|------|------|
|git init git | 저장소를 초기화 |
|git add . | 폴더에 변경된 모든 파일 staging area에 올리기 | 
|git commit -m "커밋에 대한 설명" | 유사시 돌아갈 수 있는 저장소의 체크 포인트 생성 |
|git remote add origin http://원격 저장소 주소.git | 원격 저장소(remote repository) 연결 |
|git branch 브랜치명 | 새로운 브랜치를 생성 |
|git checkout 브랜치명 | 해당 브랜치로 이동 |
|git push origin 브랜치 | 원격 저장소의 특정 브랜치에 프로젝트 저장 |
|git pull origin 브랜치 | 원격 저장소의 특정 브랜치에서 변경사항 pull 해오기 |
|git clone http://원격 저장소 주소.git | 원격 저장소에 있는 파일 전체 복사 |
|git status | git 저장소의 상태를 확인 |
  
#
  
#### Github를 이용한 협업
1. 원격 저장소 생성 (Github repository 생성)
2. 팀원을 Collaborator로 추가
3. 초기 프로젝트 push
4. 팀원들의 로컬에 프로젝트 pull
5. 팀원 각자의 브랜치를 생성하여 작업
6. 브랜치에 작업한 내용을 push
7. Master와 merge 하기 전 pull request
8. Pull request 확인 후 Master와 merge
  
#
  
#### Fork를 이용한 협업
1. 작업 하고 싶은 Repository fork 해오기
2. 자신의 로컬에서 작업
3. 변경사항을 자신의 브랜치에 push
4. 원본 레포지토리 소유자에게 Pull request 요청
5. 소유자가 pull request를 승인하여 merge하면 자동으로 collaborator 추가  
  
---
