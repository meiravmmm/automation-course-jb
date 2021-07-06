import pytest
import requests
import json
import requests


class Test6:

    def test_GetWorkPackage_by_ID(self):
        url = "http://localhost:8080/api/v3/work_packages/34"
        login = ("apikey","9b372732565f22180b5e348f5f95f281f6b59ebcc02a3b45c92ed8d46f3c44e3")

        body = {
            "lockVersion": 3,
            "subject": "This is a subject after update 1.",
            "description": {
                "raw": "This is a description after update 1."
            }
        }
        response= requests.patch(url, auth=login, json=body)
        response_body = response.json()
        response = requests.patch(url, auth=login, json=body)
        response_body = response.json()
        assert response.status_code == 200, ('The response status code failed:', response.status_code)
        assert response_body['_type'] == 'WorkPackage', 'Type is not Task'
        assert response_body['subject'] == 'This is a subject after update 1.', 'Subject is not My Task 1'
        assert response_body['description']['raw'] == 'This is a description after update 1.'




