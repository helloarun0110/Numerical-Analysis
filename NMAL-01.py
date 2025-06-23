
# Y = X^3 - X -2
def func(x):
    return x ** 3 - x -2

def bisection_traditional(a, b, epsilon = 0.001):
    if func(a) * func(b) >= 0:
        return None
    
    iter = 0
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if abs(func(c)) < epsilon:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iter += 1
    return (a + b) / 2, iter


def find_root_interval(start, end, step = 0.1):
    x = start
    while x < end:
        if func(x) * func(x + step) < 0:
            return x, x + step
        x += step
    return None, None

def improved_bisection(start, end, step = 0.1, epsilon = 0.001):
    a, b = find_root_interval(start, end, step)
    if a is None or b is None:
        return None, 0
    return bisection_traditional(a, b, epsilon)




start = float(input("Enter start of the interval: "))
end = float(input("Enter end of the interval: "))
step = float(input("Enter the step size for scanning: "))
epsilon = float(input("Enter the error tolerance: "))


root_t, iters_t = bisection_traditional(start, end, epsilon)
print(f"Traditional bisection root: {root_t}, iterations: {iters_t}")

root_i, iters_i = improved_bisection(start, end, step, epsilon)
print(f"Improved bisection root: {root_i}, iterations: {iters_i}")
