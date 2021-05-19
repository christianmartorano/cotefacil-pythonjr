
<p align="center">
<img src="https://sistemas.cotefacil.com/CTFLLogan-webapp/images/logo_semsite.png" alt="Prova Cote Fácil">
</p>
<br>

<h1 align="center">Prova Técnica Python🐍 Jr.👶🏻</h1><br>

<p>Gostaria de primeiramente agradecer ao Gabriel Gobbi equipe da  🔗<a href="https://sistemas.cotefacil.com/CTFLLogan-webapp/login.jsf">@cotefacil</a>, por me conceder a oportunidade de realizar este teste, pois aprendi muito</p><br>

## Questão 1:
<br>
<p>Foi pedido para realizar o login no site 🔗<a href="https://www.compra-agora.com.br">compre-agora</a> utilizando a 📚biblioteca 🔗<a href="https://github.com/psf/requests">Requests</a> ou framework 🔗<a href="https://github.com/scrapy/scrapy">Scrapy</a> e realizar algumas interações com o site.</p>

<p>Configurei uma Proxy em meu computador para capturar todas as requisições entre Client 🖥️Server, percebi que os dados enviados ao servidor de Logon eram criptografados após chamar duas páginas Javascript minificada presente nas URL's:</p><br>

 * https://www.compra-agora.com/web/dist/16.main.compreagora.js
 * https://www.compra-agora.com/web/dist/17.main.compreagora.js

<p>Finalmente era realizado o post request para o endereço:</p><br>

* https://www.compra-agora.com/cliente/logar

<p>Passando no Body da requisição o parametro data com o valor criptografado, conforme exemplo abaixo:</p><br>

<code>
data=9e7fc4c1430f828527c92979288785717f6b4ad08b1c5c6462c8bd2be5e94334c46241a33d2987043177d512869e843f4982ed5f852677414f0290316e867279df1362f54c69f90b2317c6cc0b2a9085c1f8f66c56c385b4747125bd8baddbcac1b28c338f3a21bf1c494a8372b90e6331f4298d9b8054dd688fe2727a4ec91c7a93830138adaaac1ef83ac441531bbc7ecba590
</code>
<br>
<p>Tentei recriar essa hash usando a lib pynacl utilizando o usuário e senha que nos foi passado no teste, utilizando o encoding hexadecimal e várias combinações de hash como <b>sha512</b> porém não tive sucesso.</p><br>

<p>Tentei criar um robô utilizando o selenium wire, que grava as requisições realizadas pelo Browser pois descobri em meus testes que o valor de data continua válido para ser utilizado mais de uma vez durante um espaço de tempo, porém devido ao tempo do teste não consegui concluir.</p><br>

 - [x] Task incompleta
 - [ ] Task completed

## Questão 2
<br>
<p>Foi pedido para realizar o login no site 🔗<a href="https://pedidoeletronico.servimed.com.br/">Servimed</a> framework 🔗<a href="https://github.com/scrapy/scrapy">Scrapy</a> e realizar pedidos no site.</p>

<p>Tive a oportunidade de conhecer este framework ao qual não havia trabalhado anteriormente em meus estudos descobri que ele é altamente escalonável e pretendo utilizá-lo em meus projetos.</p>

<p>Consegui realizar o login na plataforma utilizando spider, passando como parâmetro no body da requisição um json com as chaves:</p>

* usuario
* senha

***E modificando o Header incluindo o Content-Type: application/json***

<p>Não tive tempo hábil de estudar o framwork a fundo, para decifrar o porque quando fazia o fetch para a url ele me retornava o javascript inicial da página ao invés da página em si.</p><br>

- [x] Task incompleta
- [ ] Task completed

## Questão 3
<br>
<p>Foi pedido para realizar o login no site 🔗<a href="http://coopertotal.nc7i.com/">Coopertotal</a> utilizando a 📚biblioteca 🔗<a href="https://github.com/psf/requests">Requests</a> e realizar pedidos no site.</p>

<p>Neste exercício utilizei também uma Proxy, para capturar todos os requests realizados entre o 🖥️Client e o Server, nos requests realizados foi capturado o api_token parâmetro required , para realizar todas os requests no site.</p><br>

 - [ ] Task incompleta
 - [x] Task completed

## Questão 4
<br>
<p>Foi pedido para realizar o Download de um projeto feito em java um Connector-FTP , para realizar essa task, realizei o disassembly do arquivo .jar e no código fonte consegui capturar os parâmetros para logon, como o host / user / password , após isso conectei ao FTP utilizando um Client e realizar o Download do arquivo <b>"Great Job .txt"</b></p><br>

 - [ ] Task incompleta
 - [x] Task completed

## Questão 5
<br>
<p>Foi pedido para criar uma estrutura de árvore em Python🐍 neste exercício tive oportunidade de relembrar um pouco sobre estrutura de dados, realizando a pesquisa sobre 🌳árvores binárias.</p><br>

 - [ ] Task incompleta
 - [x] Task completed

## Questão 6
<br>
<p>Foi pedido para criar um crawler para capturar algumas informações do site 🔗<a href="http://quotes.toscrape.com">Quotes</a> , este crawler aceita como argumento o nome do autor que deseja ser procurado e busca pelas informações do autor na página. Após a captura da primeira página o script pergunta se o usuário deseja continuar a busca na próxima página por mais citações, assim por diante.</p><br>

<p align="center">
<img width="460" height="300" src="https://media.giphy.com/media/ZOjUa4QAhQfi5N56mT/giphy.gif">
</p>
<br>
 - [ ] Task incompleta
 - [x] Task completed

## Questão 7
<br>
<p>Foi pedido uma breve explicação sobre alguns serviços da Amazon ☁️Cloud.</p><br>

- [ ] Task incompleta
- [x] Task completed