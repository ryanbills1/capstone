from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class EbayDatabase(object):
    """ CRUD operations for ebaydata.products collection in MongoDB """

    def __init__(self):
        # Initialize MongoClient.
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['ebaydata']

        # Test connection to MongoDB Server.
        try:
            self.client.admin.command('ping')
        except ConnectionFailure:
            print("Server not available")

    # Create Method
    def create(self, data):
        if data is not None:
            insert = self.database.products.insert_many(data)  # Pass data as dictionary.
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read Method
    def read(self, criteria=None):

        # criteria is not None then this find will return all rows which matches the criteria.
        if criteria:
            # {'_id':False} just omits the unique ID of each row.
            data = self.database.products.find(criteria)
        else:
            # if there is no search criteria then all the rows will be returned.
            data = self.database.products.find()
    
        return data

    # Update Method
    def update(self, update_filter, update_set):
        if update_filter and update_set is not None:
            updateresult = self.database.products.update_many(update_filter, update_set)
            if updateresult != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to update, because criteria param is empty")

    # Delete Method
    def delete(self, delete_filter):
        if delete_filter is not None:
            deleteresult = self.database.products.delete_many(delete_filter)
            if deleteresult != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to delete, because filter param is empty")
