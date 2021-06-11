import json
from bs4 import BeautifulSoup


def crawler_categories(url, session):
    pagina = 0
    arr_products = []

    with session as s:

        while True:
            pagina += 1
            url_paginada = "{0}?p={1}".format(url, pagina)

            response = s.get(url_paginada)
            print(f">>>Requisitando a página => {url_paginada}")

            if BeautifulSoup(response.text, 'html.parser').find('p', {'class': 'py-5 text-center nada-encontrado'}):
                break

            products_elements = BeautifulSoup(response.text, 'html.parser').find_all('div', {
                'class': 'box-produto box-catalago box-catalago-vitrine'})
            for p in products_elements:
                product = dict(description=p.img.get('title').upper().strip(), image_url=p.img.get('data-src'),
                               manufacturer=p.find('div', {'class': 'produto-marca mb-1'}).text.upper().strip())
                arr_products.append(product)

        return arr_products


def show_products(products):
    print(f">>>Foram localizados {len(products)} produtos")
    for product in products:
        print(f"\n>>>Produto capturado => {product}")


def crawler(session, url):
    with session as s:
        response = s.get(url)
        list_menu = BeautifulSoup(response.text, 'html.parser').find_all('li', {"class": "lista-menu-itens"})
        for lst in list_menu:
            url = lst.find('a').get('href')
            print("\n>>>Capturando produtos da Categoria => {0}".format(lst.text.replace('\n', '').strip()))
            arr_products = crawler_categories(url, s)

    show_products(arr_products)

    return True
