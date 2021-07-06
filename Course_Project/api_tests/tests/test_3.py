import pytest
import requests
import json
import requests


class Test3:

    def test_create_project(self):

        expected_project_name= 'Meirav moshe'

        url = "http://localhost:8080/api/v3/projects/"

        payload = json.dumps({
            "name":  expected_project_name
        })
        headers = {
            'Authorization': 'Basic YXBpa2V5OjliMzcyNzMyNTY1ZjIyMTgwYjVlMzQ4ZjVmOTVmMjgxZjZiNTllYmNjMDJhM2I0NWM5MmVkOGQ0NmYzYzQ0ZTM=',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        assert response.status_code == 201, ('The response status code failed:', response.status_code)

        # project name

        data = response.json()
        actual_project_name = data["name"]

        assert actual_project_name == expected_project_name, ('project name not same as expected')
