import requests
import pandas as pd
import os
import pathlib
cwd = pathlib.Path(__file__).parent.resolve()
os.chdir(cwd)


class PageProcessor:
    def __init__(self, requestParameters, maxPages=100):
        self.requestParameters = requestParameters
        self.data = []
        self.maxPages = maxPages

    def processAllPages(self, url, headers):
        for _ in range(0, self.maxPages):
            res = requests.post(
                url, headers=headers, params=self.requestParameters)

            self.testResponseStatus(res)

            if not self.hasNextPage(res):
                self.appendPage(res)
                return pd.DataFrame(self.data)

            self.appendPage(res)
            self.requestParameters["page_number"] += 1

    def appendPage(self, res):
        self.data += res.json()

    def hasNextPage(self, res):
        if len(res.json()) == 200:
            return True
        return False

    def testResponseStatus(self, res):
        if res.status_code != 200:
            raise ConnectionError(str(res.status_code) + " \n" + res.text)
