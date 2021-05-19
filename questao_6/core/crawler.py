from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pprint
import json

def add_author(author, driver, element_link):
    
    link = element_link.get_attribute('href')
    author_json = {"name": author, "birth_date": "{}", "birth_location": "{}", "description": "{}"}

    driver.execute_script(f"window.open('{link}', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    elements = [{'author-born-date': 'birth_date'}, {'author-born-location': 'birth_location'}, {'author-description': 'description'}]

    for el in elements:        
        author_json[[e for e in el.values()][0]] = driver.find_element(By.CLASS_NAME, [k for k in el.keys()][0]).text

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return author_json

def add_tags(element):

    text_element= element.find_element(By.CLASS_NAME, 'text')
    elements    = element.find_elements(By.CLASS_NAME, 'tag')
    quotes_arr  = []
    tags_json   = {"text": f"{text_element.text}", "tags": []}

    for el in elements:
        tags_json['tags'].append(el.text)
    
    quotes_arr.append(tags_json)

    return quotes_arr


def get_quotes(driver, url, author):
    
    count = 0
    json_quotes = {"author": {}, "quotes": []}    
    while True:
        count = count + 1
        driver.get(url.format(count))

        try:
            elements = driver.find_elements(By.CLASS_NAME, 'quote')
        except NoSuchElementException as e:
            print(f">>> Elemento não localizado!")
            return False

        for element in elements:
            try:
                el = element.find_element(By.CLASS_NAME, 'author')            
            except NoSuchElementException as e:
                print(f">>> Elemento não localizado!")
                return False            
            
            if el.text.strip().upper() != author.strip().upper():
                print(f">>> Pulou o autor => {el.text.strip().upper()}")
                continue
            
            print(f">>> Capturando o autor => {el.text.strip().upper()}")
            
            if len(json_quotes["author"]) == 0:
                el_link = element.find_element(By.TAG_NAME, 'a')
                json_quotes["author"] = add_author(author.strip().upper(), driver, el_link)

            tags = []
            tags = add_tags(element)
            if len(tags) > 0:
                json_quotes["quotes"].append(tags)

        resp = input(">>> Deseja continuar capturando (Y/N)?")
        if resp.strip().upper() == 'N':
            driver.close()
            break
    
    print(">>> Dados capturados:")
    pprint.pprint(json_quotes, sort_dicts=False)
