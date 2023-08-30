import requests
import pytest
import json

BASE_URL = 'https://reqres.in/'

def test_get_request():
        p = {'page':2}
        response = requests.get(url=BASE_URL + 'api/users/', params=p)
        assert 200 == response.status_code
        data = response.json()
        assert 2 == data['total_pages']
        print(data)

def test_post_request():
        # new_data = {
        #     "name": "morpheus",
        #     "job": "leader"
        # }
        my_data =  open('data.json','r').read()
        # response = requests.post(url=BASE_URL + 'api/users', data=new_data)
        response = requests.post(url=BASE_URL + 'api/users', data=json.loads(my_data))
        user_data = response.json()
        assert 'Abc' == user_data['name']
        assert 201 == response.status_code

def test_put_request():
        user_id = 2
        update_user = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.put(url=BASE_URL + f'api/users/{user_id}', data = update_user)
        assert 200 == response.status_code
        updated_data = response.json()
        assert 'leader' == updated_data['job']
        user_id_check = 1
        response1 = requests.put(url=BASE_URL + f'api/users/{user_id_check}')
        assert response1.status_code == 200
        
def test_patch_request():
        user_id = 2
        update_user = {
            "job": "Dev Ops"
        }
        response = requests.patch(url=BASE_URL + f'api/users/{user_id}', data = update_user)
        assert 200 == response.status_code
        updated_data = response.json()
        assert 'Dev Ops' == updated_data['job']

def test_delete_request():
        user_id = 2
        response = requests.delete(url=BASE_URL + f'api/users/{user_id}')
        assert 204 == response.status_code
        