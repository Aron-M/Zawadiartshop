import json

def load_product_data_from_json():
    with open('/workspace/Zawadiartshop/products/fixtures/products.json', 'r') as file:
        product_data = json.load(file)
    return product_data