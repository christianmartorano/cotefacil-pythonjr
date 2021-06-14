from bs4 import BeautifulSoup
import threading
import queue


class CrawlerThreads(threading.Thread):
    def __init__(self, name, url, session, bucket):
        threading.Thread.__init__(self)
        self.name = name
        self.bucket = bucket
        self.url = url
        self.session = session

    def run(self):
        try:
            self.crawler_categories()
        except Exception as e:
            print(f">>>Exceção => {e}")

    def crawler_categories(self):
        pagina = 0
        arr_products = []

        with self.session as s:

            while True:
                pagina += 1
                url_paginada = "{0}?p={1}".format(self.url, pagina)

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

        self.bucket.put(arr_products)
        self.show_products()

    def show_products(self):
        while True:
            try:
                products = self.bucket.get()
                print(f">>>Foram localizados {len(products)} produtos")
            except queue.Empty:
                pass
            else:
                for product in products:
                    print(f"\n>>>Produto capturado => {product}")
                break


def crawler(session, url):
    index, threads, bucket = 0, [], queue.Queue()
    with session as s:
        response = s.get(url)
        list_menu = BeautifulSoup(response.text, 'html.parser').find_all('li', {"class": "lista-menu-itens"})
        while index < list_menu.__len__():
            url = list_menu.__getitem__(index).find('a').get('href')
            threads.append(
                CrawlerThreads(name=f"Thread-{list_menu.__getitem__(index).text.strip()}", url=url, session=s,
                               bucket=bucket))
            threads.__getitem__(index).run()
            index += 1
