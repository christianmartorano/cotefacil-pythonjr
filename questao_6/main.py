import sys

from helpers import read_config
from helpers import create_driver

from core import crawler

BANNER = '''
    
 █▀▀ █▀█ ▄▀█ █░█░█ █░░ █▀▀ █▀█   █▀█ █░█ █▀█ ▀█▀ █▀▀ █▀
 █▄▄ █▀▄ █▀█ ▀▄▀▄▀ █▄▄ ██▄ █▀▄   ▀▀█ █▄█ █▄█ ░█░ ██▄ ▄█'''

HELP = '''

>>>  𝙋𝙖𝙨𝙨 𝙖𝙪𝙩𝙝𝙤𝙧 𝙬𝙞𝙩𝙝 𝙖𝙧𝙜𝙪𝙢𝙚𝙣𝙩 𝙚𝙭.:

>>>  𝙥𝙮𝙩𝙝𝙤𝙣 𝙢𝙖𝙞𝙣 ❞𝙅.𝙆. 𝙍𝙤𝙬𝙡𝙞𝙣𝙜❞

'''


def main():
    print(BANNER)

    try:
        author = sys.argv[1]
    except IndexError as e:
        print(HELP)
        return False

    no_error, params = read_config.read()

    driver = create_driver.create()

    crawler.get_quotes(driver, params['url'], author)

    return True


if __name__ == "__main__":
    main()
