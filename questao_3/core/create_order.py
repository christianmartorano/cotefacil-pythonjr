import json


def send_request(session, url, data):
    with session as s:
        resp = s.post(url, data=json.dumps(data))
        print(f">>>Resposta => {resp.json()}")

        return s, resp.json()


def add_order(product, quantity):
    return {"ean": f"{product['ean']}", "discount": product['discount'], "price": product['list_price'],
            "product_id": product['product_id'],
            "quantity": quantity, "name": f"{product['name']}", "manufacturer": f"{product['manufacturer']}",
            "tax": product['price_tax'], "category": f"{product['category']}"}


def add_cart(session, products, api_token):
    urls = ['https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/cart_add&api_token={}'.format(api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/commercial_condition&api_token={}'.format(
                api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/shipping_method&api_token={}'.format(
                api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/payment_method&api_token={}'.format(
                api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/order_add&api_token={}'.format(api_token)]

    data = [{"products": products},
            {"commercial_condition_id": "103", "commercial_condition": "CONDIÇÃO DIAMANTE A PRAZO", "pay_term_id": "1",
             "name": "42 DIAS", "code": "001", "minimum_value": "100"},
            {"shipping_method": "supplier.1"}, {"payment_method": "bank_slip"},
            {"customer_date_delivery": "", "customer_order_id": ""}]

    index = 0
    with session as s:
        for u in urls:
            print(f">>> Data => {data[index]}")
            resp = s.post(u, data=json.dumps(data[index]))
            index = index + 1
            print(f">>> Resposta => {resp.json()}")

        return resp.json()


def create(session, url=None, api_token=None):
    if None in (url, api_token):
        return False, None, None

    urls = ['https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/address&api_token={}|0'.format(api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/payment_methods&api_token={}|1'.format(
                api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/commercial_conditions&api_token={}|0'.format(
                api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/shipping_methods&api_token={}|1'.format(
                api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/get_cart_ui&api_token={}|2'.format(
                api_token),
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/messageProducts|1',
            'https://coopertotal.nc7i.com/index.php?route=api/v2/rest_cooper/produtos_integracao_target&api_token={}|-1'.format(
                api_token)]

    data = [{"address_id": "535"}, '[object Object]', {"address_id": "535", "commercial_condition_id": "103"},
            {"pay_term_id": "1", "commercial_condition_id": "103"}]

    resp = session.get(url)
    for u in urls:
        url_product = u.split('|')[0]
        data_product = data[int(u.split('|')[-1])]
        print(f">>>URL => {url_product} , DATA => {data_product}")

        session, resp = send_request(session, url_product, data_product)

    arr_eans = [
        '7896241225530',
        '7897595901927',
        '7896241225547',
        '7896007547654'
    ]

    products = [
        {'ean': '7896241225530', 'quantity': 1},
        {'ean': '7897595901927', 'quantity': 2},
        {'ean': '7896241225547', 'quantity': 1},
        {'ean': '7896007547654', 'quantity': 0}
    ]

    products_json = resp['products']
    arr_orders = []

    for product in products_json:
        try:
            index = arr_eans.index(product['ean'])
        except ValueError as e:
            continue

        print(f">>> Localizou o produto => {product['name']} , quantidade => {product['quantity']}")
        if product['quantity'].__int__() > 0:
            resp = add_order(product, products[index]['quantity'])
            arr_orders.append(resp)

    resp = add_cart(session, arr_orders, api_token)
    print(f">>> Retorno => {resp}")
