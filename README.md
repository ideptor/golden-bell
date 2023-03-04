# flask

## pyenv install

```
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
```

## docker init

```
docker run -dit -v D:_shared:/shared -p 8882:8882 --name python39 python:3.9
```

## install

```
pyenv local 3.9.1
pip install -r requirements.txt
```

## init db

```
flask db init
flask db migrate
flask db upgrade
```


## run

```
./run.sh
```



## flask chell

### 플라스크 셸 실행하기

플라스크 셸은 명령 프롬프트에서 flask shell 명령으로 실행한다.

```
$ flask shell
Python 3.8.5 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
App: pybo [development]
Instance: C:\projects\myproject\instance
>>> 
```

> 플라스크 셸은 플라스크를 실행하는 데 필요한 환경이 자동으로 설정되어 실행되므로 일반 파이썬 셸과는 다르다.

### 질문 저장하기

다음처럼 Question 모델 객체를 하나 생성하자.

```
>>> from pybo.models import Question, Answer
>>> from datetime import datetime
>>> q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())
```

Question 모델의 create_date 속성은 DateTime 유형이므로 datetime.now 함수로 현재 일시를 대입했다. 하지만 객체 q를 만들었다고 해서 데이터베이스에 질문 데이터가 저장되는 것은 아니다. 데이터베이스에 데이터를 저장하려면 다음처럼 SQLAlchemy의 db 객체를 사용해야 한다.

```
>>> from pybo import db
>>> db.session.add(q)
>>> db.session.commit()
```

  