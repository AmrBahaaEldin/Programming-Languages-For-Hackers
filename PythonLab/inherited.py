#!/usr/bin/pthon3
class parent():
    def __init__(self):
        self.hi()

    def hi(self):
        x=5
        print(x)
class child(parent):
    def __init__(self):
        super().__init__()
   

       

mychild=child()    
