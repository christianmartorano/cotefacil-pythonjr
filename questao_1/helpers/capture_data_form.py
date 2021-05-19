from selenium.common.exceptions import NoSuchElementException

def capture(driver, url, username=None, password=None):

    if None in (username, password):
        print(f">>> Não foi encontrado username/password!")
        return False

    driver.get(url)

    try:
        button = driver.find_element_by_class_name('modal-politicas-cookies-button')
        button.click()
    except NoSuchElementException as e:
        pass

    button = driver.find_element_by_class_name('first-label')
    button.click()

    button = driver.find_element_by_id('fazer-login')
    button.click()

    element = driver.find_element_by_id('usuarioCnpj')
    element.send_keys(username)
    element = driver.find_element_by_id('usuarioSenha')
    element.send_keys(password)
    element = driver.find_element_by_id('realizar-login')
    element.submit()

    return driver
