import unittest
from app import app, get_list, get_primes


class TestPrimeNumbersListing(unittest.TestCase):
    def test_correct_list(self):
        tester = app.test_client(self);
        response = tester.get('/10')
        self.assertEqual(get_list(10), [2,3,5,7])
        self.assertEqual(response.status_code, 200)

    def test_incorrect_list(self):
        tester = app.test_client(self);
        response = tester.get('/1')
        self.assertEqual(get_list(10), [2,3,5,7])
        self.assertEqual(response.status_code, 400)

    def test_correct_primes(self):
        tester = app.test_client(self);
        response = tester.get('/10')
        self.assertEqual(get_primes(10), [3, 5, 7])
        self.assertEqual(response.status_code, 200)

    def test_incorrect_primes(self):
        tester = app.test_client(self);
        response = tester.get('/1')
        self.assertEqual(get_primes(10), [3, 5, 7])
        self.assertEqual(response.status_code, 400)

    def test_incorrect_route(self):
        tester = app.test_client(self);
        response = tester.get('/')
        self.assertEqual(response.status_code, 400)

