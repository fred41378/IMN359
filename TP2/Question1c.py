import sympy as sp

x= sp.Symbol('x')

f = sp.cos(x)
g = sp.cos(4*x)

integrand = f*g
integrale = sp.integrate(integrand, (x, -sp.pi, sp.pi))

print("Le resultat est : ", integrale)