def sansuExe(type="K", numberOfExec = 10):
    """
    Math exercise for 1st and 2nd grade of Japanese elementary students

    Usage
    sansuExe(type, numberOfExec)
    
    type
    T = plus
    H = minus
    K = product(product table)

    numberOfExec = number of exercise integer number

    """
    import numpy as np
    correct = {}
    num = 0

    if type=="T" or type =="t":
        for i in range(numberOfExec):
            a = np.random.randint(10,150)
            b = np.random.randint(10,200)
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
                print(f"ぷーぶ {a} + {b} = {a+b}")
                correct.update({i+1:"X"})
    elif type=="K" or type=="k":
        for i in range(numberOfExec):
            a = np.random.randint(2,9)
            b = np.random.randint(2,9)
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
                print(f"ぷーぶ {a} x {b} = {a*b}")
                correct.update({i+1:"X"})
    elif type=="H" or type == "h":
        for i in range(numberOfExec):
            a = np.random.randint(10,150)
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
                print(f"ぷーぶ {a} - {b} = {a-b}")
                correct.update({i+1:"X"})          
    else:
        print("Check your input")
    return f"Total {num}/{numberOfExec}", correct

if __name__ == "__main__":
    tOe = input("足し算は　T を、くくは　K を入れてください。")
    try:    nOe = int(input("何回練習しましょうか"))
    except:    print("数字を入れてください。"); nOe = int(input("何回練習しましょうか  "))
    sansuExe(tOe, nOe)

