import json
import requests

def login_token(session, url=None, username=None, password=None, api_token=None):

    if None in (url, username, password, api_token):
        return False, None, None

    url_login = url.format(api_token)
    data = {'email':'{}'.format(username), 'password': '{}'.format(password)}

    with session as s:
        resp = s.post(url_login, data=json.dumps(data))

        if len(resp.json()['customer']) == 0:
            return False, None, None
        
        print(f">>> Retorno => {resp.json()}")
        return True, s, resp.json()            

def login_api(session, url=None, data=None):

    if None in (url, data):
        return False, None, None

    data = {'username': 'default', 'key': '{}'.format(data)}

    with session as s:
        resp = s.post(url, data=json.dumps(data))
        if resp.json()['api_token'] == '':
            print(f">>> Erro na API")
            return False, None, None

        print(f">>> Retorno => {resp.json()}")
        return True, s, resp.json()                 

def login(url=None, service_key=None):

    if None in (service_key, url):
        return False, None, None

    print(f">>> URL => {url.format(service_key)}")
    session = requests.session()
    resp    = session.get(url.format(service_key))

    if resp.json()['success'] != True:
        print(f">>> Erro no logon !")
        return False, None, None

    print(f">>> Retorno => {resp.json()}")
    return True, session, resp.json()
        