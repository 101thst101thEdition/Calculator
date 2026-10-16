lazy import math
lazy import operator

operations = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    "^":operator.pow,
    '/^':operator.pow,
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

def calculate(d1,op,d2):
    if d1 in irrationals:
        d1 = irrationals[d1]
    if d2 in irrationals:
        d2 = irrationals[d2]
    try:
        d1 = float(d1)
        print("d1 attempted")
    except ValueError:
        print(f'Could not make sense of the value in digit 1, "{d1}", restarting calculator.')
        start()
    try:
        d2 = float(d2)
    except ValueError:
        print(f'Could not make sense of the value in digit 2, "{d2}",restarting calculator.')
        start()
    if op in ('sin','cos','tan','asin','acos','atan'):
        return(f"The answer to the {op} of {d1} is {round(float(operations[op](d1)), 5)}")
    elif op == '/^':
        return(f"The answer to {d1} /^ {d2} is {round(float(operations[op](d1,1/d2)}")
    elif op in operations:
        return(f"The answer to {d1} {op} {d2} is {round(float(operations[op](d1,d2)), 5)}")
    else:
        print(f"Could not make sense of the value for the operation, {op},restarting calculator.")
        start()
def start():
    print('If using trigonometric functions, only the first digit will be used, inverse trig functions are done by including arc at the start of the input (inverse sin = arcsin etc.)')
    print(calculate(input('Input Digit 1:'), 
                    input('Input an Operation:').lower(),
                    input('Input Digit 2:')))
    start()
start()
