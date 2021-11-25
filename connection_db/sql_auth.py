
# 라이브 서버에서는 alche가 아닌 local로 변경함

Env = 'testsqlal'

if Env == 'live':

    app ={
        'name' : 'mysql+pymysql',
        'user' : 'root',
        'password': '1234',
        'host': '0.0.0.0',
        'db': 'News',
        'port': '55222'
    }

elif Env == 'testsqlal':
    app = {
        'name' : 'mysql+pymysql',
        'user' : 'root',
        'password': '1234',
        'host': '127.0.0.1',
        'db': 'developer',
        'port': '3306'
    }