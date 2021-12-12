from ebaysdk.finding import Connection as Finding
from dotenv import load_dotenv
import datetime
import os
import pandas as pd

class EbayConnect(object):
    '''Class for connecting to the API and retrieving data'''

    # Constructor method - used to get/set the API key from (local) .env file 
    def __init__(self):
        load_dotenv()
        API_KEY = os.getenv('api_key')
        self.api_key = API_KEY

    # Function to connect to the eBay API and retrieve data. Filters using ISBN list as keywords.
    def fetch_by_isbn(self, df):
        try:
            # Initializing vars to be used in API call.
            api = Finding(appid=self.api_key, config_file=None, siteid="EBAY-US", https=True, debug=False)
            output = pd.DataFrame()
            
            # Iterate through each ISBN, calling the API each time to search for products.
            for i, row in df.iterrows():
               
                # API Call.
                response = api.execute('findItemsByProduct', f'<productId type="ISBN">{row[0]}</productId>')
                print('Searching ISBN: ', row[0], '. . .')
                
                # Append search results to the 'output' dataframe.
                for item in response.reply.searchResult.item:
                    output = output.append(
                        {   "ISBN": row[0],
                            "Title": item.title,
                            "CurrentPrice": item.sellingStatus.convertedCurrentPrice.value,
                            "Condition": item.condition.conditionDisplayName,
                            "Country": item.country,
                            "URL": item.viewItemURL, 
                            "BestOffer": item.listingInfo.bestOfferEnabled,
                            "BuyItNow": item.listingInfo.buyItNowAvailable,
                            "Timestamp": datetime.datetime.now()
                        }, ignore_index=True)
            
        # Print error message if API fails to connect.
        except ConnectionError as e:
            print(e)
            print(e.response.dict())
        return output