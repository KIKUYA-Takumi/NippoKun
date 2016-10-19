#にっぽうくん
###概要
「日報は投稿して終わりじゃない！フィードバックをもらってこそ！」をテーマにした日報アプリです。
日報を投稿するのはもちろん、読者が読んだ日報を評価する機能を実装しています。

###デモ
日報作成
![](NippoKun/images/report_entry.jpg)

日報一覧
![](NippoKun/images/index.jpg)

日報採点
![](NippoKun/images/score.jpg)
###Requirements
Python 3.5

PostgreSQL 9.6

Materialize 0.97.6

###SetUp
####secret.pyに記述する情報
使用するデータベースの情報(NAME, USER, PASSWORD, HOST, PORT)とSECRET_KEYの情報を記述する。

####データベースの作成
PostgreSQLでユーザ作成を行う。
create user 'ユーザー名';
alter role ユーザー名 with password 'パスワード';
create database 'データベース名' owner 'ユーザー名';

作成したデータベースの情報をsecret.pyに以下のように記述
db_user = 'ユーザ名'
db_pass = 'パスワード'
db_host = 'localhost'
db_port = '5432'

####SECRET_KEYをsecret.pyに以下のように記述
secret_key = 'シークレットキーにする情報'

###

###License
MIT

###Author
KIKUYA-Takumi