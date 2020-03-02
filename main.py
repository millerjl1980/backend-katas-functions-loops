#!/usr/bin/env python
import argparse
import sys

"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Justin Miller"


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
        i = i - 1
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
    parser = argparse.ArgumentParser(description= "Help")
    parser.add_argument('-x', action='store', type=int, help='Number for X')
    parser.add_argument('-y', action='store', type=int, help='Number for Y')
    parser.add_argument('-n', action='store', type=int, help='Number for N')
    parser.add_argument('-func', action='store', type=str, help='What type of operation: add, mult, pow, fact, fib')
    args = parser.parse_args()

    if args.func == 'add':
        print(add(args.x, args.y))
    elif args.func == 'mult':
        print(multiply(args.x, args.y))
    elif args.func == 'pow':
        print(power(args.x, args.n))
    elif args.func == 'fact':
        print(factorial(args.x))
    elif args.func == "fib":
        print(fibonacci(args.n))
