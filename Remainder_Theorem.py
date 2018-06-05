def synthetic_division(x,equation_coff):
    output = []
    division = 0
    for i in range(len(equation_coff)):
        y = equation_coff[i] + division
        output.append(y)
        division = x * y
    
    return(output[:-1], output[-1])

##Polynomial remainder theorem
