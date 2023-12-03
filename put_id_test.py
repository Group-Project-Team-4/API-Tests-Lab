import requests
import json as json_module

# Variable to identify the method and endpoint of the test being run.
name = 'PUT /api/products/2'


# Test application response for a PUT request at /api/products/2
def test():
    # Define URI endpoint
    endpoint = 'http://127.0.0.1:5000/api/products/2'

    # Define new data
    new_data = {
        'name': 'Updated Name',
        'quantity': 10
    }
    # The application only accepts JSON data if the request contains the
    # correct headers for JSON data. Here we define those headers for our
    # request.
    headers = {'Content-Type': 'application/json'}

    # Send request to the endpoint with data and store the response
    res = requests.put(endpoint, data=json_module.dumps({'product': new_data}), headers=headers)
    # Convert to JSON to interact with response data
    json = res.json()

    # Assert that the response indicates success
    assert json['success'], 'JSON response should indicate success.'

    # Get product into easier to access variable
    product = json['product']

    # Iterate over values in new_data to make sure they were updated in the response
    for key, value in new_data.items():
        assert product[key] == value, f'Response data {key} invalid. Expected {value}, received {product[key]}'

    # Negative testing
    # This is intentionally invalid data that is sent to the API to make sure
    # it gives us an error and doesn't process the request.
    invalid_new_data = {
        'quantity': -5,
        'category_id': 'string'
    }

    # Send request to the endpoint with bad data and store the response
    res = requests.put(endpoint, data=json_module.dumps({'product': invalid_new_data}), headers=headers)
    # Convert to JSON to interact with response data
    error_json = res.json()

    # Test that the error message exists and is correctly sent.
    assert error_json['error'] == 'Invalid product information.', 'Negative testing did not yield an error message.'

    # Test clean-up
    # Default data to reset to
    default_data = {
        'name': 'Polo Shirt',
        'quantity': 1
    }

    # Send request to reset data to default
    requests.put(endpoint, data=json_module.dumps({'product': default_data}), headers=headers)


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
