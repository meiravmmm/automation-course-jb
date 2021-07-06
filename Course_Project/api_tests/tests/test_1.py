import pytest
import requests
import json
import requests


class Test1:

    def test_get_project_by_id(self):

        expected_project_name = "TestProject1"
        expected_project_description="This is the first test project"

        url = "http://localhost:8080/api/v3/projects/3"

        payload = {}
        headers = {
            'Authorization': 'Basic YXBpa2V5OjliMzcyNzMyNTY1ZjIyMTgwYjVlMzQ4ZjVmOTVmMjgxZjZiNTllYmNjMDJhM2I0NWM5MmVkOGQ0NmYzYzQ0ZTM='
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        assert response.status_code==200,('The response status code failed: ', response.status_code)

        # project name
        data = response.json()
        actual_project_name = data["name"]


       # project description
        actual_project_description = data["description"]
        actual_project_raw = actual_project_description["raw"]

        assert actual_project_name == expected_project_name,('project name not same as expected')
        assert actual_project_raw == expected_project_description ,('programe description not same as expected')
