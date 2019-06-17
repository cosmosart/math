def interest_calculate(amount, rate, year, compound = 1, continus = False):
    import math
    if continus == False:
        return round(amount * (1 + (rate/100)/compound)**(year*compound),2)
    elif continus == True:
        return round(amount * math.exp((rate/100)*year),2)
    else:
        print('Usage "interest_calculate(amount, rate, year, compound(option), continus(option))"')
