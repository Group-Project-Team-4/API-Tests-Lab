import get_products_test
import get_id_test
import post_products_test
import put_id_test
import delete_id_test

# Values for printing colored text
fail_col = '\033[91m'
pass_col = '\033[92m'
normal_col = '\033[0m'
def main():
    # Count tests passed and failed
    passed = 0
    failed = 0

    # Test GET /api/products
    try:
        get_products_test.test()
    except AssertionError as e:
        failed += 1
        print(f'{get_products_test.name}  {fail_col}FAILED{normal_col}  {e}')
    else:
        passed += 1
        print(f'{get_products_test.name}  {pass_col}PASSED{normal_col}')

    # Test GET /api/products/<id>
    try:
        get_id_test.test()
    except AssertionError as e:
        failed += 1
        print(f'{get_id_test.name}  {fail_col}FAILED{normal_col}  {e}')
    else:
        passed += 1
        print(f'{get_id_test.name}  {pass_col}PASSED{normal_col}')

    # Test POST /api/products
    try:
        post_products_test.test()
    except AssertionError as e:
        failed += 1
        print(f'{post_products_test.name}  {fail_col}FAILED{normal_col}  {e}')
    else:
        passed += 1
        print(f'{post_products_test.name}  {pass_col}PASSED{normal_col}')

    # Test PUT /api/products/2
    try:
        put_id_test.test()
    except AssertionError as e:
        failed += 1
        print(f'{put_id_test.name}  {fail_col}FAILED{normal_col}  {e}')
    else:
        passed += 1
        print(f'{put_id_test.name}  {pass_col}PASSED{normal_col}')

    # Test DELETE /api/products/<id>
    try:
        delete_id_test.test()
    except AssertionError as e:
        failed += 1
        print(f'{delete_id_test.name}  {fail_col}FAILED{normal_col}  {e}')
    else:
        passed += 1
        print(f'{delete_id_test.name}  {pass_col}PASSED{normal_col}')

    print(f'\nTest Summary:\n{passed} passed. {failed} failed')


if __name__ == '__main__':
    main()
