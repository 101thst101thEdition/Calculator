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
}

def calculate(d1,op,d2):
    if d1 == 'pi':
        d1 = math.pi
    if d2 == 'pi':
        d2 = math.pi
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
    elif op in operations:
        return(f"The answer to {d1} {op} {d2} is {round(float(operations[op](d1,d2)), 5)}")
    else:
        print(f"Could not make sense of the value for the operation, {op},restarting calculator.")
        start()
def start():
    print('If using trigonometric functions, only the first digit will be used, inverse trig functions are done by including arc at the start of the input (inverse sin = arcsin etc.)')
    print(calculate(input('Input Digit 1:'), 
                      input('Input an Operation (+,-,*,/,^,/^,sin,cos,tan):').lower(),
                      input('Input Digit 2:')))
    start()
start()