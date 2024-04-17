from methods import dichotomy, golden_ratio
import numpy as np
import matplotlib.pyplot as plt

from graphics import plot_compare, plot_target
from utils import PrintableFunction

from math import sin, exp, log, cos, e
from typing import Any
from utils import N_steps_dichotomy_analytical, N_steps_gr_analytical

f_1 = PrintableFunction(lambda x:((x-0.5)**2/4)+8, "((x - 0.5)^2 / 4) + 8")
#f_2 = PrintableFunction(lambda x: log((x-0.5)**2, e), "-16sin(x) + 4x^2 - 10")
#f_3 = PrintableFunction(lambda x: -6*exp(-0.3*(x-1)**2)+3, "60cos(0.3x - 2) + 50")

a, b = -1, 1
f = f_1
digits1 = 1
digits2 = 2
digits3 = 3
eps1 = 10**-digits1
eps2 = 10**-digits2
eps3 = 10**-digits3

a_d, b_d, n_d = dichotomy(f, a, b, eps1, eps1*1e-1)
a_g, b_g, n_g = golden_ratio(f, a, b, eps1)

print(f"Функция: {f_1}\n")
print(f"eps = {eps1}\n")

print(f"Метод дихотомии:")
print(f"\tПолученный интервал: [{round(a_d, digits1+1)}, {round(b_d, digits1+1)}], число вызовов функции: {n_d}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_dichotomy_analytical(a, b, eps1, eps1*1e-1)}\n")

print(f"Метод золотого сечения:")
print(f"\tПолученный интервал: [{round(a_g, digits1+1)}, {round(b_g, digits1+1)}], число вызовов функции: {n_g}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_gr_analytical(a, b, eps1)}\n")
print("----------------------------------------------\n")

a_d, b_d, n_d = dichotomy(f, a, b, eps2, eps2*1e-1)
a_g, b_g, n_g = golden_ratio(f, a, b, eps2)

print(f"Функция: {f_1}\n")
print(f"eps = {eps2}\n")

print(f"Метод дихотомии:")
print(f"\tПолученный интервал: [{round(a_d, digits2+1)}, {round(b_d, digits2+1)}], число вызовов функции: {n_d}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_dichotomy_analytical(a, b, eps2, eps2*1e-1)}\n")

print(f"Метод золотого сечения:")
print(f"\tПолученный интервал: [{round(a_g, digits2+1)}, {round(b_g, digits2+1)}], число вызовов функции: {n_g}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_gr_analytical(a, b, eps2)}\n")
print("----------------------------------------------\n")

a_d, b_d, n_d = dichotomy(f, a, b, eps3, eps3*1e-1)
a_g, b_g, n_g = golden_ratio(f, a, b, eps3)

print(f"Функция: {f_1}\n")
print(f"eps = {eps3}\n")

print(f"Метод дихотомии:")
print(f"\tПолученный интервал: [{round(a_d, digits3+1)}, {round(b_d, digits3+1)}], число вызовов функции: {n_d}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_dichotomy_analytical(a, b, eps3, eps3*1e-1)}\n")

print(f"Метод золотого сечения:")
print(f"\tПолученный интервал: [{round(a_g, digits3+1)}, {round(b_g, digits3+1)}], число вызовов функции: {n_g}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_gr_analytical(a, b, eps3)}\n")
print("----------------------------------------------\n")

plot_target([f_1], a, b)

plot_compare(f_1, a, b, [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9])

'''new_function = PrintableFunction(lambda x: e**x - 1/3*x**3 + 2*x, "e^x - 1/3 x^3 + 2x")

a, b = -2, 1
f = new_function
digits = 3
eps = 3**-digits

a_d, b_d, n_d = dichotomy(f, a, b, eps)
a_g, b_g, n_g = golden_ratio(f, a, b, eps)

print(f"eps = {eps}\n")

print(f"Метод дихотомии:")
print(f"\tПолученный интервал: [{round(a_d, digits+1)}, {round(b_d, digits+1)}], число вызовов функции: {n_d}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_dichotomy_analytical(a, b, eps)}\n")

print(f"Метод золотого сечения:")
print(f"\tПолученный интервал: [{round(a_g, digits+1)}, {round(b_g, digits+1)}], число вызовов функции: {n_g}")
print(f"\tАналитический расчёт числа вызовов функции: {N_steps_gr_analytical(a, b, eps)}\n")'''


def compare_epsilons_dichotomy(method, function, a, b, digits, method_name=None):
    if method_name:
        print(f"Метод: {method_name}\n")

    print(f"Функция: {function}\n")
    print(f"На интервале [{a}, {b}]\n")

    print('|' + '|'.join(map(str, digits)) + '|')
    print("|" + '|'.join(["--"] * len(digits)) + "|")
    intervals = []
    number_of_calls = []
    for i in range(len(digits)):
        eps = 10 ** -digits[i]
        left_limit, right_limit, n = method(function, a, b, eps, eps*1e-1)
        intervals.append((round(left_limit,5 ), round(right_limit,5 )))
        number_of_calls.append(n)
    print('|' + '|'.join(map(str, intervals)) + '|')
    print('|' + '|'.join(map(str, number_of_calls)) + '|')

def compare_epsilons_gr(method, function, a, b, digits, method_name=None):
    if method_name:
        print(f"Метод: {method_name}\n")

    print(f"Функция: {function}\n")
    print(f"На интервале [{a}, {b}]\n")

    print('|' + '|'.join(map(str, digits)) + '|')
    print("|" + '|'.join(["--"] * len(digits)) + "|")
    intervals = []
    number_of_calls = []
    for i in range(len(digits)):
        eps = 10 ** -digits[i]
        left_limit, right_limit, n = method(function, a, b, eps)
        intervals.append((round(left_limit,5 ), round(right_limit,5 )))
        number_of_calls.append(n)
    print('|' + '|'.join(map(str, intervals)) + '|')
    print('|' + '|'.join(map(str, number_of_calls)) + '|')

#plot_target([new_function], a, b)

#plot_target([f_2], -10, 10)

compare_epsilons_gr(golden_ratio, f_1, -1, 1, [1, 2, 3], method_name="Метод золотого сечения")
print("----------------------------------------------\n")
compare_epsilons_dichotomy(dichotomy, f_1, -1, 1, [1, 2, 3], method_name="Метод дихотомии")