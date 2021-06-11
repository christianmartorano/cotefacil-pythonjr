# -*- coding: utf-8 -*-
from helpers import read_config
from core import login, crawler_products


def main():
    try:

        error, params = read_config.read()
        if not error:
            raise ValueError('>>>Erro ao capturar o arquivo de configuração')

        error, session = login.login(params['url'], params['user'], params['password'])
        if not error:
            raise ValueError('>>>Erro ao efetuar o Login')

        error = crawler_products.crawler(session, params['url'])
        if not error:
            raise ValueError('>>>Erro ao capturar os produtos')

        print('>>>Processo finalizado com sucesso!')
    except ValueError:
        return False

    else:
        return True


if __name__ == "__main__":
    main()
