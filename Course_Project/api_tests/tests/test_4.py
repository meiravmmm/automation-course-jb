import pytest
import requests
import json
import requests


# sent request to creat a new project with a unique name
class Test4:

    def test_create_project(self):

        expected_project_name= 'Meirav moshe'

        url = "http://localhost:8080/api/v3/projects/"

        payload = {"name":expected_project_name }

        login = ("apikey","9b372732565f22180b5e348f5f95f281f6b59ebcc02a3b45c92ed8d46f3c44e3")

        response= requests.post(url,json=payload,auth=login)

        assert response.status_code == 201, ('The response status code failed:', response.status_code)

        actual_project_name = response.json()["name"]

        assert actual_project_name == expected_project_name, ('project name not same as expected')


# Delete the newly created project send the request to delete a project by ID

    def test_delete_project(self):
        url = "http://localhost:8080/api/v3/projects/26"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YXBpa2V5OjliMzcyNzMyNTY1ZjIyMTgwYjVlMzQ4ZjVmOTVmMjgxZjZiNTllYmNjMDJhM2I0NWM5MmVkOGQ0NmYzYzQ0ZTM=',
            'Cookie': '_open_project_session=b8d70aca21e9fbb49c35d00376e3e57c'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

# verify the project was deleted by sending arequest to get a project by ID

    def test_VerifyDelete_project(self):
        url = "http://localhost:8080/api/v3/projects/26"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YXBpa2V5OjliMzcyNzMyNTY1ZjIyMTgwYjVlMzQ4ZjVmOTVmMjgxZjZiNTllYmNjMDJhM2I0NWM5MmVkOGQ0NmYzYzQ0ZTM=',
            'Cookie': '_open_project_session=b8d70aca21e9fbb49c35d00376e3e57c'
        }

        response = requests.request("GET", url, headers=headers, data=payload)