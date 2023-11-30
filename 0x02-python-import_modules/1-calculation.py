#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

#Call functions and print results

sum_result = add(a, b)
print(f"Addition: {a} + {b} = {sum_result}")

difference_result = sub(a, b)
print(f"Subtraction: {a} - {b} = {difference_result}")

product_result = mul(a, b)
print(f"Multiplication: {a} * {b} = {product_result}")

division_result = div(a, b)
print(f"Division: {a} / {b} = {division_result}")
