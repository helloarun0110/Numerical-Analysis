import math

def func(x):
    return math.log(x * 3) - 3

def regula_falsi(a, b, tol = 1e-4, max_iter = 100):
    if func(a) * func(b) > 0:
        print("No root found in the interval.")
        return None, 0
    
    iter = 0
    while iter < max_iter:
        c = b - (func(b) * (a - b)) / (func(a) - func(b))
        if abs(func(c)) < tol:
            return c, iter
        
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iter += 1

    return c, iter



root, iterations = regula_falsi(2, 10)
print(f"Regula Falsi Root: {root}, iterations: {iterations}")