# -*- coding: utf-8 -*-
import re
import json
import requests
from nacl.public import PublicKey, SealedBox
from nacl.encoding import HexEncoder

from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


def encrypt_data(user, password, public_key):
    _box = SealedBox(PublicKey(public_key, encoder=HexEncoder))
    return _box.encrypt(json.dumps(
        {'usuario_cnpj': f"{user}", 'usuario_senha': f"{password}", 'eub': '', 'recaptchaLoginToken': None}).encode()
                        ).hex()


def get_key(session, url):
    global HEADERS
    with session as s:
        resp = s.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.text, 'html.parser').find_all("script", {"src": False})
        for script_line in soup:
            for s_line in script_line.string.split('\n'):
                m_search = re.search(r'.*\b(\w*PUBLIC_KEY\w*)\b.*', s_line)
                if m_search:
                    print(f">>>Localizou a Key => {m_search.string}")
                    return m_search.string.split('=')[-1].strip().replace(';', '').replace('"', '')


def login(url=None, user=None, password=None):
    global HEADERS
    if None in (url, user, password):
        print(f">>>Valor de URL/USER/PASSWORD inválido!")
        return False, None

    with requests.session() as session:

        public_key = get_key(session, url)
        data = encrypt_data(user, password, public_key)

        url_login = f"{url}/cliente/logar"
        print(f">>>Logando no site com URL => {url_login}")
        response = session.post(url_login, headers=HEADERS, data={'data': data})

        if not response.ok:
            print(f">>>Erro no request, URL => {response.url} / RESPONSE => {response.status_code}")
            return False, None
        elif not response.json()['success']:
            print(f">>>Erro de login, Response => {response.json()}")
            return False, None

        return True, session
