from helpers import read_config
from core import login
from core import create_order


def main():
    no_error, params = read_config.read()
    no_error, session, resp = login.login(params['url_login'], params['service_key'])
    no_error, session, resp = login.login_api(session, params['url_api'], resp['serviceKey'])

    api_token = resp['api_token']

    no_error, session, resp = login.login_token(session, params['url_token'], params['username'], params['password'],
                                                api_token)

    create_order.create(session, params['url_pedido'], api_token)


if __name__ == "__main__":
    main()
