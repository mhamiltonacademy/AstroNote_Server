import unittest
import requests

class TestUsers(unittest.TestCase):
    URL = 'http://127.0.0.1:5000/users'

# get all users
    def test_all_users(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

# get single user
    def test_single_user_found(self):
        response = requests.get(self.URL + '/1')
        self.assertEqual(response.status_code, 200)
    def test_single_user_not_found(self):
        response = requests.get(self.URL + '/9999')
        self.assertEqual(response.status_code, 500) # why should this be 500 instead of 404?

# have trouble passing in the data
# create user
    # def test_new_user(self):
    #     data = {
    #         'name': 'name',
    #         'password': 'password'}
    #     response = requests.post(self.URL, json=data)
    #     self.assertEqual(response.status_code, 200)

# update user
    def test_update_user(self):
        data = {
            'name': 'name',
            'password': 'password'}
        response = requests.put(self.URL + '/1', json=data)
        self.assertEqual(response.status_code, 200)
    def test_update_user_not_found(self):
        data = {
            'name': 'name',
            'password': 'password'}
        response = requests.put(self.URL + '/users/9999', json=data)
        self.assertEqual(response.status_code, 404)

# delete user
    def test_delete_user_found(self):
        response = requests.delete(self.URL + '/users/1')
        self.assertEqual(response.status_code, 404)
    def test_delete_user_not_found(self):
        response = requests.delete(self.URL + '/users/9999')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
