import requests

from bs4 import BeautifulSoup

def crawler_categories(url, session):
    
    product = {}
    pagina  = 0
    arr_products = []    

    with session as s:

        while True:
            pagina       = pagina + 1
            url_paginada = "{0}?p={1}".format(url, pagina)
                
            reponse = s.get(url_paginada)
            print(f">>>Requisitando a página => {url_paginada}")

            product = BeautifulSoup(response.text, 'html.parser').find_all('div', {'class': 'box-produto box-catalago box-catalago-vitrine'})            
            for p in product:
                product['description'] = p.img.get('title').upper().strip()                
                product['image_url']   = p.img.get('data-src')
                product['manufacturer']= p.find('div', {'class': 'produto-marca mb-1'}).text.upper().strip()
                arr_products.append(product)

                print(f">>>Capturando produto => {product}")

def crawler(session, url):

    with session as s:
        
        response  = s.get(url)
        response  = s.get(url)
        #list_menu = BeautifulSoup(response.text, 'html.parser').find_all('li', {"class": "lista-menu-itens"})
        list_menu = BeautifulSoup(response.text, 'html.parser').find_all('ul', {'class': 'hover-menu'})
        #print(BeautifulSoup(response.text, 'html.parser'))
        #print(f">>>Capturando Links dos Menus => {list_menu}")
        
        for lst in list_menu:
            print(f"{lst}")
            #url = lst.find('a').get('href')
            #print(">>>Capturando produtos da Categoria => {0} / URL => {1}".format(lst.text.replace('\n', '').strip(), url))
            #crawler_categories(url, s)
