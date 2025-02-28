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