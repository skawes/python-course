class Demo(object):
    def __init__(self,name,price):
        self.name=name
        self.price=price

d1=Demo("Awes",500)
print("{0.name},{0.price}".format(d1))