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
        self.assertEqual(response.status_code, 500)

# # create a task in project
    # def test_new_project(self):
    #     data = {
    #         'name': 'name_test',
    #         'description': 'description_test',
    #         'deadline': '05/05/2020',
    #         'priority': '1',
    #         'progress': '1',
    #         'project_id': '2',
    #         'engineer_id': '2'}
    #     response = requests.post(self.URL, json=data)
    #     self.assertEqual(response.status_code, 200)

# update a task in project
    def test_update_project_found(self):
        data = {
            'name': 'name_test',
            'description': 'description_test',
            'deadline': '05/05/2020',
            'priority': '1',
            'progress': '1',
            'project_id': '2',
            'engineer_id': '2'}
        response = requests.put(self.URL + '/1/tasks/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_project_not_found(self):
        data = {
            'name': 'name_test',
            'description': 'description_test',
            'deadline': '05/05/2020',
            'priority': '1',
            'progress': '1',
            'project_id': '2',
            'engineer_id': '2'}
        response = requests.put(self.URL + '/9999/tasks/9999', json=data)
        self.assertEqual(response.status_code, 500)

# delete a task in project
    def test_delete_project_found(self):
        response = requests.delete(self.URL + '/1/tasks/2')
        self.assertEqual(response.status_code, 200)

    def test_delete_project_not_found(self):
        response = requests.delete(self.URL + '/9999/tasks/9999')
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
