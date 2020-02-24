#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    sum_ = x + y
    return sum_


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    mult_s = 0
    for num in range(x):
        mult_s = mult_s + y
    return mult_s


def power(x, n):
    """Raise x to power n, where n >= 0"""
    power_s = x
    for num in range(n):
        power_s = multiply(power_s, x)
    return power_s


def factorial(x):
    """Compute factorial of x, where x > 0"""
    fact_s = 1
    i = x
    while i >=1:
        fact_s = multiply(fact_s, i)
        i -= 1
    return fact_s


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    num1 = 1
    num2 = 0
    num3 = 1
    for num in range(n):
        if num >= 2:
            num3 = num1 + num2
            num1 = num2
            num2 = num3
    return num2


if __name__ == '__main__':
    # your code to call functions above
    pass
