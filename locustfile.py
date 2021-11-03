import random, json
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    min_wait = 5000
    max_wait = 9000    

    @task
    def home_page(self):
        self.client.get("/")
      
    @task
    def prediction(self):
        self.client.post("/predict", 
            json={"CHAS": { "0":0 },
                  "RM":{ "0":6.575 },
                  "TAX":{ "0":296.0 },
                  "PTRATIO":{ "0":15.3 },
                  "B":{ "0":396.9 },
                  "LSTAT":{ "0":4.98 }         
            })