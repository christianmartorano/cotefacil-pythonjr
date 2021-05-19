import scrapy
import json

class ServimedSpider(scrapy.Spider):
    name = 'servimed'
    allowed_domains = ['.servimed.com.br']
    start_urls = ['https://pedidoeletronico.servimed.com.br/']

    def parse(self, response):
        self.log(">>> Requisição página: {}".format(response.url))
        return self.login(response)

    def login(self, response):        
        return scrapy.Request(
            method='POST',          
            url = 'https://peapi.servimed.com.br/api/usuario/login',
            body = json.dumps({
               'usuario': 'juliano@farmaprevonline.com.br',
                'senha':  'a007299A'
            }), 
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
            }, 
            callback = self.parse_pedidos)

    def parse_pedidos(self, response):
        pass