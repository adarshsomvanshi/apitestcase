'''Test For valid api key'''
# import unittest
# import requests

# class TestAPIKeyValidation(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.valid_api_key = "valid-api-key"
#         self.invalid_short_api_key = "abc"
#         self.invalid_long_api_key = "a" * 101  # Assuming max length is 100 characters

#     def test_valid_api_key(self):
#         headers = {"Authorization": f"Bearer {self.valid_api_key}"}
#         response = requests.get(self.base_url + "/endpoint", headers=headers)
#         self.assertEqual(response.status_code, 200)

#     def test_invalid_short_api_key(self):
#         headers = {"Authorization": f"Bearer {self.invalid_short_api_key}"}
#         response = requests.get(self.base_url + "/endpoint", headers=headers)
#         self.assertEqual(response.status_code, 401)

#     def test_invalid_long_api_key(self):
#         headers = {"Authorization": f"Bearer {self.invalid_long_api_key}"}
#         response = requests.get(self.base_url + "/endpoint", headers=headers)
#         self.assertEqual(response.status_code, 401)

# if __name__ == "__main__":
#     unittest.main()

'''Test For Valid JSON and XML response'''
# import unittest
# import requests

# class TestAPIKeyResponse(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.valid_api_key = "valid-api-key"

#     def test_json_api_with_valid_key(self):
#         headers = {"Authorization": f"Bearer {self.valid_api_key}"}
#         response = requests.get(self.base_url + "/json-endpoint", headers=headers)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.headers["Content-Type"], "application/json")

#         # You might add more assertions here to validate the JSON response content

#     def test_xml_api_with_valid_key(self):
#         headers = {"Authorization": f"Bearer {self.valid_api_key}"}
#         response = requests.get(self.base_url + "/xml-endpoint", headers=headers)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.headers["Content-Type"], "application/xml")

#         # You might add more assertions here to validate the XML response content

# if __name__ == "__main__":
#     unittest.main()

'''XML Schema Validation'''
# import unittest
# import requests
# import xmlschema

# class TestXMLSchemaValidation(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.schema_file = "path/to/xml/schema.xsd"  # Replace with your XML schema file path

#     def test_xml_response_validation(self):
#         response = requests.get(self.base_url + "/xml-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Load the XML schema
#         xs = xmlschema.XMLSchema(self.schema_file)

#         # Parse the response content as XML
#         xml_content = response.content.decode("utf-8")
#         xml_root = xs.to_etree(xml_content)

#         # Validate the XML content against the schema
#         self.assertTrue(xs.is_valid(xml_root))

# if __name__ == "__main__":
#     unittest.main()

'''JSON Schema Validation'''
# import unittest
# import requests
# import jsonschema

# class TestJSONSchemaValidation(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.schema_file = "path/to/json/schema.json"  # Replace with your JSON schema file path

#     def test_json_response_validation(self):
#         response = requests.get(self.base_url + "/json-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Load the JSON schema
#         with open(self.schema_file, "r") as schema_file:
            # schema = jsonschema.Draft7Validator(json.load(schema_file))     

#         # Parse the response content as JSON
#         json_content = response.json()

#         # Validate the JSON content against the schema
#         self.assertTrue(schema.is_valid(json_content))

# if __name__ == "__main__":
#     unittest.main()

'''Verify Parse response Data'''
# import unittest
# import requests

# class TestResponseParsing(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_parse_response(self):
#         response = requests.get(self.base_url + "/api-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Parse the response content as JSON
#         response_json = response.json()

#         # Verify specific portions of the parsed response data
#         self.assertIn("key1", response_json)
#         self.assertEqual(response_json["key2"], "expected_value")
#         self.assertTrue(response_json["key3"])

#         # You can add more assertions to verify other portions of the response

# if __name__ == "__main__":
#     unittest.main()

'''Verify Json schema Validation, Field Type and the Mandatory field.'''
# import unittest
# import requests
# import jsonschema

# class TestAPIValidation(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.schema_file = "path/to/json/schema.json"  # Replace with your JSON schema file path

#     def test_json_schema_validation(self):
#         response = requests.get(self.base_url + "/api-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Load the JSON schema
#         with open(self.schema_file, "r") as schema_file:
#             schema = jsonschema.Draft7Validator(json.load(schema_file))

#         # Parse the response content as JSON
#         json_content = response.json()

#         # Validate the JSON content against the schema
#         self.assertTrue(schema.is_valid(json_content))

#     def test_field_types(self):
#         response = requests.get(self.base_url + "/api-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Parse the response content as JSON
#         response_json = response.json()

