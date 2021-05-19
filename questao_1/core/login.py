import requests

def login(url=None, data_login=None):

    if None in (url, data_login):
        print(f">>>Valor de URL/DATA_LOGIN inválido!")
        return False, None

    with requests.session() as session:
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': 'application/json, text/javascript, */*; q=0.01', 
            'X-Requested-With': 'XMLHttpRequest', 
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
            'Sec-Fetch-Site': 'same-origin', 
            'Sec-Fetch-Mode': 'cors', 
            'Sec-Fetch-Dest': 'empty', 
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
        }

        url_login = "{}/cliente/logar".format(url)        
        #url_login = url
        print(f">>>Logando no site com URL => {url_login}")
        response = session.post(url, headers=headers, data={'data': data_login})

        if not response.ok:
            print(f">>>Erro no request, URL => {response.url} / RESPONSE => {response.status_code}")
            return False, None
        
        return True, session
