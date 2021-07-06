import pytest
import requests
import json
import requests


class Test2:

    def test_Update_project_by_id(self):

        expected_project_description="This is the first test project"

        #response = requests.request("PATCH", url, headers=headers, data=payload)
        url = "http://localhost:8080/api/v3/projects/3"

        payload = json.dumps({
            "_links": {},
            "description": {
                "raw": expected_project_description
            }
        })
        headers = {
            'Authorization': 'Basic YXBpa2V5OjliMzcyNzMyNTY1ZjIyMTgwYjVlMzQ4ZjVmOTVmMjgxZjZiNTllYmNjMDJhM2I0NWM5MmVkOGQ0NmYzYzQ0ZTM=',
            'Content-Type': 'application/json'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)
        assert response.status_code==200,('The response status code failed: ', response.status_code)

        data = response.json()
        # project description
        actual_project_description = data["description"]
        actual_project_raw = actual_project_description["raw"]

        assert actual_project_raw == expected_project_description ,('program description not same as expected')
