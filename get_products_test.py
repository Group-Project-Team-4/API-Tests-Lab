import requests

# Variable to identify the method and endpoint of the test being run.
name = 'GET /api/products'


# Test application response for a GET request at /api/products
def test():
    # Define URI endpoint
    endpoint = 'http://127.0.0.1:5000/api/products'

    # Send request to the endpoint and store the response
    res = requests.get(endpoint)
    # Convert to JSON to interact with response data
    json = res.json()

    # Assert that the response indicates success
    assert json['success'], 'JSON response should indicate success.'

    # Iterate through every item in the products list to make sure they contain
    # all of the necessary values and that they are all of the correct type.
    for item in json['products']:
        # Informative error string that gets formatted for each
        error_string = 'Item {} is invalid: expected {}, received: {} (type: {})'
        assert isinstance(item['id'], int), error_string.format('id', 'int', item['id'], type(item['id']))
        assert isinstance(item['category_id'], int), error_string.format('category ID', 'int', item['category_id'], type(item['category_id']))
        assert isinstance(item['quantity'], int), error_string.format('quantity', 'int', item['quantity'], type(item['quantity']))
        assert isinstance(item['price'], float), error_string.format('price', 'float', item['price'], type(item[price]))
        assert isinstance(item['name'], str), error_string.format('name', 'str', item['name'], type(item['name']))
        assert isinstance(item['description'], str), error_string.format('description', 'str', item['description'], type(item['description']))

    return


# main function for running the test on its own and printing output
def main():
    # Values for printing colored text
    fail_col = '\033[91m'
    pass_col = '\033[92m'
    normal_col = '\033[0m'

    # Counters for the tests passed and failed
    passed = 0
    failed = 0
    try:
        # Run the test
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
