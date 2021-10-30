
Env = 'local'

if Env == 'local':

    app ={
        'user' : 'root',
        'password' : '1234',
        'host' : '0.0.0.0',
        'charset' : 'utf8',
        'port' : '55222'
    }

elif Env == 'Dev':
    app = {
        'user': 'dev',
        'password': '1234',
        'host': '0.0.0.0',
        'charset': 'utf8',
        'port': '12345'
    }



