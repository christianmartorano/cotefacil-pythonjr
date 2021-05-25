
import re
import requests

from bs4 import BeautifulSoup


HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': 'application/json, text/javascript, */*; q=0.01', 
            'X-Requested-With': 'XMLHttpRequest', 
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',            
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

def encrypt_data(user, password):
    data = {'usuario_cnpj': f"{user}", 'usuario_senha': f"{password}", 'eub': '', 'recaptchaLoginToken': None}
    
    return data

def get_key(session, url):

    with session as s:
        resp = s.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.text, 'html.parser').find_all("script", {"src": False})
        for s in soup:
            for pkey in s.string.split('\n'):
                m_search = re.search(r'.*\b(\w*PUBLIC_KEY\w*)\b.*', pkey)
                if m_search:
                    print(f">>> Localizou a Key => {m_search.string}")
                    return m_search.string.split('=')[-1].strip().replace(';', '').replace('"', '')

def login(url=None, user=None, password=None):

    if None in (url, user, password):
        print(f">>>Valor de URL/USER/PASSWORD inválido!")
        return False, None

    with requests.session() as session:        

        public_key  = get_key(session, url)
        data        = encrypt_data(user, password)

        url_login  = "{}/cliente/logar".format(url)
        print(f">>>Logando no site com URL => {url_login}")
        response = session.post(url, headers=HEADERS, data=data)

        if not response.ok:
            print(f">>>Erro no request, URL => {response.url} / RESPONSE => {response.status_code}")
            return False, None
        
        return True, session
