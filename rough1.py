'''Authentication and authorization'''
# import unittest
# import requests

# class TestAuthentication(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.username = "testuser"
#         self.password = "testpass"

#     def test_successful_login(self):
#         response = requests.post(self.base_url + "/login", json={"username": self.username, "password": self.password})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("access_token", response.json())

#     def test_invalid_credentials(self):
#         response = requests.post(self.base_url + "/login", json={"username": self.username, "password": "wrongpass"})
#         self.assertEqual(response.status_code, 401)
#         self.assertNotIn("access_token", response.json())

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# import requests

# class TestAuthorization(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.valid_token = "valid-access-token"
#         self.invalid_token = "invalid-access-token"

#     def test_authorized_access(self):
#         headers = {"Authorization": f"Bearer {self.valid_token}"}
#         response = requests.get(self.base_url + "/protected-resource", headers=headers)
#         self.assertEqual(response.status_code, 200)

#     def test_unauthorized_access(self):
#         headers = {"Authorization": f"Bearer {self.invalid_token}"}
#         response = requests.get(self.base_url + "/protected-resource", headers=headers)
#         self.assertEqual(response.status_code, 403)

# if __name__ == "__main__":
#     unittest.main()
