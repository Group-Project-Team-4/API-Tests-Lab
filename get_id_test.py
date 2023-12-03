import requests

# Variable to identify the method and endpoint of the test being run.
name = 'GET /api/products/2'


# Test application response for a GET request at /api/products/2
def test():
    # Define URI endpoint
    endpoint = 'http://127.0.0.1:5000/api/products/2'

    # Send request to the endpoint and store the response
    res = requests.get(endpoint)
    # Convert to JSON to interact with response data
    json = res.json()

    # Assert that the response indicates success
    assert json['success'], 'JSON response should indicate success.'

    # Get the product values into the 
    product = json['product']

    # IMPORTANT: If you are getting errors from this part of the test, make sure
    # the application's database hasn't been changed by interating with it with Postman
    # or some other interaction with the API.
    # Check each property to validate that it is the same as the expected value.
    assert product['id'] == 2, f'Received product ID incorrect. Expected 2, received: {product["id"]}'
    assert product['category_id'] == 1, f'Received product category ID incorrect. Expected 1, received: {product["category_id"]}'
    assert product['quantity'] == 1, f'Received product quantity incorrect. Expected 1, received: {product["quantity"]}'
    assert product['price'] == 29.99, f'Received product ID incorrect. Expected 1, received: {product["price"]}'
    assert product['name'] == "Polo Shirt", f'Received product ID incorrect. Expected "Polo Shirt" received: {product["name"]}'
    assert product['description'] == "A shirt for looking fancy.", f'Received product ID incorrect. Expected "A shirt for looking fancy." received: {product["description"]}'

    return


# main function for running the test on its own and printing output
def main():
    # Values for printing colored text
    fail_col = '\033[91m'
    pass_col = '\033[92m'
    normal_col = '\033[0m'

    passed = 0
    failed = 0
    try:
        test()
    except AssertionError as e:
        failed += 1
        print(f'{name}  {fail_col}FAILED{normal_col}:  {e}')
    else:
        passed += 1
        print(f'{name}  {pass_col}PASSED{normal_col}')
    finally:
        print(f'\nTest Summary:\n{passed} passed. {failed} failed')


if __name__ == '__main__':
    main()
