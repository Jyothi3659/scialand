# scialand

products.py file contains two classes container and item

container class expects dictionary object 

sample dictionary object :
{
	'E-book "Matrix 2.0"': {
		'rate': 12.49,
		'sugar_index': 0.7,
		'tax': 0,
		'deposit_tax': 0,
		'product_category': 'primary'
	},
	'Bar of Chocolate': {
		'rate': 2.25,
		'sugar_index': 0.7,
		'tax': 50,
		'deposit_tax': 0,
		'product_category': 'primary'
	},
	'SciEnergy Drink (Can)': {
		'rate': 0.99,
		'sugar_index': 1.2,
		'tax': 50,
		'deposit_tax': 0.50,
		'product_category': 'primary'
	},
	'Car (Einstein Model 3)': {
		'rate': 1877.5,
		'sugar_index': 0,
		'tax': 50,
		'deposit_tax': 0,
		'product_category': 'primary'
	},
	'SciSky Suite': {
		'rate': 300.78,
		'sugar_index': 0.7,
		'tax': 0,
		'deposit_tax': 0,
		'product_category': 'primary'
	},
	'Cool Phone': {
		'rate': 112.30,
		'sugar_index': 0,
		'tax': 0,
		'deposit_tax': 40,
		'product_category': 'primary'
	}
}

if you want add few more products to the config you modify avaliable_products in config.py and use relavant products in csv file

item class is to get individual product data like tax, environment deposit tax etc..

how to execute python file?
step1 : cd to file directory
step2 : python3 products.py

then it will print receipt in cmd prompt

how to execute test cases?
step1 : cd to file directory
step2 : python3 test_products.py