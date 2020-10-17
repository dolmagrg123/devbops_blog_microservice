import unittest
import requests
class BasicTestCase(unittest.TestCase):

    def test_posting(self):
        res = requests.get('http://localhost:5000/posting')
        self.assertEquals(res.status_code, 200)

    def test_comment(self):
        res = requests.post('http://localhost:5000/comment')
        self.assertEquals(res.status_code, 200)

    def test_viewing(self):
        res = requests.get('http://localhost:5000/viewing')
        self.assertEquals(res.status_code, 200)

if __name__ == '__main__': 
  
    unittest.main()
