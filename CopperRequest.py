from PageProcessor import PageProcessor
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
        requestUrl = "https://api.copper.com/developer_api/v1/opportunities/search"
        requestParameters = {
                "page_number": 1,
                "page_size": str(page_size),
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_created_date": minimum_created_date
        }
        
        pageProcessor = PageProcessor(requestParameters)
        
        return pageProcessor.processAllPages(requestUrl, self.headers)
        
        
            
    def prevYearOpportunities(self, minimum_created_date, maximum_created_date, sort_by="date_created", page_size=200):
        requestUrl = "https://api.copper.com/developer_api/v1/opportunities/search"
        requestParameters = {
                "page_number":1,
                "page_size": str(page_size),
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_created_date": minimum_created_date,
                "maximum_created_date": maximum_created_date
            }

        pageProcessor = PageProcessor(requestParameters)
        
        return pageProcessor.processAllPages(requestUrl, self.headers)

    def wonOpportunities(self, minimum_close_date, sort_by="date_created", page_size=200):
        requestUrl = "https://api.copper.com/developer_api/v1/opportunities/search"
        requestParameters = {
                "page_number": 1,
                "page_size": str(page_size),
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_close_date": minimum_close_date,
                "status_ids[]": ["1"]
            }
        pageProcessor = PageProcessor(requestParameters)
        return pageProcessor.processAllPages(requestUrl, self.headers)
        

    def lostOpportunities(self, minimum_close_date, sort_by="date_created", page_size=200):
        requestUrl = "https://api.copper.com/developer_api/v1/opportunities/search"
        requestParameters = {
                "page_number": 1,
                "page_size": page_size,
                "sort_by": sort_by,
                "sort_direction": "desc",
                "minimum_close_date": minimum_close_date,
                "status_ids[]": ["2", "3"]
            }
        pageProcessor = PageProcessor(requestParameters)
        return pageProcessor.processAllPages(requestUrl, self.headers)
            
    def currentOpenOpportunties(self, minimum_close_date, sort_by="date_created", page_size=200):
        requestUrl = "https://api.copper.com/developer_api/v1/opportunities/search"
        requestParameters = {
                "minimum_close_date": minimum_close_date,
                "page_number": 1,
                "page_size": page_size,
                "sort_by": sort_by,
                "sort_direction": "desc",
                "status_ids[]": ["0"]
            }
        
        pageProcessor = PageProcessor(requestParameters)
        return pageProcessor.processAllPages(requestUrl, self.headers)
       

    def lossReasons(self):
        lossReasons = requests.get(
            "https://api.copper.com/developer_api/v1/loss_reasons", headers=self.headers).json()
        
        return pd.DataFrame(lossReasons)
    
    def customerSources(self):
        customerSources = requests.get(
            "https://api.copper.com/developer_api/v1/customer_sources", headers=self.headers).json()
        
        return pd.DataFrame(customerSources)

