import csv
from config import avaliable_products
import logging
import sys,traceback

logging.basicConfig(filename='scialand.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def read_csv():
    '''To read CSV file and generates dictionary object'''
    pass
            

class Item():

    def __init__(self):
        pass

    def set_tax(self):
        """Method to calculate tax for each selected product"""
        pass

    def set_deposit_tax(self):
        """Method to calculate deposit tax on recyclable products"""
        pass

    def set_category(self):
        """To set primary and luxury tax based on category"""
        pass
    
    def compute(self):
        pass


class Container():
    
    def __init__(self,products):
        """Container class expects dictionary which contains selected products"""
        pass

    def print_receipt(self):
        """Method to generate recept based on selected  products"""
        pass

    def process(self):
        """calculate tax, deposit tax and total fare for all the products"""
        pass

