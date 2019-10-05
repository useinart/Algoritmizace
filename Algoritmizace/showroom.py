class Car:
    def __init__(self,identification,name,brand,price,active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active

class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode

class LinkedList:
    def __init__(self):
        self.head = None

db = LinkedList()

def init(cars):
    for car in cars:
        add(car)

def add(data):
    if db.head is None:
        new_Node = Node(None, None, data)
        new_Node.prevNode = None
        db.head = new_Node
    else:
        new_Node = Node(None, None, data)
        if new_Node.data.price < db.head.data.price:
            new_Node.nextNode = db.head
            db.head.prevNode = new_Node
            db.head = new_Node
        else:
            cur = db.head
            while new_Node.data.price >= cur.data.price:
                if cur.nextNode == None:
                    break
                cur = cur.nextNode
            last = cur.prevNode
            if new_Node.data.price < cur.data.price:
                new_Node.nextNode = cur
                new_Node.prevNode = last
                cur.prevNode = new_Node
                last.nextNode = new_Node
            else:
                cur.nextNode = new_Node
                new_Node.prevNode = cur
                new_Node.nextNode = None

def getDatabase():
    return db

def getDatabaseHead():
    return db.head

def updateName(identification,name):
    cur = db.head
    while cur.data.identification != identification:
        if cur.nextNode == None:
            return None
        cur = cur.nextNode
    cur.data.name = name

def updateBrand(identification,brand):
    cur = db.head
    while cur.data.identification != identification:
        if cur.nextNode == None:
            return None
        cur = cur.nextNode
    cur.data.brand = brand

def activateCar(identification):
    cur = db.head
    while cur.data.identification != identification:
        if cur.nextNode == None:
            return None
        cur = cur.nextNode
    cur.data.active = True

def deactivateCar(identification):
    cur = db.head
    while cur.data.identification != identification:
        if cur.nextNode == None:
            return None
        cur = cur.nextNode
    cur.data.active = False

def calculateCarPrice():
    carPrice = 0
    cur = db.head
    while cur != None:
        if cur.data.active == True:
            carPrice += cur.data.price
        cur = cur.nextNode
    return carPrice

def clean():
    db.head = None




'''first = Car(1,'rx','mazda',2000,True)
second = Car(2,'x','bmv',3000,True)
third = Car(3,'italia' , 'ferrari' , 1500 , True)
fourth = Car(4,'fer' , 'ferra' , 2500 , True)
fifth = Car(5,'lambo' , 'ferra' , 4000 , True)
six = Car(6,'lamb' , 'ferr' , 500 , True)
seven = Car(7,'lam' , 'fer' , 2700 , True)
eight = Car(8,'xt' , 'ford' ,90000 , True)
nine = Car(9,'9' , 'lada' , 3 , True)
ten = Car(10 , 'x' , 'tesla' , 3000 , True)
arturaArray = [first,second,third,fourth,fifth,six,seven,eight,nine,ten]
init(arturaArray)


while db.head.next is not None:
    print(db.head.data.brand)
    db.head = db.head.next
print(db.head.data.brand)'''