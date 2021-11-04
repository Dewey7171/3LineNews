
Env = 'alche'

if Env == 'local':

    app ={
        'user' : 'root',
        'password' : '1234',
        'host' : '0.0.0.0',
        'charset' : 'utf8',
        'port' : 55222
    }

elif Env == 'alche':
    app = {
        'name' : 'mysql+pymysql',
        'user' : 'root',
        'password': '1234',
        'host': '127.0.0.1',
        'db': 'developer'
    }