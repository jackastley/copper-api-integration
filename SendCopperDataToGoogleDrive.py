import gspread


def sendToSheet(googleKeyPath, spreadsheetTitle, workSheetTitle, dataFrame):
    
    #REPLACE NANS WITH 0s
    for column in dataFrame:
        dataFrame[column] = dataFrame[column].fillna(0)
        if dataFrame[column].dtype == object:
            dataFrame[column] = dataFrame[column].astype(str)
         
    
    # SEND TO GOOGLE SHEET
    sa = gspread.service_account(filename=googleKeyPath)

    sh = sa.open(spreadsheetTitle)

    worksheet = sh.worksheet(workSheetTitle)

    worksheet.clear()

    worksheet.update([dataFrame.columns.values.tolist()] +
                     dataFrame.values.tolist())

    print('Sheet updated.')


