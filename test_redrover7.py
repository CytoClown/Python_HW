import pytest
import requests
# from my_module import sum_it
#
# def test_1():
#     assert sum_it(4,8) == 12, 'Wrong result'
#
# def test_2():
#     assert sum_it(5,12) == 15, 'Wrong result'

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200

@pytest.fixture(scope='function')
def booking_id():
    payload = {
        "firstname" : "Jimmy",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2023-10-10",
            "checkout" : "2023-10-17"
        },
        "additionalneeds" : "Breakfast"}

    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id

def test_get_all_bookings():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK
    # print(f'\n{len(response.json())}')
    # assert len(response.json()) == 1223
    print(response.headers)
    assert 'Connection' in response.headers, 'There is no such key'

def test_get_booking_with_id():
    response = requests.get(f'{BASE_URL}/2')
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    assert response_data['firstname'] == 'Eric'
    for key in expected_keys:
        assert key in response_data.keys()
    print(response_data)
    assert response.status_code == STATUS_OK

def test_create_booking():
    payload = {
    "firstname" : "Jimmy",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-10-10",
        "checkout" : "2023-10-17"
    },
    "additionalneeds" : "Breakfast"}

    response = requests.post(BASE_URL, json=payload)
    print(response.json())
    assert response.status_code == STATUS_OK
    id = response.json()['bookingid']
    get_response = requests.get(f'{BASE_URL}/{id}')
    assert get_response.json()['firstname'] == 'Jimmy'

def test_create_booking_with_fixture(booking_id):
    response = requests.get(f'{BASE_URL}/{booking_id}')
    assert response.status_code == STATUS_OK
    assert response.json()['firstname'] == 'Jimmy'

@pytest.fixture(scope='function')
def token():
    payload = {
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == 200
    yield token

def test_delete_new_booking(booking_id, token):
    headers = {'Cookie': f'token={token}'}
    response = requests.delete(f'{BASE_URL}/{booking_id}', headers=headers)
    assert response.status_code == 201
    get_response = requests.get(f'{BASE_URL}/{booking_id}')
    assert get_response.status_code == 404