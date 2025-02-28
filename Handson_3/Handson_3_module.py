def Input()->float:
    Sum = 0
    while (True):    
        cost = float(input("Cost of item: "))
        if cost == 0: break
        Sum += cost
    return Sum

def calculateTax(Total:float)->float:
    return round(Total * 0.06, 2)

def afterTax(Total:float)->float:
    return (Total + calculateTax(Total))

def feetToMeters(distance:float)->float:
    distance = round(distance * 0.3048, 2)
    return distance

def metersToFeet(distance:float)->float:
    distance = round(distance / 0.3048, 2)
    return distance

def displayTitle():
    print("Conversions Menu:\na.\tFeet to Meters\nb.\tMeters to Feet")
    
