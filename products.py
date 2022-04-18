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

    def __init__(self,rate,tax,deposit_tax,category):
        self.tax = tax
        self.rate = rate
        self.deposit = deposit_tax
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
        self.deposit_tax = (float(self.rate)*float(self.deposit))/100

    def set_category(self):
        """To set primary and luxury tax based on category"""
        if self.category == 'primary':
            self.primary_tax = self.item_tax
        elif self.category == 'luxury':
            self.luxury_tax = self.item_tax
    
    def compute(self):
        """To set primary tax, luxury tax based on category"""
        self.set_tax()
        self.set_deposit_tax()
        self.set_category()


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
        for key,value in self.purchase_products.items():
            print(value['quantity']," ",key, "@ SC ", value['rate'])
        print('\n')
        print('Total:   ',self.total)
        print('Deposit: SC ', self.deposit_tax)
        print('Sales Tax (Luxury): SC ', self.luxury_tax)
        print('Sales Tax (Primary): SC ', self.primary_tax)

    def process(self):
        """calculate tax, deposit tax and total fare for all the products"""
        for key,value in self.purchase_products.items():
            try:
                product = avaliable_products[key]
                item = Item(product['rate'],product['tax'],product['deposit_tax'],product['product_category'])
                item.compute()
                self.luxury_tax += item.luxury_tax
                self.deposit_tax += item.deposit_tax 
                self.primary_tax += item.primary_tax
                total = product['rate'] + self.luxury_tax + self.primary_tax + self.deposit_tax
                self.total += total * value['quantity']
            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                error_stack = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
                logging.error(error_stack)
        self.print_receipt()

if __name__ == '__main__':
    basket = read_csv()
    container = Container(basket)
    container.process()
