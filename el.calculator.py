import math
import operator

operations = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    "^":operator.pow,
    '/^':lambda a,b: operator.pow(a, 1/b)
}
singOperations = {
    'sin':math.sin,
    'asin':math.asin,
    'cos':math.cos,
    'acos':math.acos,
    'tan':math.tan,
    'atan':math.atan,
    'ln':math.log,
}
irrationals = {
    'pi':math.pi,
    'e':math.e,
    'tau':math.tau,
}
def replace(value):
    value = value.strip().lower()
    return irrationals[value] if value in irrationals else float(value)
def calculate(d1,op,d2):
    d1 = replace(d1)
    if op in singOperations:
        return(f"The answer to the {op} of {d1} is {round(float(singOperations[op](d1)), 5)}")
    if op in operations:
        d2 = replace(d2)
        return(f"The answer to {d1} {op} {d2} is {round(float(operations[op](d1,d2)), 5)}")
    raise KeyError(op)
def start():
    print('If using trigonometric functions, only the first input will be used, inverse trig functions are done by including a at the start of the input (inverse sin = asin etc.)')
    d1 = input("Input digit 1: ")
    op = input("Input an operation: ")
    d2 = None if op in singOperations else input("Input digit 2")
    try:
        print(calculate(d1, op, d2))
    except KeyError:
        print(f"{op} is not a valid operator")
    except ValueError as e:
        print(f"{e} is not a valid input")
    except ZeroDivisionError:
        print("Zero is not divisible")
    except OverflowError:
        print("Answer too large")
start()
