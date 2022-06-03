import unittest
import requests


class TestProjects(unittest.TestCase):
    URL = 'http://127.0.0.1:5000/projects'

# get users in project
    def test_get_projects_found(self):
        response = requests.get(self.URL + '/1/users')
        self.assertEqual(response.status_code, 200)

    def test_get_projects_not_found(self):
        response = requests.get(self.URL + '/9999/users')
        self.assertEqual(response.status_code, 404)

# create a task in project
    # def test_new_project(self):
    #     data = {
    #         'name': 'name',
    #         'password': 'password'}
    #     response = requests.post(self.URL + '/1/tasks', json=data)
    #     self.assertEqual(response.status_code, 200)

# update a task in project
    def test_update_project_found(self):
        data = {
            'name': 'name',
            'password': 'password'}
        response = requests.put(self.URL + '/1/tasks/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_project_not_found(self):
        data = {
            'name': 'name',
            'password': 'password'}
        response = requests.put(self.URL + '/1/tasks/9999', json=data)
        self.assertEqual(response.status_code, 404)

# delete a task in project
    def test_delete_project_found(self):
        response = requests.delete(self.URL + '/1/tasks/1')
        self.assertEqual(response.status_code, 404)

    def test_delete_project_not_found(self):
        response = requests.delete(self.URL + '/1/tasks/9999')
        self.assertEqual(response.status_code, 404)
