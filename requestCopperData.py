import requests
import os
import pathlib
import pandas as pd
cwd = pathlib.Path(__file__).parent.resolve()
os.chdir(cwd)

with open('copper_api_key.txt') as f:
    api_key = f.readline()
    
with open('copper_api_user.txt') as f:
    user = f.readline()


class CopperRequest:
    def __init__(self, access_token):
        self.headers = {
            "X-PW-AccessToken": access_token,
            "X-PW-Application": "developer_api",
            "X-PW-UserEmail": user,
            "Content-Type": "application/json"
        }

    def YTDOpportunities(self, minimum_created_date, sort_by="date_created", page_size=200):
        pageNumber = 1
        dataToReturn = []
        for i in range(0, 5):
            params = {
                "page_number":pageNumber,
                "page_size": str(page_size),
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_created_date": minimum_created_date
            }

            res = requests.post(
                "https://api.copper.com/developer_api/v1/opportunities/search", headers=self.headers, params=params)

            if res.status_code != 200:
                print(str(res.status_code) + " \n" + res.text)
                return False

            if len(res.json()) == 0:
                return dataToReturn

            if len(res.json()) == 200:
                pageNumber += 1
                dataToReturn = dataToReturn + res.json()
            else:
                dataToReturn = dataToReturn + res.json()
                return pd.DataFrame(dataToReturn)
            
    def prevYearOpportunities(self, minimum_created_date, maximum_created_date, sort_by="date_created", page_size=200):
        pageNumber = 1
        dataToReturn = []
        for i in range(0, 5):
            params = {
                "page_number":pageNumber,
                "page_size": str(page_size),
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_created_date": minimum_created_date,
                "maximum_created_date": maximum_created_date
            }

            res = requests.post(
                "https://api.copper.com/developer_api/v1/opportunities/search", headers=self.headers, params=params)

            if res.status_code != 200:
                print(str(res.status_code) + " \n" + res.text)
                return False

            if len(res.json()) == 0:
                return dataToReturn

            if len(res.json()) == 200:
                pageNumber += 1
                dataToReturn = dataToReturn + res.json()
            else:
                dataToReturn = dataToReturn + res.json()
                return pd.DataFrame(dataToReturn)

    def wonOpportunities(self, minimum_close_date, sort_by="date_created", page_size=200):
        pageNumber = 1
        dataToReturn = []

        for i in range(0, 5):
            params = {
                "page_number": pageNumber,
                "page_size": str(page_size),
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_close_date": minimum_close_date,
                "status_ids[]": ["1"]
            }

            res = requests.post(
                "https://api.copper.com/developer_api/v1/opportunities/search", headers=self.headers, params=params)

            if res.status_code != 200:
                print(str(res.status_code) + " \n" + res.text)
                return False
            if len(res.json()) == 0:
                return dataToReturn
            if len(res.json()) == 200:
                pageNumber += 1
                dataToReturn = dataToReturn + res.json()
            else:
                dataToReturn = dataToReturn + res.json()
                return pd.DataFrame(dataToReturn)

    def lostOpportunities(self, minimum_close_date, sort_by="date_created", page_size=200):
        pageNumber = 1
        dataToReturn = []

        for i in range(0, 5):
            params = {
                "page_number": pageNumber,
                "page_size": page_size,
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_close_date": minimum_close_date,
                "status_ids[]": ["2", "3"]
            }

            res = requests.post(
                "https://api.copper.com/developer_api/v1/opportunities/search", headers=self.headers, params=params)

            if res.status_code != 200:
                print(str(res.status_code) + " \n" + res.text)
                return False
            if len(res.json()) == 0:
                return dataToReturn
            if len(res.json()) == 200:
                pageNumber += 1
                dataToReturn = dataToReturn + res.json()
            else:
                dataToReturn = dataToReturn + res.json()
                return pd.DataFrame(dataToReturn)
            
    def currentOpenOpportunties(self, minimum_close_date, sort_by="date_created", page_size=200):
        pageNumber = 1
        dataToReturn = []

        for i in range(0, 5):
            params = {
                "minimum_close_date": minimum_close_date,
                "page_number": pageNumber,
                "page_size": page_size,
                "sort_by": sort_by,
                "sort_direction": "desc",
                "status_ids[]": ["0"]
            }

            res = requests.post(
                "https://api.copper.com/developer_api/v1/opportunities/search", headers=self.headers, params=params)

            if res.status_code != 200:
                print(str(res.status_code) + " \n" + res.text)
                return False
            if len(res.json()) == 0:
                return dataToReturn
            if len(res.json()) == 200:
                pageNumber += 1
                dataToReturn = dataToReturn + res.json()
            else:
                dataToReturn = dataToReturn + res.json()
                return pd.DataFrame(dataToReturn)

    def lossReasons(self):
        lossReasons = requests.get(
            "https://api.copper.com/developer_api/v1/loss_reasons", headers=self.headers).json()
        
        return pd.DataFrame(lossReasons)
    
    def customerSources(self):
        customerSources = requests.get(
            "https://api.copper.com/developer_api/v1/customer_sources", headers=self.headers).json()
        
        return pd.DataFrame(customerSources)
    