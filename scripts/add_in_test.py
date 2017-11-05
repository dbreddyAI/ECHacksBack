import requests

from user import uid as user_uuid

BASE_URL = 'http://127.0.0.1'
INSERT_URL = '%s/api/addTransaction' % BASE_URL

# user_uuid = '36fe18b8-9795-40ac-94e5-63a88c838b63'
api_key = '6cc8f23c-ed6b-400c-aff8-24350495b839'

def submit():
    data = {
        'date_of_transaction': 'Jul 2, 2018',
        'amount': '100000',
        'user_uuid': user_uuid,
        'details': 'Tesla Lethbridge, AB',
        'train': True,
        'api_key': api_key
    }

    print(requests.post(INSERT_URL, json=data).content)

if __name__ == "__main__":
    submit()
