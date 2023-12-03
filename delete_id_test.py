import requests
import json as json_module

# Variable to identify the method and endpoint of the test being run.
name = 'DELETE /api/products/<id>'


# Test application response for a PUT request at /api/products/2
def test():
    # Unlike other tests, this one uses a sample POST request to make a new
    # entry in the database to delete.

    # Define headers for POST request
    headers = {'Content-Type': 'application/json'}

    # Define POST data and send request
    post_data = json_module.dumps({
        'product': {
            'name': 'Test Product',
            'description': 'Sample Test Product Data',
            'price': 9.99,
            'quantity': 5,
            'category_id': 1
        }
    })
    post_endpoint = 'http://127.0.0.1:5000/api/products'
    post_res = requests.post(post_endpoint, data=post_data, headers=headers)

    post_json = post_res.json()

    # Retrieve the ID assigned to the item in the POST request to delete
    post_id = post_json['product']['id']

    # Define URI endpoint
    endpoint = f'http://127.0.0.1:5000/api/products/{post_id}'

    # Send delete request to endpoint and store
    res = requests.delete(endpoint)
    # Store json in easier to access variable
    json = res.json()

    # Make sure response indicates success
    assert json['success'], 'JSON response should indicate success.'


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
