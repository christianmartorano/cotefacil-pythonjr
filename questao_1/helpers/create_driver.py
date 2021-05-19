try:
  from seleniumwire import webdriver
except Exception as e:
    print("Necessário instalar biblioteca selenium")
from selenium.webdriver.chrome.options import Options

from helpers import capture_paths

def create(cookie=True):
    download_path = capture_paths.capture_root_directory()
    options  = Options()
    options.add_experimental_option("prefs", {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
    })
    
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-gpu")        
    if cookie == False:        
        options.add_argument("user-data-dir=cache_robo")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    return driver