from urllib import response

import pytest
import requests
import json



class Test7:
    def test_GetWorkPackage_by_ID(self):
        url = "http://localhost:8080/api/v3/work_packages"
        login = ("apikey","9b372732565f22180b5e348f5f95f281f6b59ebcc02a3b45c92ed8d46f3c44e3")
        import requests

        body = {
            "subject": "Exc7",
            "_links": {
                "type": {
                    "href": "/api/v3/types/1",
                    "title": "Task"
                },
                "project": {
                    "href": "/api/v3/projects/3",
                    "title": "TestProject1"
                }
            }
        }

        response = requests.post(url, json=body, auth=login)
        assert response.status_code == 201, ('The response status code failed:', response.status_code)
        assert response.json()["subject"] == 'Exc7'

