import hashlib
import time
import sys

def number():
    num = int(input("Enter number: "))
    if num >= 1000000000 and num<=9999999999:
        print(num)
    else:
        print("Invalid Number Enter again")
        number()

totalsum = []


def bill():
    print("***ENTER YOUR DETAILS*****")
    billname=str(input("Enter your name : "))
    date=str(input("Enter Today's data(dd/mm/yy) : "))
    print("=================Total Bill===================")
    print("Date",date)
    print("Name : ",billname)
    print("==============================================")
    print("Total Bill:",sum(totalsum))
    print("1.cash")
    print("2.card")
    print("\nEnter your choice : ")
    chcash=int(input())
    if(chcash==1):
        cashamount=float(input("Enter the amount customer given : "))
        balance=cashamount-sum(totalsum)
        print("balance : ",balance)
    else:
        cardnum=int(input("Enter Your Card Number:"))
        cardname=str(input("Enter Card Holder Name:"))
        topayamount=int(input("Enter Total Bill:"))
        cardpin=int(input("Enter Your Pin:"))
            
        print("Amount piad Successfully!")
    house=str(input("Enter Your Address:"))
    pins=int(input("Enter Your Postal Code:"))
    number()    
    print("Your Order is Confirmed!!")
    print("**THANKYOU**")
    sys.exit() 


