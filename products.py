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
    purchase_products = {}
    with open('Purchase products - Sheet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                if row[0] in list(purchase_products.keys()):
                    purchase_products[row[0]]['quantity'] += 1
                else :
                    purchase_products[row[0]] = {'quantity':1,'rate':row[1]}
    return purchase_products
            

class Item():

    def __init__(self,rate,tax,category):
        self.tax = tax
        self.rate = rate
        self.category = category
        self.item_tax = 0
        self.deposit_tax = 0
        self.primary_tax = 0
        self.luxury_tax = 0

    def set_tax(self):
        """Method to calculate tax for each selected product"""
        self.item_tax = (float(self.rate)*float(self.tax))/100

    def set_deposit_tax(self):
        """Method to calculate deposit tax on recyclable products"""
        self.deposit_tax = (float(self.rate)*float(self.tax))/100

    def set_category(self):
        """To set primary and luxury tax based on category"""
        if self.category == 'primary':
            self.primary_tax = self.item_tax
        elif self.category == 'luxury':
            self.luxury_tax = self.item_tax
    
    def compute(self):
        pass


class Container():
    
    def __init__(self,products):
        """Container class expects dictionary which contains selected products"""
        self.purchase_products = products
        self.luxury_tax = 0
        self.deposit_tax = 0
        self.primary_tax = 0
        self.total = 0

    def print_receipt(self):
        """Method to generate recept based on selected  products"""
        pass

    def process(self):
        """calculate tax, deposit tax and total fare for all the products"""
        pass

if __name__ == '__main__':
    basket = read_csv()
    container = Container(basket)
