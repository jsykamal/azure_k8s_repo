try:
    from app import app
    import unittest
except Exception as e:
    print("Some Modules are missing : {}".format(e))

class MyTestCase(unittest.TestCase):

    # Check if response is 200
    def test_index_route(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content return is application / json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "application/json")

    # Check for data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'Message' in response.data)

    def test_predict_route(self):
        with app.app_context():
            response = app.test_client().get(
                '/predict?sentence=Hello'
            )
        statuscode = response.status_code
        print(response.data)
        self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main()