#         # Verify the types of specific fields
#         self.assertIsInstance(response_json.get("field1"), int)
#         self.assertIsInstance(response_json.get("field2"), str)
#         self.assertIsInstance(response_json.get("field3"), bool)
#         # Add more assertions for other fields and their expected types

#     def test_mandatory_fields(self):
#         response = requests.get(self.base_url + "/api-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Parse the response content as JSON
#         response_json = response.json()

#         # Verify the presence of mandatory fields
#         self.assertIn("mandatory_field1", response_json)
#         self.assertIn("mandatory_field2", response_json)
#         # Add more assertions for other mandatory fields

# if __name__ == "__main__":
#     unittest.main()

'''Valid Response Header and Negative Testcases'''
# import unittest
# import requests

# class TestAPIResponse(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_response_headers(self):
#         response = requests.get(self.base_url + "/api-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Verify specific response headers
#         self.assertEqual(response.headers["Content-Type"], "application/json")
#         self.assertIn("X-RateLimit-Limit", response.headers)
#         self.assertIn("X-RateLimit-Remaining", response.headers)

#     def test_negative_response(self):
#         response = requests.get(self.base_url + "/invalid-endpoint")
        
#         # Verify that the response has the expected status code
#         self.assertEqual(response.status_code, 404)

#         # Verify that the response content contains an error message
#         error_message = response.json().get("message", "")
#         self.assertEqual(error_message, "Endpoint not found")

# if __name__ == "__main__":
#     unittest.main()

'''Verify and Identify the handling of API error codes'''
# write testcases for SQL injection in api autonomus testing.
# import unittest
# import requests

# class TestAPIErrorHandling(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_invalid_endpoint(self):
#         response = requests.get(self.base_url + "/invalid-endpoint")
        
#         # Verify that the response has the expected status code (e.g., 404)
#         self.assertEqual(response.status_code, 404)

#         # Verify that the response content contains an appropriate error message
#         error_message = response.json().get("message", "")
#         self.assertEqual(error_message, "Endpoint not found")

#     def test_unauthorized_request(self):
#         response = requests.get(self.base_url + "/restricted-endpoint")
        
#         # Verify that the response has the expected status code (e.g., 401)
#         self.assertEqual(response.status_code, 401)

#         # Verify that the response content contains an appropriate error message
#         error_message = response.json().get("message", "")
#         self.assertEqual(error_message, "Unauthorized request")

#     # Add more test cases to cover other error scenarios
#     # For example: test_bad_request, test_server_error, etc.

# if __name__ == "__main__":
#     unittest.main()

'''Response HTTP status Code'''
# import unittest
# import requests

# class TestAPIResponse(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_successful_response(self):
#         response = requests.get(self.base_url + "/success-endpoint")
        
#         # Verify that the response has a successful status code (2xx)
#         self.assertTrue(response.status_code >= 200 and response.status_code < 300)

#     def test_client_error_response(self):
#         response = requests.get(self.base_url + "/client-error-endpoint")
        
#         # Verify that the response has a client error status code (4xx)
#         self.assertTrue(response.status_code >= 400 and response.status_code < 500)

#     def test_server_error_response(self):
#         response = requests.get(self.base_url + "/server-error-endpoint")
        
#         # Verify that the response has a server error status code (5xx)
#         self.assertTrue(response.status_code >= 500 and response.status_code < 600)

# if __name__ == "__main__":
#     unittest.main()

'''Valid Response payload'''
# import unittest
# import requests
# import json

# class TestAPIResponsePayload(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_json_response_format(self):
#         response = requests.get(self.base_url + "/json-endpoint")
#         self.assertEqual(response.status_code, 200)

#         try:
#             response_json = response.json()  # Try parsing the response as JSON
#             self.assertTrue(isinstance(response_json, dict) or isinstance(response_json, list))
#         except json.JSONDecodeError:
#             self.fail("Failed to parse response JSON")

#     def test_xml_response_format(self):
#         response = requests.get(self.base_url + "/xml-endpoint")
#         self.assertEqual(response.status_code, 200)

#         # Validate XML response format (you may need an XML parsing library)
#         # Example: lxml, xml.etree.ElementTree, etc.

#         # If using lxml:
#         try:
#             from lxml import etree
#             xml_parser = etree.XMLParser(dtd_validation=True)
#             xml_content = response.content
#             etree.fromstring(xml_content, parser=xml_parser)
#         except ImportError:
#             self.skipTest("lxml library not available")

# if __name__ == "__main__":
#     unittest.main()

'''Chain Request verification'''
# import unittest
# import requests

# class TestAPIChaining(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.user_id = 1  # Replace with an actual user ID

