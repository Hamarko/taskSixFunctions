def fun_a(x):
    return x ** 2


def fun_b(x):
    return 2 * x + 1


def fun_c(x):
    return x - 1


def fun_d(x):
    return x / 10


def fun_e(x):
    return x + 10


def fun_f(x):
    return x/2

def constructor(f,x):
    if f == "a": return fun_a(x)
    if f == "b": return fun_b(x)
    if f == "c": return fun_c(x)
    if f == "d": return fun_d(x)
    if f == "e": return fun_e(x)
    if f == "f": return fun_f(x)
    return None