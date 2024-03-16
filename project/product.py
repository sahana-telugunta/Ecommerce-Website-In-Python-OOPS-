import csv
class Product:
    def __init__(self) :
        self.c=0

    def display_products(self):
        print("\n\n-------------PRODUCTS LIST--------------")
        with open('productdata.csv','r') as f:
            r=csv.DictReader(f)
            j=1
            for i in r:
                print(j,i['name'],sep='. ',end='      ')
                j+=1

    def product_details(self,no):
        with open('productdata.csv','r') as f:
            r=csv.DictReader(f)
            for row in r:
                if row.get('id') == str(no):
                    for key, value in row.items():
                         if key != 'id':
                            print(f"{key}: {value}")
                    return    

