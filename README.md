# abc

All aBout Coin

## Summary

요즘 핫한 가상화폐에 대한 정보 공유 및 해외 및 국내 거래소에 있는 코인들에 대한 시세를 확인할 수 있도록 내가 사용하면서 느꼈던 불편한점과 있었으면 좋을 것 같은 기능들을 추가할 예정

## Stack

1. Server : AWS EC2 Ubuntu18.04버전사용
2. Backend : Python3, Django
3. DataBase : 미정 ( MySql 또는 Oracle 사용 예정 NoSQL은 사용하지 않을 것 같다)
4. FrontEnd : React 기반으로 구현할 에정이긴 하다

## Reference

-   Ubuntu 환경에 있는 python버전 변경하기 (https://seongkyun.github.io/others/2019/05/09/ubuntu_python)

## Record

### 2021-03-18

-   기존 AWS EC2 인스턴스에 있던 Ubuntu환경에 python 버전 변경 및 Django 설치 후 퍼블릭 IP 및 로컬 개발환경 연결 확인

### 2021-03-29

-   기존 test app 제거 및 실제 작업할 ABC app 생성
-   template, static 적용

### 시작방법

기본적으로 python3.7버전이 설치되어 있어야함

1. git clone https://github.com/drexqq/abc
2. cd abc_com
3. python manage.py runserver
4. localhost 또는 127.0.0.1 8000번 포트에서
