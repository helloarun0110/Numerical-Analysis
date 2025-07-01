def func(x):
    return x ** 5 - 3 * x + 5

def derivative(x):
    return 5 * x ** 4 - 3

def newton_raphson(x0, tol = 1e-3, max_iter = 100):
    iter = 0

    while iter < max_iter:
        f_x = func(x0)
        f_prime_x = derivative(x0)

        if f_prime_x == 0:
            print("derivative is zero, no solution found")
            return None, iter
        
        x1 = x0 - f_x / f_prime_x
        if abs(x1 - x0) < tol:
            return x1, iter
        
        x0 = x1
        iter += 1

    print("maximum iterations reached no solution found")
    return None, iter

x0 = float(input("enter initial guess: "))
root, iterations = newton_raphson(x0)
if root is not None:
    print(f"newton raphson root: {root}, iterations: {iterations}")


