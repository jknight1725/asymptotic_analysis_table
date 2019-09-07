import numpy as np
import pandas as pd
from math import log2, sqrt, floor


# Each function represents the time complexity of an algorithm
# returns the Highest N that could be solved in a given time t in microseconds
def log_n(t):
    return f"2^{sci_format(t)}"


def sqrt_n(t):
    return sci_format(t ** 2)


def n(t):
    return sci_format(t)


# Calculus(newtons method) - could be made recursive or add iterations for greater accuracy
# a0 = n/log2n
# ak+1 = a0 -   ( (a0 log a0) - t / ( 1 / ln(2)  + log2 a0 ))
def n_log_n(t):
    a0 = t / log2(t)
    a1 = a0 - ((a0 * log2(a0) - t) / ((1 / 1.44) + log2(a0)))
    return sci_format(a1)


def n_squared(t):
    return floor(sqrt(t))


def n_cubed(t):
    return floor(t ** (1. / 3.))


def two_raised_n(t):
    return floor(log2(t))


def n_factorial(t):
    i = 2
    j = 1
    c = 0
    while j < t:
        j *= i
        i += 1
        c += 1
    return c


# Formats a number into scientific notation with two decimal places
# e.g. sci_format(1000) returns 1.00e+3
def sci_format(number):
    return '{:.2e}'.format(number)


# Expects function and a dictionary containing numerical values
# Returns a list of each dict value mutated by the respective fcn
def generate_row(fcn, arg):
    row = [*arg.values()]
    return [fcn(x) for x in row]


# times in MICROSECONDS
times_in_ms = {
    'second': (10 ** 6),
    'minute': (10 ** 6) * 60,
    'hour': (10 ** 6) * 60 * 60,
    'day': (10 ** 6) * 60 * 60 * 24,
    'month': (10 ** 6) * 60 * 60 * 24 * 30,
    'year': (10 ** 6) * 60 * 60 * 24 * 365,
    'century': (10 ** 6) * 60 * 60 * 24 * 365 * 100
}

# Row Headers - Big O to analyze
time_complexity = np.array(['lg n', 'sqrt n', 'n', 'n lg n', 'n^2', 'n^3', '2^n', 'n!'])

# Col Headers - Each key of the times_in_ms dict in order
time = np.array([*times_in_ms])

# Generates data for table rows by calling each fcn in fcn_list with each value in the times_in_ms dict
fcn_list = [log_n, sqrt_n, n, n_log_n, n_squared, n_cubed, two_raised_n, n_factorial]
table_rows = np.array([
    generate_row(fcn, times_in_ms) for fcn in fcn_list
])

# Generate html table code with pandas using numpy arrays as input
table = pd.DataFrame(table_rows, index=time_complexity, columns=time)
html_table = table.to_html()
print(html_table)
