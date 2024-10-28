from sympy import *
x, y = symbols('x, y')

solution = solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
pprint(solution)

pprint(integrate(x**2, x))
pprint(integrate(sin(x), y))
pprint(integrate(-x*exp(-x**2/2), x))

y = Function("y")
x = Symbol('x')
y_ = Derivative(y(x), x)
pprint(dsolve(y_ + 5*y(x), y(x)))