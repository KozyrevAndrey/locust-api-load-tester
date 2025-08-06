import uuid

from locust import HttpUser, between, task

from app.config import API_KEY, BASE_URL, ENDPOINTS


class APIUser(HttpUser):
    wait_time = between(1, 2)
    host = BASE_URL

    @task(1)
    def get_endpoint(self):
        endpoint = ENDPOINTS.get("dummy")
        user_id = uuid.uuid4()
        self.client.get(
            f"{endpoint}{user_id}/",
            headers={"Authorization": f"Api-Key {API_KEY}"},
        )
