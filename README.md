## python-flask-sample

#### DB(Sqlite3 for windows)
* 必要なファイルをDLし、パスを通しておく
* DBファイルは事前に作成が必要
```
$ sqlite3 flask-sample.sqlite

$ create table user(id, username, email, password)
```
* ここまで実施すれば、Intellijから接続して操作できる。