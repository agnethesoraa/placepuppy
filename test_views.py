import unittest

import views


class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = views.app.test_client()

    def tearDown(self):
        pass

    def assertStatusCode(self, response, expected):
        self.assertEquals(response._status_code, expected)

    def test_index(self):
        response = self.app.get('/')
        self.assertStatusCode(response, 200)

    def test_image_view(self):
        pass

    def test_bw_image_view(self):
        pass

if __name__ == '__main__':
    unittest.main()
