import pytest
import requests
import json
import requests


class Test5:

    def test_GetWorkPackage_by_ID(self):

        url = "http://localhost:8080/api/v3/work_packages/34"

        login = ("apikey","9b372732565f22180b5e348f5f95f281f6b59ebcc02a3b45c92ed8d46f3c44e3")

        response= requests.get(url,auth=login)
        response_body = response.json()

        assert response.status_code == 200, ('The response status code failed:', response.status_code)
        assert response_body['_embedded']['type']['name'] == 'Task', 'Type is not Task'
        assert response_body['subject'] == 'My Task 1', 'Subject is not My Task 1'




