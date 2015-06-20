
Title: Mac OSX, Python3, Virtualenv 환경에서 PyQt5 설치하기
Date: 2015-06-20 15:09
Category: tech
Tags: mac, python, pyqt
Slug: install-pyqt5-in-virtualenv-mac-python3

설치 순서는 다음과 같다.

python3를 homebrew를 통해서 설치한다.
> brew install python3

QT5를 homebrew를 통해서 설치한다. QT5부터 Retina Display를 지원한다. 맥 환경이라면, QT4보단 QT5를 설치하자. 
> brew install qt5

venv (virtualenv) 환경을 만든다. Python3.4에서는 별도로 Virtualenv를 설치하지 않아도 venv라는 이름으로 기본 제공된다.
> python3 -m venv [MYENV]

venv 활성화를 활성화 시킨다.
> source /[MYENV]/bin/activate

sip과 pyqt5를 다운받아서 [MYENV]에 압축을 해제한다. pip을 사용하여 설치하지 않는 이유는 venv환경에서 제대로 설치가 되지 않기 때문이다.

[sip][1]을 설치한다. sip 폴더로 이동하여 직접 설치한다.
> python configure.py && make && make install

마찬가지로 [PyQT5][2]도 동일한 방법으로 설치하면 되지만, sip 때와는 달리 qmake를 이용해야 한다.
> python configure.py -q [qmake directory] -d [venv site-package directory]
> make && make install

[1]: http://sourceforge.net/projects/pyqt/files/sip/
[2]: http://sourceforge.net/projects/pyqt/files/PyQt5/
