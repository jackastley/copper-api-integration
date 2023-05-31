from CopperRequest import CopperRequest
from SendCopperDataToGoogleDrive import sendToSheet
import time
import datetime
import os
import pathlib
cwd = pathlib.Path(__file__).parent.resolve()
os.chdir(cwd)

#SET TIMESTAMP
def setYear(year):
    timestamp = time.mktime(datetime.datetime(year,7,1,1,1,1).timetuple())
    return int(timestamp)

FY_timestamp = setYear(2022)
prev_year_timestamp = setYear(2021)

#LOAD COPPER API KEY
with open("copper_api_key.txt") as f:
    api_key = f.readline()

#SET GOOGLE KEY PATH
google_key_path = "../google_key.json"

#SEND REQUESTS
request = CopperRequest(access_token=api_key)

ytd_ops = request.YTDOpportunities(minimum_created_date=FY_timestamp)
current_ops =request.currentOpenOpportunties(minimum_close_date=FY_timestamp)
won_ops = request.wonOpportunities(minimum_close_date=FY_timestamp)
lost_ops = request.lostOpportunities(minimum_close_date=FY_timestamp)
customer_sources = request.customerSources()
loss_reasons = request.lossReasons()
prev_ops = request.prevYearOpportunities(minimum_created_date=prev_year_timestamp, maximum_created_date=FY_timestamp)

#SEND TO GOOGLE SHEET
sendToSheet(googleKeyPath=google_key_path, spreadsheetTitle="Copper Raw Data", workSheetTitle="YTD_OPS", dataFrame=ytd_ops)
sendToSheet(googleKeyPath=google_key_path, spreadsheetTitle="Copper Raw Data", workSheetTitle="PREV_OPS", dataFrame=prev_ops)
sendToSheet(googleKeyPath=google_key_path, spreadsheetTitle="Copper Raw Data", workSheetTitle="CURRENT_OPS", dataFrame=current_ops)
sendToSheet(googleKeyPath=google_key_path, spreadsheetTitle="Copper Raw Data", workSheetTitle="WON_OPS", dataFrame=won_ops)
sendToSheet(googleKeyPath=google_key_path, spreadsheetTitle="Copper Raw Data", workSheetTitle="LOST_OPS", dataFrame=lost_ops)
sendToSheet(googleKeyPath=google_key_path, spreadsheetTitle="Copper Raw Data", workSheetTitle="CUSTOMER_SOURCES", dataFrame=customer_sources)
sendToSheet(googleKeyPath=google_key_path, spreadsheetTitle="Copper Raw Data", workSheetTitle="LOSS_REASONS", dataFrame=loss_reasons)
