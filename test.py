import sympy as sp
#굿

def function():
    formula_input = input("함수 입력: ")
    x = sp.Symbol('x')
    formula = sp.sympify(formula_input)


    taylor = sp.series(formula, x, 0, 6)
    print("테일러 급수: {}". format(taylor))

function()

