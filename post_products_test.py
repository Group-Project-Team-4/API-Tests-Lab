import requests
import json as json_module

# Variable to identify the method and endpoint of the test being run.
name = 'POST /api/products'


# Test application response for a PUT request at /api/products/2
def test():
    # Define URI endpoint
    endpoint = 'http://127.0.0.1:5000/api/products'

    # Define test data to send to the application
    req_product_data = {
                'name': 'Test Product',
                'description': 'Sample Test Product Data',
                'price': 9.99,
                'quantity': 5,
                'category_id': 1
            }

    # The application only accepts JSON data if the request contains the
    # correct headers for JSON data. Here we define those headers for our
    # request.
    headers = {'Content-Type': 'application/json'}

    # Send request to the endpoint with data and store the response
    res = requests.post(endpoint, data=json_module.dumps({'product': req_product_data}), headers=headers)
    # Convert to JSON to interact with response data
    json = res.json()

    # Assert that the response indicates success
    assert json['success'], 'JSON response should indicate success.'

    # Get product field from JSON to more easily access it
    product = json['product']

    # The ID property is is a unique key value which gets incremented
    # automatically by the app's database, meaning it can't be manipulated in
    # POST/PUT requests. Because of this, there isn't a reliable way to test
    # the validity of the ID received back from the request without assuming a
    # lot, and assuming too much in testing makes the tests more difficult
    # to use. To make the tests as educational and easy to use as possible, no
    # part of the tests will check the validity of ID values.

    # The response from POST requests for this API functions exactly the same
    # as making a separate GET /api/product/<id> request with the new ID, so we
    # do not have to send another GET request to test the validity of this POST
    # request's response.

    # Check that the response body contains the same data sent in the request
    for key, value in req_product_data.items():
        assert product[key] == value, f'Response data {key} invalid. Expected {value}, received {product[key]}'

    # This part of the test is now complete, but it is very bad practice to not
    # clean up testing sample values after testing is concluded.
    # This removes the data that we added to the database, reverting it as much
    # as possible to the state it had before the test. As mentioned above, the
    # ID value is already incremented and will not be reset until the user runs
    # `flask --app clothing_store init-db` again.
    requests.delete(endpoint + '/' + str(product['id']))

    # Negative testing
    # This is intentionally invalid data that is sent to the API to make sure
    # it gives us an error and doesn't process the request.
    invalid_product_data = {
                'name': 'Invalid Test Product',
                'description': 'Sample Test Bad Data',
                'price': 9.99,
                'quantity': -5,
                'category_id': 'string'
            }

    # Send request to the endpoint with bad data and store the response
    res = requests.post(endpoint, data=json_module.dumps({'product': invalid_product_data}), headers=headers)
    # Convert to JSON to interact with response data
    error_json = res.json()

    # Test that the error message exists and is correctly sent.
    assert error_json['error'] == 'Invalid product information.', 'Negative testing did not yield an error message.'

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
