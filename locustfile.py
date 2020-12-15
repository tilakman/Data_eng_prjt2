
from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0,0)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        print ('CEST FINI')

    @task(1)
    def hello_world(self):
        self.client.post("http://localhost:5000", {'sentence':'hi'})