from LoadExcel import LoadExcel as LoadExcel
from EbayConnect import EbayConnect
from EbayDatabase import EbayDatabase as EbayDatabase
import pandas as pd

#Main Function
if __name__ == '__main__':

    # Load Excel input into a Pandas dataframe variable.
    ExcelObject = LoadExcel()
    excel_data = ExcelObject.get_data_from_excel()

    # Call eBay API with search criteria, passing dataframe from above.
    e = EbayConnect()
    listing_data = e.fetch_by_isbn(excel_data)
    listing_data = listing_data.to_dict("records")
    
    # Instantiate EbayDatabase to initialize MongoDB connection.
    ebayDB = EbayDatabase()

    # Insert listing_data dictionary to MongoDB products collection.
    ebayDB.create(listing_data)

    # Reading from database, specifying query criteria to filter results.
    output = pd.DataFrame(list(ebayDB.read({
        #"BuyItNow": "true", 
        #"Condition":{'$regex' : '^((?!Acceptable).)*$', '$options' : 'i'}
        })))
    
    # Exporting database output to Excel.
    output.to_excel("output.xlsx")        