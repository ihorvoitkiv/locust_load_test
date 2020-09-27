from locust import HttpUser, task, between

class UserBehaviour(HttpUser):
    wait_time = between(1, 2)

    def main_endpoint(self):
        self.client.get("/")

    @task(2)
    def posts(self):
        self.client.get("/posts")

    @task(1)
    def comments(self):
        data = {
            "postId": 1,
            "name": "my comment",
            "email": "test@user.test",
            "body": "Author is cool. Some text. Hello world!"
        }
        self.client.post("/comments", data)