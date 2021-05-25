from helpers import read_config
from core import login

def main():
    
    no_error, params  = read_config.read()
    no_error, session = login.login(params['url'], params['user'], params['password'])
    crawler_products.crawler(session, params['url'])

if __name__ == "__main__":    
    main()