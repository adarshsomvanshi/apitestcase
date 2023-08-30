import requests

'''This is for GET method.'''
# p = {'page': 2}
# resp =  requests.get('https://reqres.in/api/users', params=p)
# print(resp.url)
# code = resp.status_code
# assert code == 200 , "code doesn't match"
# print(resp.text)
# print(resp.content)
# json_response = resp.json()
# print(json_response['total'])
# print(json_response['total_pages'])
# assert json_response['total'] == 12, 'total page count is not matching'
# print(json_response['data'][0]['email'])
# assert (json_response['data'][0]['email']).endswith('reqres.in'), 'email doestnot match.'
# print(type(resp.headers))
# print(resp.headers)
# print(resp.url)
# print(resp.cookies)
# print(resp.encoding)
# print(json_response['data'][1]['first_name'])
# print(json_response['data'][2]['last_name'])

'''For Post method'''
# new_data = {
#     "email": "eve.holt@reqres.in",
#     "password": "pistol"
# }
# import json
# my_data = open('data.json','r').read()
# resp = requests.post('https://reqres.in/api/register',data=new_data)
# # resp = requests.post('https://reqres.in/api/users',data=json.loads(my_data))
# print(resp)
# print(resp.json()['token'])
# # assert resp.json()['job'] == 'leader', 'job did not match.'
# # print(resp.headers.get('Content-Type'))
# print(resp.status_code)

'''For Update'''
# Put Method
# my_data = {
#     "name": "API",
#     "job": "Testing"
# }
# resp = requests.put('https://reqres.in/api/users/2', data=my_data)
# print(resp)
# print(resp.json())
# print(resp.json()['job'])

# Patch Method
# my_data = {
#     "name": "API"
# }
# resp = requests.patch('https://reqres.in/api/users/2', data=my_data)
# print(resp)
# print(resp.json())
# print(resp.json()['name'])

'''For Delete Method'''

# resp = requests.delete('https://reqres.in/api/users/2')
# # print(resp.json())
# print(resp.status_code)
# assert resp.status_code == 204, 'user deletion fail'

'''For Timeout'''

# resp = requests.get('https://httpbin.org/delay/4', timeout=10)
# print(resp.status_code)
