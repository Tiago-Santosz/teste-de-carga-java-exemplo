from locust import HttpUser, task, between
import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Gera credenciais únicas por usuário
        self.username = f"user_{random_string(5)}"
        self.password = random_string(10)

    @task(1)
    def register(self):
        self.client.post("/api/register", json={
            "username": self.username,
            "password": self.password
        })

    @task(2)
    def login(self):
        self.client.post("/api/login", json={
            "username": self.username,
            "password": self.password
        })
