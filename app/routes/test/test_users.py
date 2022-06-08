import unittest
import requests


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000/users'

# get all users
    def test_all_users(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

# get single user
    def test_single_user_found(self):
        response = requests.get(self.base_url + '/1')
        self.assertEqual(response.status_code, 200)

    def test_single_user_not_found(self):
        response = requests.get(self.base_url + '/9999')
        self.assertEqual(response.status_code, 500)

# create user
    def test_new_user(self):
        data = {
            'name': 'name',
            'password': 'password'}
        response = requests.post(self.base_url + '/', json=data)
        self.assertEqual(response.status_code, 200)

# update user
    def test_update_user(self):
        data = {
            'name': 'name_test',
            'password': 'password_test'}
        response = requests.put(self.base_url + '/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_user_not_found(self):
        response = requests.put(self.base_url + '/9999')
        self.assertEqual(response.status_code, 400)

# delete user
    def test_delete_user_found(self):
        response = requests.delete(self.base_url + '/2')
        self.assertEqual(response.status_code, 200)

    def test_delete_user_not_found(self):
        response = requests.delete(self.base_url + '/9999')
        self.assertEqual(response.status_code, 500)


class TestUserProjects(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000/users'

# get all user's projects
    def test_user_projects(self):
        response = requests.get(self.base_url + '/1/projects')
        self.assertEqual(response.status_code, 200)

# create a user project
    def test_new_user_project(self):
        data = {
            'name': 'name',
            'is_complete': '0',
            'description': 'new description'}
        response = requests.post(self.base_url + '/1/projects', json=data)
        self.assertEqual(response.status_code, 200)

# update user project
    def test_update_user_project_found(self):
        data = {
            'name': 'name',
            'is_complete': '1',
            'description': 'new description'}
        response = requests.put(self.base_url + '/1/projects/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_user_project_not_found(self):
        response = requests.put(self.base_url + '/1/projects/9999')
        self.assertEqual(response.status_code, 400)

# delete user project
    def test_delete_user_project_found(self):
        response = requests.delete(self.base_url + '/1/projects/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_user_project_not_found(self):
        response = requests.delete(self.base_url + '/9999/projects/9999')
        self.assertEqual(response.status_code, 500)


class TestUserTasks(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000/users'

# get all user's tasks
    def test_user_tasks(self):
        response = requests.get(self.base_url + '/1/tasks')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
