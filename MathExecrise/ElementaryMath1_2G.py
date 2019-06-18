def sansuExe(type="K", numberOfExec = 10, lang="J", boundaryA = 150, boundaryB = 200, boundaryC = 9, id = 0):
    """
    Math exercise for 1st and 2nd grade of Japanese elementary students

    Usage
    sansuExe(type, numberOfExec)
    
    type
    T = plus
    H = minus
    K = product(product table)
    D = divide

    boundary are random integer number boundary for exercise
    boundaryA for plus and minus, boundaryA for first number boundary for second number
    boundaryA + boundaryB  
    or 
    boundaryA - boundaryB
    
    boundaryC for product and divide 
    boundaryC * boundaryC 
    or
    (boundaryC * boundaryC) / boundaryC

    numberOfExec = number of exercise integer number

    id = user ID
    id 0 for guest
    default = 0 

    """
    import numpy as np
    correct = {}
    num = 0
    # if id != 0:

    type = type.upper()

    if type=="P":
        for i in range(numberOfExec):
            a = np.random.randint(boundaryC,boundaryA)
            b = np.random.randint(boundaryC,boundaryB)
            c = input(f"{a} + {b} = ")
            try:
                c = int(c)
            except:
                print("Enter a Number")
                c = input(f"{a} + {b} =")    
            if a + b == c:
                print("OK")
                correct.update({i+1:"OK"})
                num += 1
            else:
                print(f"X {a} + {b} = {a+b}")
                correct.update({i+1:"X"})
    elif type=="T":
        for i in range(numberOfExec):
            a = np.random.randint(2,boundaryC)
            b = np.random.randint(2,boundaryC)
            c = input(f"{a} x {b} = ")
            try:
                c = int(c)
            except:
                print("Enter a Number")
                c = input(f"{a} x {b} =")    
            if a * b == c:
                print("OK")
                correct.update({i+1:"OK"})
                num += 1
            else:
                print(f"X {a} x {b} = {a*b}")
                correct.update({i+1:"X"})
    elif type=="M":
        for i in range(numberOfExec):
            a = np.random.randint(10,boundaryA)
            b = np.random.randint(1,a)
            c = input(f"{a} - {b} = ")
            try:
                c = int(c)
            except:
                print("Enter a Number")
                c = input(f"{a} - {b} =")    
            if a - b == c:
                print("OK")
                correct.update({i+1:"OK"})
                num += 1
            else:
                print(f"X {a} - {b} = {a-b}")
                correct.update({i+1:"X"})
    elif type=="D":
        for i in range(numberOfExec):
            b = np.random.randint(2,boundaryC)
            a = np.random.randint(2,boundaryC) * b
            c = input(f"{a} / {b} = ")
            try:
                c = int(c)
            except:
                print("Enter a Number")
                c = input(f"{a} / {b} =")    
            if a / b == c:
                print("OK")
                correct.update({i+1:"OK"})
                num += 1
            else:
                print(f"X {a} / {b} = {int(a/b)}")
                correct.update({i+1:"X"})
    else:
        print("Check your input")
    return f"Total {num}/{numberOfExec}", correct

if __name__ == "__main__":
    tOe = input("足し算は　P を、くくは　T を入れてください。")
    try:    nOe = int(input("何回練習しましょうか？ "))
    except:    print("数字を入れてください。"); nOe = int(input("何回練習しましょうか？ "))
    sansuExe(tOe, nOe)

