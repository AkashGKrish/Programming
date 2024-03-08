#!/usr/bin/env python


def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

#Memoization
memo_dict = {}

def dynamic_fib(n):
    if n <= 0:
        return 0
    
    # Base cases
    if n == 1 or n == 2:
        return 1
    
    # Check if result is already memoized
    if n in memo_dict:
        return memo_dict[n]
    
    # Recursive case
    result = dynamic_fib(n - 1) + dynamic_fib(n - 2)
    
    # Memoize the result
    memo_dict[n] = result

    return result


print(dynamic_fib(1))
print(dynamic_fib(2))
print(dynamic_fib(3))
print(dynamic_fib(4))
print(dynamic_fib(5))
print(dynamic_fib(100))