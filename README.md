
<p align="center">
<img src="https://sistemas.cotefacil.com/CTFLLogan-webapp/images/logo_semsite.png" alt="Prova Cote Fácil">
</p>
<br>

<h1 align="center">Prova Técnica Python🐍 Jr.👶🏻</h1><br>

🏁 Tabela de conteúdos
=================
<!--ts-->
* Tabela de conteúdos
  * 👉[Agradecimentos](#agradecimentos)
* Questões
  * 👉[Questão 1](#questão-1)
  * 👉[Questão 2](#questão-2)
  * 👉[Questão 3](#questão-3)
  * 👉[Questão 4](#questão-4)
  * 👉[Questão 5](#questão-5)
  * 👉[Questão 6](#questão-6)
  * 👉[Questão 7](#questão-7)
<!--te-->

## Agradecimentos:
<p align="justify">Gostaria de primeiramente agradecer ao Gabriel Gobbi equipe da  🔗<a href="https://sistemas.cotefacil.com/CTFLLogan-webapp/login.jsf">@cotefacil</a>, por me conceder a oportunidade de realizar este teste, pois aprendi muito</p><br>

## Questão 1:
<br>
<p align="justify">Foi pedido para realizar o login no site 🔗<a href="https://www.compra-agora.com.br">compre-agora</a> utilizando a 📚biblioteca 🔗<a href="https://github.com/psf/requests">Requests</a> ou framework 🔗<a href="https://github.com/scrapy/scrapy">Scrapy</a> e realizar algumas interações com o site.</p>

<p align="justify">Configurei uma Proxy em meu computador para capturar todas as requisições entre Client 🖥️Server, percebi que os dados enviados ao servidor de Logon eram criptografados após chamar duas páginas Javascript minificada presente nas URL's:</p><br>

 * https://www.compra-agora.com/web/dist/16.main.compreagora.js
 * https://www.compra-agora.com/web/dist/17.main.compreagora.js

<p align="justify">Finalmente era realizado o post request para o endereço:</p><br>

* https://www.compra-agora.com/cliente/logar

<p align="justify">Passando no Body da requisição o parametro data com o valor criptografado, conforme exemplo abaixo:</p><br>

```
data=9e7fc4c1430f828527c92979288785717f6b4ad08b1c5c6462c8bd2be5e94334c46241a33d2987043177d512869e843f4982ed5f852677414f0290316e867279df1362f54c69f90b2317c6cc0b2a9085c1f8f66c56c385b4747125bd8baddbcac1b28c338f3a21bf1c494a8372b90e6331f4298d9b8054dd688fe2727a4ec91c7a93830138adaaac1ef83ac441531bbc7ecba590
```
<br>
<br>

<p align="justify">Capturei a variável PUBLIC_KEY que se encontra no código fonte da página utilizando Regex utilizei a lib pynacl pra criar SealedBox com o JSON abaixo:</p><br>

```
"{"usuario_cnpj":"CNPJ","usuario_senha":"SENHA","eub":"","recaptchaLoginToken":null}"
```

```
def encrypt_data(user, password, public_key):
    _box = SealedBox(PublicKey(public_key, encoder=HexEncoder))
    return _box.encrypt(json.dumps(
        {'usuario_cnpj': f"{user}", 'usuario_senha': f"{password}", 'eub': '', 'recaptchaLoginToken': None}).encode()
                        ).hex()
```

<p align="justify">Após isso relizei o login no site e o crawler dos produtos.</p><br>

 - [ ] Task incompleted
 - [x] Task completed

## Questão 2
<br>
<p align="justify">Foi pedido para realizar o login no site 🔗<a href="https://pedidoeletronico.servimed.com.br/">Servimed</a> framework 🔗<a href="https://github.com/scrapy/scrapy">Scrapy</a> e realizar pedidos no site.</p>

<p align="justify">Tive a oportunidade de conhecer este framework ao qual não havia trabalhado anteriormente em meus estudos descobri que ele é altamente escalonável e pretendo utilizá-lo em meus projetos.</p>

<p align="justify">Consegui realizar o login na plataforma utilizando spider, passando como parâmetro no body da requisição um json com as chaves e modificando o header para aceitar o <i>Content-Type: application/json</i>:</p>

* usuario
* senha


<p align="justify">Após o login inicial foi necessário interagir com a api do site através da url <i>https://peapi.servimed.com.br</i></p><br>
<p align="justify">Outro desafio encontrado foi construir o header da requisição que utilizava 3 parâmetros para efetuar as requisições com a API, são eles:</p>

```
  Content-Type: application/json,
  Accesstoken: @token_jwt
  Loggeduser: @codigo_usuario
```
<p align="justify">No caso do Loggeduser foi necessário somente guardar a resposta da API do site após o logon, que este mesmo traz as informações de logon.
Já no caso do Accesstoken, foi necessário pegar o Set-Cookie da requisição com o token de acesso e utilizar a biblioteca jwt, para obter o token da seguinte forma: 
</p>

```
def get_access_token(self, value):
  access_token = [c for c in value if "accesstoken" in str(c)]
  access_token_jwt = self.jwt.decode(access_token[0].__str__().split('=')[1].split(';')[0], None, None)
  return access_token_jwt['token']
```
<p align="justify">Após isso foi necessário somente realizar as interações com a API do site utilizando a Spider e salvar o retorno dos pedidos em um arquivo <b>.JSON</b>
</p>

- [ ] Task incompleted
- [x] Task completed

## Questão 3
<br>
<p align="justify">Foi pedido para realizar o login no site 🔗<a href="http://coopertotal.nc7i.com/">Coopertotal</a> utilizando a 📚biblioteca 🔗<a href="https://github.com/psf/requests">Requests</a> e realizar pedidos no site.</p>

<p align="justify">Neste exercício utilizei também uma Proxy, para capturar todos os requests realizados entre o 🖥️Client e o Server, nos requests realizados foi capturado o api_token parâmetro required , para realizar todas os requests no site.</p><br>

 - [ ] Task incompleted
 - [x] Task completed

## Questão 4
<br>
<p align="justify">Foi pedido para realizar o Download de um projeto feito em java um <i>Connector-FTP.jar</i> , para realizar essa task, realizei o disassembly do arquivo .jar e no código fonte consegui capturar os parâmetros para logon, como o 🖥️ host / 🤵 user / 🔑 password , após isso conectei ao FTP utilizando um Client e realizar o Download do arquivo <b>"Great Job .txt"</b></p><br>

 - [ ] Task incompleted
 - [x] Task completed

## Questão 5
<br>
<p align="justify">Foi pedido para criar uma estrutura de árvore em Python🐍 neste exercício tive oportunidade de relembrar um pouco sobre estrutura de dados, realizando a pesquisa sobre 🌳árvores binárias.</p><br>

 - [ ] Task incompleted
 - [x] Task completed

## Questão 6
<br>
<p align="justify">Foi pedido para criar um crawler para capturar algumas informações do site 🔗<a href="http://quotes.toscrape.com">Quotes</a> , este crawler aceita como argumento o nome do autor que deseja ser procurado e busca pelas informações do autor na página. Após a captura da primeira página o script pergunta se o usuário deseja continuar a busca na próxima página por mais citações, assim por diante.</p><br>

<p align="center">
<img width="460" height="300" src="https://media.giphy.com/media/ZOjUa4QAhQfi5N56mT/giphy.gif">
</p><br>

 - [ ] Task incompleted
 - [x] Task completed

## Questão 7
<br>
<p align="justify">Foi pedido uma breve explicação sobre alguns serviços da Amazon ☁️Cloud.</p><br>

- [ ] Task incompleted
- [x] Task completed

	
## Autor

 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/28970494?v=4" width="100px;" alt="Christian Santos Martorano - Avatar"/> 
 <sub><b>Christian Santos Martorano</b></sub>

Feito por Christian Santos Martorano 👋🏽 Entre em contato!