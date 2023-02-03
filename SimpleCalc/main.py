# defining subroutines
# these first two subroutines include error handling which gives the user a chance to reinput their choice of operator or their choice of two numbers
def inputOperator(msg):
    while True:
        opin = input(msg)
        if opin not in ["+", "-", "*", "/"]:
            print("Operator is not in the given list. Please try again.")
            continue
        else:
            return opin
            break

def inputNumber(msg):
    while True:
        try:
            numin = float(input(msg))
        except ValueError:  # a ValueError will occur when the user has provided an input which is not a float value which the input has requested
            print("The provided input is not a number. Try again.")
            continue
        else:
            return numin
            break


def addNum(arg1, arg2):
    return arg1 + arg2

def subNum(arg1, arg2):
    return arg1 - arg2

def multNum(arg1, arg2):
    return arg1 * arg2

def divNum(arg1, arg2):
    return arg1 / arg2


# runs the subroutines inputOperator and inputNumber
operator = inputOperator("Would you like to add, subtract, multiply or divide? Use the characters: +, -, *, /\n")
num1 = inputNumber("Please enter your first number: \n")
num2 = inputNumber("Please enter your next number:\n")

# math operation code
if operator == "+":
    print(f'Your answer is: {addNum(num1, num2)}')
if operator == "-":
    print(f'Your answer is: {subNum(num1, num2)}')
if operator == "*":
    print(f'Your answer is: {multNum(num1, num2)}')
if operator == "/":
    print(f'Your answer is: {divNum(num1, num2)}')
