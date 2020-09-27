from locust import HttpUser, task, between


class FlowException(Exception):
    pass


class UserBehavior(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def check_flow(self):
        new_post = {'userId': 1, 'title': 'post#1', 'body': 'hello everybody'}
        post_response = self.client.post('/posts', json=new_post)
        if post_response.status_code != 201:
            raise FlowException('post not created')
        post_id = post_response.json().get('id')

        new_comment = {
            "postId": post_id,
            "name": "my comment",
            "email": "locust_test@mailinator.com",
            "body": "Hello world!"
        }
        comment_response = self.client.post('/comments', json=new_comment)
        if comment_response.status_code != 201:
            raise FlowException('comment not created')
        comment_id = comment_response.json().get('id')

        self.client.get(f'/comments/{comment_id}', name='/comments/[id]')
        if comment_response.status_code != 200:
            raise FlowException('comment not read')