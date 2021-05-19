from helpers import read_config
from core    import login
from core    import crawler_products

def main():
    
    no_error, params  = read_config.read()
    no_error, session = login.login(params['url'], params['data'])
    crawler_products.crawler(session, params['url'])

if __name__ == "__main__":    
    main()