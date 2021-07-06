import requests

def test_008():
    id = create()
    delete(id)
    get(id)


def create():
    url = "http://localhost:8080/api/v3/work_packages"
    login = ("apikey", "9b372732565f22180b5e348f5f95f281f6b59ebcc02a3b45c92ed8d46f3c44e3")
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
    return response.json()['id']


def delete(id):
    url = f"http://localhost:8080/api/v3/work_packages/{id}"
    login = ("apikey", "9b372732565f22180b5e348f5f95f281f6b59ebcc02a3b45c92ed8d46f3c44e3")
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.delete(url, headers=headers, auth=login)
    assert response.status_code == 204


def get(id):
    url = f"http://localhost:8080/api/v3/work_packages/{id}"
    login = ("apikey", "9b372732565f22180b5e348f5f95f281f6b59ebcc02a3b45c92ed8d46f3c44e3")

    response = requests.get(url, auth=login)
    assert response.status_code == 404
