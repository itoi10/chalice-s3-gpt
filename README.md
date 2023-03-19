# chalice

AWS認証情報を設定しておく
```sh
$ cat ~/.aws/credentials
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY

$ cat ~/.aws/config
[default]
output=json
region=YOUR_REGION
```

chalice アプリ作成
```sh
$ python -V
Python 3.9.16

$ pip install chalice

$ chalice new-project chatgpt-api
Your project has been generated in ./chatgpt-api
```

ローカル起動
```sh
$ cd chatgpt-api

$ chalice local
Serving on http://127.0.0.1:8000
```
