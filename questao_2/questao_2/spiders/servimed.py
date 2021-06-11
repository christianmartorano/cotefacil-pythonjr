from scrapy.spiders.init import InitSpider
from datetime import datetime
from scrapy import Request
from ..classes import user, header
import json
import os


class ServimedSpider(InitSpider):
    name = 'servimed'
    file_path = "{0}{1}questao_2{1}json_dir{1}".format(os.getcwd(), os.sep)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = user.User()
        self.url_base = 'https://pedidoeletronico.servimed.com.br/'
        self.url_api = 'https://peapi.servimed.com.br'
        self.file = f"{self.file_path}{datetime.now().strftime('%Y%m%d_%H%M')}.jl"

    def init_request(self):
        self.log(f">>> Request inicial")
        yield Request(
            url=self.url_base,
            callback=self.login
        )

    def login(self, response):
        url = f"{self.url_api}/api/usuario/login"
        self.log(f">>>Efetuando request {url}")
        yield Request(
            url=url,
            method='POST',
            body=json.dumps({
                'usuario': 'juliano@farmaprevonline.com.br',
                'senha': 'a007299A'
            }),
            headers={
                'Content-Type': 'application/json'
            },
            callback=self.parse_pedidos)

    def parse_pedidos(self, response):
        self.log(f">>>Resposta do login => {response.body}")

        self.user.jwt = self.user.get_access_token(response.headers.getlist('Set-Cookie'))
        self.user.populate_user(response.json()['usuario'])

        url = f"{self.url_api}/api/Pedido"
        for pagina in range(7):
            payload = {
                'dataInicio': '',
                'dataFim': '',
                'filtro': '',
                'pagina': pagina,
                'registrosPorPagina': 10,
                'codigoExterno': self.user.user['codigoExterno'],
                'codigoUsuario': self.user.user['codigoUsuario'],
                'users': self.user.user['users']
            }
            self.log(f">>>Realizando o pedido => {url} , Payload => {payload}")
            headers = header.header(self.user.user['codigoUsuario'], self.user.jwt).header_mount
            yield Request(
                url=url,
                method='POST',
                headers=headers,
                body=json.dumps(
                    payload
                ),
                callback=self.get_pedidos
            )

    def get_pedidos(self, response):
        self.log(f">>>Chegou pedidos => {response.body}")
        headers = header.header(self.user.user['codigoUsuario'], self.user.jwt).header_mount
        for pedido in json.loads(response.text)['lista']:
            self.log(f">>>Capturando o pedido => {pedido}")
            url = f"{self.url_api}/api/Pedido/ObterTodasInformacoesPedidoPendentePorId/{pedido['id']}"
            yield Request(
                url=url,
                headers=headers,
                callback=self.get_pedidos_response
            )

    def get_pedidos_response(self, response):
        self.log(f"Resposta do Pedido => {response.text}")
        with open(self.file, "a+") as file:
            for pedido in json.loads(response.text)['itens']:
                self.log(f"Salvou o pedido => {pedido}")
                file.write(f"{json.dumps(pedido)}\n")