def res():
    costv=[120,120,100,150,150,150,250,250,300,350]  
    sumv=0
    

    costf=[600,550,999,899,1199,1299,1350,1450,250,200]
    sumf=0

    costb=[59,189,220,265,131,220,235,105,79,99]
    sumb=0

    costd=[164,115,179,179,179,129,179,179,155,109]
    sumd=0

    costs=[210,220,210,250,200,180,210,145,180,140]
    sums=0

    coste=[265,275,205,215,255,205,300,205,330,235]
    sume=0


    while True:
        print("\n*********Select your Restaurant*******")
        print("1.Veg Street")
        print("2.Mandi")
        print("3.Mc.Donalds")
        print("4.KFC")
        print("5.Brew Buzz")
        print("6.Star Bucks")
        ch1=int(input("select your choice : \n"))
    
        if (ch1==1):
            print("*****MENU*****")
            print("1.Spring Rolls-Rs:120")
            print("2.Paneer 65-RS:120")
            print("3.Chilli Mushroom-Rs:100")
            print("4.Gobi 65-Rs:150")
            print("5.Crispy Corn-RS:150")
            print("6.Veg Friedrice-Rs:150")
            print("7.Manchurian Rice-Rs:250")
            print("8.Paneer Friedrice-Rs:250")
            print("9.Veg Biryani-Rs:300")
            print("10.Paneer Biryani-Rs:350")
            for i in range(1):
                j=int(input("Enter choice : "))
                Quantity=float(input("Enter Quantity : "))
                amount=Quantity*costv[j-1]
                sumv=sumv+amount
            totalsum.append(sumv)
            print("Total Bill: ",sumv)
            a=(int(input("Press 1 to continue or 0 to bill : ")))
            if a == 1:
                res()
            elif a == 0:
                print("YOUR BILL IS PROCESSING")
                print(".")
                print("..")
                time.sleep(2)
                bill()
        
        
        
        if (ch1==2):
            print("*****MENU*****")
            print("1.Mixed Veg Mandi-Rs:600(Couple)")
            print("2.Paneer Mandi-Rs:550(Couple)")
            print("3.Chicken BBQ Mandi-Rs:999(Full)")
            print("4.Chicken Steak Mandi-Rs:899(Full)")
            print("5.Mutton Juicy Mandi-Rs:1199(Full)")
            print("6.Bhuna Gosth(Mutton)Mandi-Rs:1299(Jumbo)")
            print("7.Grill Fish Mandi-Rs:1350(Jumbo)")
            print("8.Prawn Mandi-Rs:1450(Jumbo)")
            print("9.Mutton Bone Soup-Rs:250(1)")
            print("10.Hot And Sour Soup-Rs:200(1)")
            for i in range(1):
                j=int(input("Enter choice : "))
                quantity=float(input("Enter Quantity : "))
                amount=quantity*costf[j-1]
                sumf=sumf+amount
            totalsum.append(sumf)
            print("Total Bill: ",sumf)
            a=(int(input("Press 1 to continue or 0 to bill : ")))
            if a == 1:
                res()
            elif a == 0:
                print("YOUR BILL IS PROCESSING")
                print(".")
                print("..")
                time.sleep(2)
                bill()
        
        if (ch1==3):
            print("*****MENU*****")
            print("1.McAloo Tikki Burger-Rs:59")
            print("2.McSpicy Paneer Wrap-Rs:189")
            print("3.Veg Maharaja Mac-Rs:220")
            print("4.Happy Meal-Rs:265")
            print("5.McChicken Burger-Rs:131")
            print("6.Big Spicy Chicken Wrap-Rs:220")
            print("7.Chicken Maharaja Mac-Rs:235")
            print("8.Nuggets-Rs:105(6)")
            print("9.French Fries-Rs:79(Large)")
            print("10.McFlurry Oreo-Rs:99")
            for i in range(1):
                j=int(input("Enter choice : "))
                item=float(input("Enter Quantity : "))
                amount=item*costb[j-1]
                sumb=sumb+amount
            totalsum.append(sumb)
            print("Total Bill:",sumb)
            a=(int(input("Press 1 to continue or 0 to bill : ")))
            if a == 1:
                res()
            elif a == 0:
                print("YOUR BILL IS PROCESSING")
                print(".")
                print("..")
                time.sleep(2)
                bill()
        
        if (ch1==4):
            print("*****MENU*****")
            print("1.Chicken Popcorn-Rs:164(Medium)")
            print("2.Hot And Crispy-Rs:115(1 PCS)")
            print("3.Smoky Red Grilled Chicken-Rs:179(2 PCS)")
            print("4.Pop Corn Rice Bowl-Rs:179")
            print("5.Smoky Red Grilled Chicken Bowl-Rs:179")
            print("6.Veg Rice Bowl-Rs:129")
            print("7.Tandoori Zinger Burger-Rs:179")
            print("8.Veg Zinger Burger-Rs:179")
            print("9.Veg Patty-Rs:155(2 PCS)")
            print("10.Choco lava-Rs:109")
            for i in range(1):
                j=int(input("Enter choice : "))
                item=float(input("Enter Quantity : "))
                amount=item*costd[j-1]
                sumd=sumd+amount
            totalsum.append(sumd)
            print("Total Bill:",sumd)
            a=(int(input("Press 1 to continue or 0 to bill : ")))
            if a == 1:
                res()
            elif a == 0:
                print("YOUR BILL IS PROCESSING")
                print(".")
                print("..")
                time.sleep(2)
                bill()
        
        if (ch1==5):
            print("*****MENU*****")
            print("1.Fruity Bliss-Rs:210")
            print("2.Dark Passion-Rs:220")
            print("3.Choco O Hola-Rs:210")
            print("4.Chocolate Avalanche-Rs:250")
            print("5.Death By Chocolate-Rs:200")
            print("6.Browine-Rs:180")
            print("7.Chocolate Sandwich-Rs:210")
            print("8.Veg Sandwich-Rs:145")
            print("9.Special Veg Sandwich-Rs:180")
            print("10.Chocolate Truffle-Rs:140")
            for i in range(1):
                j=int(input("Enter choice : "))
                item=float(input("Enter Quantity : "))
                amount=item*costs[j-1]
                sums=sums+amount
            totalsum.append(sums)
            print("Total Amount for this category",sums)
            a=(int(input("Press 1 to continue or 0 to bill : ")))
            if a == 1:
                res()
            elif a == 0:
                print("YOUR BILL IS PROCESSING")
                print(".")
                print("..")
                time.sleep(2)
                bill()
         
        if (ch1==6):
            print("*****MENU*****")
            print("1.Java Chip Frappuccino-Rs:265")
            print("2.Double Chocolate Chip Frappuccino-Rs:275")
            print("3.Caffe Latte-Rs:205")
            print("4.Signature Hot Chocolate-Rs:215")
            print("5.Cold Coffee-Rs:255")
            print("6.Caffe Americano-Rs:205")
            print("7.Caramel Macchiato-Rs:300")
            print("8.Caffe Latte-Rs:205")
            print("9.Mocha Frappuccino-Rs:330")
            print("10.Iced Caffe Latte-Rs:235")
            for i in range(1):
                j=int(input("Enter choice : "))
                item=float(input("Enter Quantity : "))
                amount=item*coste[j-1]
                sume=sume+amount
            totalsum.append(sume)
            print("Total Amount for this category",sume)
            
            a=(int(input("Press 1 to continue or 0 to bill : ")))
            if a == 1:
                res()
            elif a == 0:
                print("YOUR BILL IS PROCESSING")
                print(".")
                print("..")
                time.sleep(2)
                bill()

while(1):
    print("=======================Welcome to food paradise==================\n")
    print("**********Login System********")
    print("1.Signup:")
    print("2.Login:")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("credentials.txt", "w") as f:
                f.write(email + "\n")
                f.write(hash1)
                f.close()
                print("You have registered successfully!")
                
        else:
            print("Password is not same as above!")
    elif ch == 2:
        email = input("Enter email: ")
        pwd = input("Enter password: ")
        auth = pwd.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open("credentials.txt", "r") as f:
            stored_email, stored_pwd = f.read().split("\n")
        f.close()
        if email == stored_email and auth_hash == stored_pwd:
            print("Logged in Successfully!")
            res()
            break
        else:
            print("Login failed!")
    else:
        print("Wrong Choice!")
