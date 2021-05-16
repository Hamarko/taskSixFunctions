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


def constructor(f, x):
    return {
        "a": fun_a(x),
        "b": fun_b(x),
        "c": fun_c(x),
        "d": fun_d(x),
        "e": fun_e(x),
        "f": fun_f(x),
    }.get(f)