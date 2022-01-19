import pandas as pd
import os

from sqlalchemy import false

database = pd.DataFrame(columns=["Username","Password"])

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def dataStoring(self):
        if self.username not in database['Username']:
            database['Username'] = self.username 
            database['Password'] = self.password 
            database.to_csv(index = false)
            return True
        else:
            return False 
        
    def userExists(self):
        if self.username not in database['Username'] and self.password in database["password"]:
            return True
        else:
            return False 