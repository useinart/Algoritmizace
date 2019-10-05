class Fridge:
    def __init__(self,name,minimalCofeinRequired):
        self.name = name
        self.minimalCofeinRequired = minimalCofeinRequired
        self.items = []

class Items:
    def __init__(self,name,coffeCapacity,number):
        self.name = name
        self.coffeCapacity = coffeCapacity
        self.number = number

def biggestCofeinInFridge(array):
    answer = max(array)
    return answer

def isWorkingAllNight(itemsInFridge,cofeinRequired):
    coffein = 0
    sum = cofeinRequired + cofeinRequired*0.1
    for cofie in range(len(itemsInFridge)):
        if itemsInFridge[cofie] < 0:
            continue
        else:
            coffein += itemsInFridge[cofie]
    if (coffein <= sum) and (coffein >= cofeinRequired):
        return 0
    elif coffein > cofeinRequired:
        return 1
    elif coffein < cofeinRequired:
        return -1

def whenCallSupplier(itemsInFridge,consumptions):
    days = 0
    coffein = 0
    for cofie in range(len(itemsInFridge)):
        if itemsInFridge[cofie] < 0:
            continue
        else:
            coffein += itemsInFridge[cofie]
    for day in range(len(consumptions)):
        if coffein >= consumptions[day]:
            print(day)
            if day == len(consumptions) - 1:
                days = -1
                return days
            coffein -= consumptions[day]
            days += 1
            continue
        elif coffein < consumptions[day]:
            break
    return days






print(str(biggestCofeinInFridge([1,0,3])))
print(str(isWorkingAllNight([1,10,10,-3],20)))

print(str(whenCallSupplier([1,-1,1,10],[2,3,1,2,0,3])))
