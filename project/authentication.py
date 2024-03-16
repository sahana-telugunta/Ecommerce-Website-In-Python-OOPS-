import csv
class Authentication:
    def __init__(self):
        #print("------------  Welcome to SAHANA STORES  -----------")
        #print('please select an option:\n1.LOGIN\n2.REGISTER\n3.EXIT')
        pass
    def register(self,username,password,mail,phno,address):
        with open('data.csv','a',newline='') as f:
            a=csv.writer(f)
            a.writerow([username,password,mail,phno,address])
            f.close()
            return print("----- Registration Successful -----")
    def login(self,username,password):
        with open('data.csv','r',newline='') as f:
            r=csv.DictReader(f)
            for i in r:
                if i['username']==username and i["password"]==password:
                    print("------- Login Successful -------")
                    return False
            print("Invalid user name or password try again")
            return True
    def exit(self):
        print("------- Thank you for visiting sahana stores. Visit again -------")
        return exit()