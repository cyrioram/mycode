#!/usr/bin/env python3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#def main():
selection = input("Welcome to the Calculator! Select 1 to add, 2 to subtract, 3 to multiply, or 4 to divide ")

a = float(input("What is your first digit? "))
b = float(input("What is your second digit? "))


if selection == "1":
    print(add(a, b))

elif selection == "2":
    print(subtract(a, b))

elif selection == "3":
     print(multiply(a, b))

elif selection == "4": 
     print(divide(a, b))

else: 
    print(f"Are you sure {a} and {b} are actually numbers AND {selection} is between 1 - 4?")
    #main()
