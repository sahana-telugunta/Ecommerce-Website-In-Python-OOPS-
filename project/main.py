from authentication import *
from product import *
from order import *
print("--------------  Welcome to SAHANA STORES  -------------")
while(1):
    print('Please select an option:\n1.REGISTER\n2.LOGIN\n3.EXIT')
    n=int(input('Enter your option no:'))
    if n==1:
        print("----------------Registration form---------------")
        us=input("Enter your username:")
        p=input("Enter your password:")
        m=input("Enter your mail id:")
        ph=input("Enter your phone number:")
        add=input("Enter your address:")
        obj=Authentication()
        obj.register(us,p,m,ph,add)
    if n==2:
        print("---------------- Login Page ---------------")
        res=True
        while(res):
            us=input("Enter your username:")
            p=input("Enter your password:")
            obj=Authentication()
            res=obj.login(us,p)
        break
    if n==3:
        obj=Authentication()
        obj.exit()
        break
if res==False:
    while(1):
        obj=Product()
        obj.display_products()
        c=int(input("\nEnter the product no you want to explore :"))
        obj.product_details(c)
        i=input("select any option no(1.order  2.go back  ) :")
        if i==2:
            continue
        else:
            obj=Order()
            obj.place_order(c)
            obj=Authentication()
            obj.exit()
        
            
    


      


