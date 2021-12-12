import os
import pandas as pd

class LoadExcel(object):
    '''Class for loading Excel input file into a Pandas dataframe.'''
    
    def get_data_from_excel(self):
        input_file = (os.getcwd() + "\\eBayBookInfo.xlsx")
        df = pd.read_excel(input_file)
        return df