#     def test_request_chaining(self):
#         # Step 1: Get user details
#         user_response = requests.get(self.base_url + f"/users/{self.user_id}")
#         self.assertEqual(user_response.status_code, 200)
#         user_data = user_response.json()

#         # Step 2: Get user's posts
#         posts_response = requests.get(self.base_url + f"/users/{self.user_id}/posts")
#         self.assertEqual(posts_response.status_code, 200)
#         posts_data = posts_response.json()

#         # Verify that user details and posts are consistent
#         self.assertEqual(user_data["id"], self.user_id)
#         for post in posts_data:
#             self.assertEqual(post["userId"], self.user_id)

#     # Add more test cases to test other API chaining scenarios

# if __name__ == "__main__":
#     unittest.main()

'''Verify APIs for input parameters'''
# import unittest
# import requests

# class TestAPIWithInputParameters(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_valid_input_parameter(self):
#         query_param = "parameter_value"
#         response = requests.get(self.base_url + f"/endpoint?query_param={query_param}")
#         self.assertEqual(response.status_code, 200)

#         # Verify the response data based on the input parameter
#         response_data = response.json()
#         self.assertEqual(response_data["status"], "success")
#         self.assertEqual(response_data["data"]["input_param"], query_param)

#     def test_missing_input_parameter(self):
#         response = requests.get(self.base_url + "/endpoint")
#         self.assertEqual(response.status_code, 400)

#         # Verify the response contains an appropriate error message
#         error_message = response.json().get("message", "")
#         self.assertEqual(error_message, "Missing required input parameter")

#     # Add more test cases to cover other input parameter scenarios
#     # For example: test_invalid_input_parameter, test_edge_cases, etc.

# if __name__ == "__main__":
#     unittest.main()

'''Check Database Integrity Testcases'''
# import unittest
# import requests
# import sqlite3  # Use the appropriate database library for your database system

# class TestDatabaseIntegrity(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.db_connection = sqlite3.connect("test.db")  # Replace with your database connection

#     def tearDown(self):
#         self.db_connection.close()

#     def test_create_resource(self):
#         # Send a POST request to create a resource through the API
#         response = requests.post(self.base_url + "/create-resource", json={"name": "New Resource"})
#         self.assertEqual(response.status_code, 201)

#         # Verify that the resource was created in the database
#         cursor = self.db_connection.cursor()
#         cursor.execute("SELECT * FROM resources WHERE name = 'New Resource'")
#         result = cursor.fetchone()
#         self.assertIsNotNone(result)
#         cursor.close()

#     def test_update_resource(self):
#         # Send a PUT request to update a resource through the API
#         response = requests.put(self.base_url + "/update-resource/1", json={"name": "Updated Resource"})
#         self.assertEqual(response.status_code, 200)

#         # Verify that the resource was updated in the database
#         cursor = self.db_connection.cursor()
#         cursor.execute("SELECT * FROM resources WHERE id = 1")
#         result = cursor.fetchone()
#         self.assertIsNotNone(result)
#         self.assertEqual(result[1], "Updated Resource")
#         cursor.close()

#     def test_delete_resource(self):
#         # Send a DELETE request to delete a resource through the API
#         response = requests.delete(self.base_url + "/delete-resource/1")
#         self.assertEqual(response.status_code, 204)

#         # Verify that the resource was deleted from the database
#         cursor = self.db_connection.cursor()
#         cursor.execute("SELECT * FROM resources WHERE id = 1")
#         result = cursor.fetchone()
#         self.assertIsNone(result)
#         cursor.close()

# if __name__ == "__main__":
#     unittest.main()

'''Verify File Upload TestCases'''
# import unittest
# import requests

# class TestFileUpload(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_successful_file_upload(self):
#         with open("test_file.txt", "rb") as file:
#             files = {"file": ("test_file.txt", file)}
#             response = requests.post(self.base_url + "/upload", files=files)
        
#         self.assertEqual(response.status_code, 201)
#         self.assertIn("file_id", response.json())  # Assuming the response includes a file ID

#     def test_file_upload_without_file(self):
#         response = requests.post(self.base_url + "/upload")
#         self.assertEqual(response.status_code, 400)
#         self.assertIn("error", response.json())  # Assuming the response includes an error message

#     def test_invalid_file_format(self):
#         with open("invalid_file.exe", "rb") as file:
#             files = {"file": ("invalid_file.exe", file)}
#             response = requests.post(self.base_url + "/upload", files=files)
        
#         self.assertEqual(response.status_code, 400)
#         self.assertIn("error", response.json())  # Assuming the response includes an error message

#     def test_large_file_upload(self):
#         with open("large_file.zip", "rb") as file:
#             files = {"file": ("large_file.zip", file)}
#             response = requests.post(self.base_url + "/upload", files=files)
        
