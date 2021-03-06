from selenium.webdriver.chrome.webdriver import WebDriver

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError as e:
    raise ImportError('Necessário instalar biblioteca selenium')


def create(cookie=True):
    options = Options()
    options.add_experimental_option("prefs", {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
    })
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-gpu")
    if not cookie:
        options.add_argument("user-data-dir=cache_robo")
    driver: WebDriver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    return driver
