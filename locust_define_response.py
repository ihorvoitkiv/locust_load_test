from locust import HttpUser
import random

class UserBehaviour(HttpUser):

    def check_album_if(self):
        photo_id = random.randint(1, 5000)
        with self.client.get(f'/photos/{photo_id}', response_catch=True, name=f'/photos/[id]') as response:
            if response.status_code == 200:
                album_id = response.json().get('albumId')
                if album_id % 10 == 0:
                    response.success()
                else:
                    response.failure(f'{album_id} is not valid')
            else:
                response.failure(f'status code is {response.status_code}')