#         self.assertEqual(response.status_code, 413)  # Assuming HTTP status 413 for Payload Too Large


# if __name__ == "__main__":
#     unittest.main()

'''End-to-End CRUD flow'''
# import unittest
# import requests

# class TestCRUDFlow(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"
#         self.resource_id = None  # To store the created resource ID

#     def tearDown(self):
#         if self.resource_id:
#             # Clean up by deleting the created resource
#             response = requests.delete(self.base_url + f"/resources/{self.resource_id}")
#             self.assertEqual(response.status_code, 204)

#     def test_create_resource(self):
#         # Send a POST request to create a resource
#         response = requests.post(self.base_url + "/resources", json={"name": "New Resource"})
#         self.assertEqual(response.status_code, 201)
#         self.assertIn("id", response.json())
#         self.resource_id = response.json()["id"]

#     def test_read_resource(self):
#         # Ensure there is a resource to read (create it if not)
#         if not self.resource_id:
#             self.test_create_resource()

#         # Send a GET request to read the created resource
#         response = requests.get(self.base_url + f"/resources/{self.resource_id}")
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("name", response.json())

#     def test_update_resource(self):
#         # Ensure there is a resource to update (create it if not)
#         if not self.resource_id:
#             self.test_create_resource()

#         # Send a PUT request to update the created resource
#         response = requests.put(self.base_url + f"/resources/{self.resource_id}", json={"name": "Updated Resource"})
#         self.assertEqual(response.status_code, 200)

#         # Verify the resource was updated by reading it again
#         updated_response = requests.get(self.base_url + f"/resources/{self.resource_id}")
#         self.assertEqual(updated_response.json()["name"], "Updated Resource")

#     def test_delete_resource(self):
#         # Ensure there is a resource to delete (create it if not)
#         if not self.resource_id:
#             self.test_create_resource()

#         # Send a DELETE request to delete the created resource
#         response = requests.delete(self.base_url + f"/resources/{self.resource_id}")
#         self.assertEqual(response.status_code, 204)

#         # Verify the resource is deleted by trying to read it again
#         deleted_response = requests.get(self.base_url + f"/resources/{self.resource_id}")
#         self.assertEqual(deleted_response.status_code, 404)

# if __name__ == "__main__":
#     unittest.main()

'''SQL Injection'''
# import unittest
# import requests

# class TestSQLInjection(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_basic_sql_injection(self):
#         payload = "1' OR '1'='1"
#         response = requests.get(self.base_url + f"/search?query={payload}")
#         self.assertEqual(response.status_code, 200)
#         self.assertNotIn("Unauthorized", response.text)  # Check for SQL error messages

#     def test_union_based_sql_injection(self):
#         payload = "1' UNION SELECT null, username, password FROM users--"
#         response = requests.get(self.base_url + f"/search?query={payload}")
#         self.assertEqual(response.status_code, 200)
#         self.assertNotIn("Unauthorized", response.text)  # Check for SQL error messages

#     def test_time_based_blind_sql_injection(self):
#         payload = "1' OR IF(1=1, SLEEP(5), 0)--"
#         response = requests.get(self.base_url + f"/search?query={payload}")
#         self.assertEqual(response.status_code, 200)
#         # Check for delayed response indicating successful injection (if the API supports this)

#     # Add more SQL injection test cases for different types and scenarios

# if __name__ == "__main__":
#     unittest.main()

'''SQL injection for all APIs'''
# import unittest
# import requests

# class TestSQLInjection(unittest.TestCase):

#     def setUp(self):
#         self.base_url = "http://your-api-base-url"

#     def test_sql_injection_protection(self):
#         payloads = [
#             "1' OR '1'='1",
#             "admin' OR '1'='1'--",
#             "1; DROP TABLE users--",
#             "' UNION SELECT null, username, password FROM users--",
#             "1' UNION SELECT 1, database(), 3--",
#             "1' AND 1=2--",
#             "' AND 1=1--"
#             # Add more payloads here
#         ]

#         endpoints = [
#             ("/search", 200),
#             ("/login", 401),
#             ("/profile", 403),
#             # Add more API endpoints and their expected status codes
#         ]

#         for endpoint, expected_status in endpoints:
#             for payload in payloads:
#                 response = requests.get(self.base_url + f"{endpoint}?query={payload}")
#                 self.assertEqual(response.status_code, expected_status)  # Check status code
#                 self.assertNotIn("Unauthorized", response.text)          # Ensure no SQL error messages
#                 self.assertNotIn("Syntax error", response.text)           # Ensure no SQL syntax errors

# if __name__ == "__main__":
#     unittest.main()
