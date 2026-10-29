import math
import operator
import statistics

def factorial(x):
    if x > 180:
        raise OverflowError
    if x.is_integer():
        return(math.factorial(int(x)))
    else:
        raise ValueError()
    
stats = {
    'statmean':statistics.mean,
    'statmedian':statistics.median,
    'statmode':statistics.mode,
    'statrange':lambda x: max(x)-min(x),
}

operations = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    "^":operator.pow,
    '/^':lambda a,b: operator.pow(a, 1/b),
    '%':operator.mod,
    'log':math.log,
}
singOperations = {
    'sin':math.sin,
    'asin':math.asin,
    'cos':math.cos,
    'acos':math.acos,
    'tan':math.tan,
    'atan':math.atan,
    'csc':lambda x: 1/math.sin(x),
    'acsc':lambda x: math.asin(1/x),
    'sec':lambda x: 1/math.cos(x),
    'asec':lambda x: math.acos(1/x),
    'cot':lambda x: 1/math.tan(x),
    'acot':lambda x: math.pi/2 -math.atan(x),
    'ln':math.log,
    '!':factorial,
    'sqrt':math.sqrt
}
trig = ['sin','cos','tan','csc','sec','cot']
iTrig = ['asin','acos','atan','acsc','asec','acot']
constants = {
    'pi':math.pi,
    'e':math.e,
    'tau':math.tau,
}

class BadInput(Exception):
    pass
class BadAnswer(Exception):
    pass
def replace(value, ans):
    if value is None:
        raise BadInput('An input is missing')
    value = value.strip().lower()
    if "nan" in value:
        raise BadInput(f"'{value}' is not a number")
    if value == 'ans':
        if ans is None: 
            raise BadInput('No answer found')
        return float(ans)
    if value in constants:
        return constants[value]
    try:
        return float(value)
    except ValueError:
        raise BadInput(f"'{value}' is not a number") from None

def calculate(d1, op, d2, ans, degrees, roundTo):
    d1 = replace(d1, ans)
    if op in singOperations:
        if d2 is not None:
            raise BadInput('Too many values given for this operation')
        if degrees and op in trig:
            d1 = math.radians(d1) 
        value = float(singOperations[op](d1))
        if degrees and op in iTrig:
            value = math.degrees(value)
        realVal = round(value, roundTo)+0.0
    elif op in operations:
        d2 = replace(d2, ans)
        realVal = round(float(operations[op](d1,d2)), roundTo)+0.0
    else:
        raise BadInput(f"{op} is not a valid operator")
    if math.isnan(realVal):
        raise BadAnswer('Not a real answer found')
    return(realVal)

def start():
    ans = None
    degrees = False
    history = []
    roundTo = 5
    while True:
        solving = input('Input expression or command (Include spaces and if using a unary operation, have the operation come second):')
        if solving[0] is None:
            print('No input found')
            continue
        if solving[0].strip().lower() in stats:
            try:
                data = [replace(i, ans) for i in solving[1:]]
                result = stats[solving[0].strip().lower()](data)
                print(f"{solving[0]} of {data}: {result}")
            except ValueError:
                print('Data is not valid')
            except BadInput as e:
                print(e)
            continue
        elif len(solving) == 3:
            d1 = solving[0]
            op = solving[1].lower()
            d2 = solving[2]
        elif len(solving) == 2:
            if solving[0].strip().lower() == 'roundto':
                try: 
                    roundTo = int(solving[1])
                    print(f"Rounding to {roundTo}")
                except ValueError:
                    print('Input is not an integer')
                continue
            else:
                d1 = solving[0]
                op = solving[1].lower()
                d2 = None
        elif len(solving) == 1:
            command = solving[0].lower()
            if command == 'history':
                if not history:
                    print('History not found')
                else:
                    for entry in history:
                        print(entry)
            elif command == 'mode':
                degrees = not degrees
                print(f'Degrees active: {degrees}')
            elif command == 'quit':
                break
            else: 
                print('Not a valid command')
            continue
        else:
            print('Expression is of wrong length')
            continue
        try:
            result = calculate(d1, op, d2, ans, degrees, roundTo)
            expr = f"{d1} {op}" if op in singOperations else f"{d1} {op} {d2}"
        except TypeError:
            print("Answer too complex")
        except ValueError:
            print("Domain is invalid")
        except ZeroDivisionError:
            print("Zero cannot be used here")
        except OverflowError:
            print("Answer too large")
        except (BadInput, BadAnswer) as e:
            print(e)
        else:
            history.append(f"{expr} = {result}")
            ans = result
            print(f"Answer: {ans}")



if __name__ == "__main__": start()