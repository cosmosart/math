def synthetic_division(x,equation_coff):
    """ 
    Polynomial remainder theorem
    https://en.wikipedia.org/wiki/Polynomial_remainder_theorem
    """
    output = []
    division = 0
    for i in range(len(equation_coff)):
        y = equation_coff[i] + division
        output.append(y)
        division = x * y
    
    return(output[:-1], output[-1])

# 
