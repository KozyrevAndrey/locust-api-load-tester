from locust import HttpUser, task, between
from app.config import BASE_URL, ENDPOINTS, API_KEY
from mimesis import Field, Locale
from mimesis.locales import Locale


class APIUser(HttpUser):
    wait_time = between(1, 5)
    host = BASE_URL
    fake = Field(locale=Locale.EN)

    @task(3)
    def get_endpoint(self):
        endpoint = ENDPOINTS.get("pinata_init")
        user_id = "lt" + self.fake("code.imei")
        self.client.get(
            f"{endpoint}{user_id}/",
            headers={"Authorization": f"Api-Key {API_KEY}"},
        )
