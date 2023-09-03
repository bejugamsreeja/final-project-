#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Admin:
    l=[]
    def __init__(self,FoodID,name,quantity,price,discount,stock):
        self.FoodID=FoodID
        self.name=name
        self.quantity=quantity
        self.discount=discount
        self.stock=stock
    def add_items(self,FoodID,name,quantity,price,discount,stock):
        d=dict()
        d['FoodID':self.FoodID]
        d['name':self.name]
        d['quantity':self.quantity]
        d['price':self.price]
        d['discount':self.discount]
        d['stock':self.stock]
        l.append(d)
    def edit_items(self,FoodID,Food,name,quantity,price,discount,stock):
        for i in Food.keys():
            if i== FoodID:
                self.name=name
                self.quantity=quantity
                self.price=price
                self.discount=discount
                self.stock=stock
        
    def view_List(self,Food):
        self.Food=Food
        return Food
    def remove_Food(self,FoodID,Food):
        del Food[FoodID]
class user:
    def __init__(self):
        pass
    def register(self,fname,phnum,email,add,pwd,re_List):
        
        fname=input("Input name")
        re_List.append(fname)
        phnum=input("Phone number")
        re_List.append(phnum)
        email=input("Email")
        re_List.append(email)
        add=input("Address")
        re_List.append(add)
        pwd=input("Passowrd")
        re_List.append(pwd)
        print("Registartion is Successful")
        return re_List
    def Login(self,email,pwd,re_List):
        email=input("Please enter your Email ID")
        pwd=input("please enter your pwd")
        e,p=0,0
        for i in re_List:
            if i==email:
                e=1
            if i==pwd:
                p=1
        if e==1 and p==1:
            print("Login has successful")
        else:
            print("Email or password is wrong")
    def options(self,cart):
        print("1.Place New Order")
        print("2.Order History")
        print("3.Update Profile")
    def placeOrderMenu(self,Food):
        print(Food)
    def select(self,c,Food,cart):
        for i in c:
            for j in Food.keys():
                if j==i:
                    cart.append(Food[j])
        cart=["Tandoori Chicken","Vegan Burger"]
        return cart
    def placeOrder(self,cart):
        print("Order has placed Successfully")
    def orderHistory(self,cart):
        print("Previous order is:",cart)
    def updateProfile(self,phnum,email,add,pwd,re_List):
        re_List[1]=phnum
        re_List[2]=email
        re_List[3]=add
        re_List[4]=pwd
        print("Profile Updated Successfully")
        return re_List
    
    
        
Food={1:"Tandoori Chicken",2:"Vegan Burger",3:"Tuffle Cake",4:"paneer puff"}
re_List=[]
#A.Add_items(1,"Tandoori Chicken",2,100,5,"yes")
#print(A.l)
A=Admin(1,"cake",2,100,5,"yes")
A.view_List(Food)
print("Stock Before Editing by Admin",A.stock)
#updating Stock by admin
A.edit_items(1,Food,"cake",2,100,5,"No")
print("Stock After Editing by Admin",A.stock)
print("Menu before Removing item from List",A.view_List(Food))
#Removing food From List
k=int(input("please enter the item to remove from list"))
A.remove_Food(k,Food)
print("Menu After Removing item from List",A.view_List(Food))
cart=[]
U=user()
re_List=[]
re_List=U.register( _,_,_,_,_,re_List)
U.Login(_,_,re_List)
U.options(cart)
U.placeOrderMenu(cart)
c=list()
a=input("please enter the id of Food")
b=input("please enter the id of Food")
c.append(a)
c.append(b)
cart=U.select(c,Food,cart)
print(cart)
U.placeOrder(cart)
U.orderHistory(cart)
U.updateProfile("960","abc@gmail.com","Hyd","xyz",re_List)


# In[ ]:





# In[ ]:




