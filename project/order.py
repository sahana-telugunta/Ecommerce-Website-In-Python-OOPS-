import csv
class Order:
    def __init__(self):
        self.fl=['id','name','price','category','stock_left']
        pass
    def place_order(self,no):
        while(1):
            q=int(input('enter the quantity of the product:'))
            with open('productdata.csv','r') as f:
                r=csv.DictReader(f)
                for row in r:
                    if row.get('id') == str(no):
                        if int(row.get('stock_left'))>=q:
                            p=int(row.get('price'))
                            # w=csv.DictWriter(f,fieldnames=self.fl)
                            # for row in r:
                            #     if row.get('id') == str(no):
                            #         row['stock_left']=int(row.get('stock_left'))-q
                            print('Order has been placed please pay the payment of rupees '+str(p*q)+' on the delivery')
                            return
                        else:
                            print('no sufficient quantity available')
                        
    
    def display_orders(self):
        pass