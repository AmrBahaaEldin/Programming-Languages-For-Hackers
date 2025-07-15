#!/usr/bin/python3
wordList=["admin","123","password123","administrator","ceo"]
for word in wordList:
    if "in" in word:
       print(word)

def sum():
    x,y=3,4
    return x+y
print(sum())



print("_______________________________________")
def sum(x):
    y=3
    return x+y
print(sum(100))




print("_______________________________________")



class NewClass:
    def main(self):
        print("this is a Big BOy")
myClass=NewClass()
myClass.main()



print("_______________________________________")

class NewClass1:
    def newFunc(self):
        x=4
        self.x=x
    def another(self):
        print(self.x)
myClass=NewClass1()
myClass.newFunc()
myClass.another()

print("_______________________________________")

#country is no public all method
#self is can allow using all method 

class Car:
   def __init__(self,color,dateAppear,country):
     self.color=color
     self.dateAppear=dateAppear
     print("this is my car")
     self.buildin()
     self.firstLook(country=country)
   def buildin(self):
       print(f"bmw MX600 {self.color}")
   def firstLook(self,country):
       print(f"bmw MX600 {self.dateAppear} in {country}")



myBMW=Car(color="red",dateAppear="2010",country="italy")



