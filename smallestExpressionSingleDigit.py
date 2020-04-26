# to restrict the maximum number of times the 'D' can be used to obtain N
LIMIT = 10
minimum = LIMIT

# to store the value of intermediate D
# and the D of operands used to get that intermediate D, ie
# seen[intermediateNumber] = numberOfOperandsUsed
seen = {}

# stack to store the operators used to print the expression
operators = []


# function to obtain minimum D of operands in recursive tree
def minNumberOfOperands(total, N, D, numberOfOperands):
    global minimum

    # if total is equal to given N
    if total == N:
        # store if D of operands is minimum
        minimum = min(minimum, numberOfOperands)
        return

    # if the last level (limit) is reached
    if numberOfOperands == minimum:
        return

    # if total can be divided by D, recurse by dividing the total by D
    if total % D == 0:
        minNumberOfOperands(total / D, N, D, numberOfOperands + 1)

    # recurse for total + D
    minNumberOfOperands(total + D, N, D, numberOfOperands + 1)

    # if total - D is greater than 0, recurse for total - D
    if total - D > 0:
        minNumberOfOperands(total - D, N, D, numberOfOperands + 1)

    # recurse for total * D
    minNumberOfOperands(total * D, N, D, numberOfOperands + 1)


# function to generate the minimum expression
def generate(total, N, D, numberOfOperands):
    
    # if total is equal to N
    if total == N:
        return True

    # if the last level is reached
    if numberOfOperands == minimum:
        return False

    # if the total is not already seen or if the total is seen with more numberOfOperands
    # then mark total as seen with current numberOfOperands
    if seen.get(total) is None or seen.get(total) >= numberOfOperands:
        seen[total] = numberOfOperands

        divide = -1
        # if total is divisible by D
        if total % D == 0:
            divide = total / D
            # if the number (divide) is not seen, mark as seen
            if seen.get(divide) is None:
                seen[divide] = numberOfOperands + 1

        addition = total + D
        # if the number (addition) is not seen, mark as seen
        if seen.get(addition) is None:
            seen[addition] = numberOfOperands + 1

        subtraction = -1
        # if D can be subtracted from total
        if total - D > 0:
            subtraction = total - D
            # if the number (subtraction) is not seen, mark as seen
            if seen.get(subtraction) is None:
                seen[subtraction] = numberOfOperands + 1

        multiplication = total * D
        # if the number (multiplication) is not seen, mark as seen
        if seen.get(multiplication) is None:
            seen[multiplication] = numberOfOperands + 1

        # recurse by dividing the total if possible and store the operator
        if divide != -1 and generate(divide, N, D, numberOfOperands + 1):
            operators.append('/')
            return True

        # recurse by adding D to total and store the operator
        if generate(addition, N, D, numberOfOperands + 1):
            operators.append('+')
            return True

        # recurse by subtracting D from total if possible and store the operator
        if subtraction != -1 and generate(subtraction, N, D, numberOfOperands + 1):
            operators.append('-')
            return True

        # recurse by multiplying D by total and store the operator
        if generate(multiplication, N, D, numberOfOperands + 1):
            operators.append('*')
            return True

    # expression is not found yet
    return False


# function to print the expression
def printExpression(N, D):
    # find minimum number of operands
    minNumberOfOperands(D, N, D, 1)

    # generate expression if possible
    if generate(D, N, D, 1):
        expression = ''
        # if stack is not empty, concatenate D and operator popped from stack
        if len(operators) > 0:
            expression = str(D) + operators.pop()

        # until stack is empty, concatenate the operator popped with parenthesis for precedence
        while len(operators) > 0:
            popped = operators.pop()
            if popped == '/' or popped == '*':
                expression = '(' + expression + str(D) + ')' + popped
            else:
                expression = expression + str(D) + popped

        expression = expression + str(D)
        print("Expression: " + expression)

    # not possible within 10 digits.
    else:
        print("Expression not found!")


# Driver's code
if __name__ == '__main__':
    # N = 7, D = 4
    minimum = LIMIT
    printExpression(7, 4)

    minimum = LIMIT
    printExpression(100, 7)

    minimum = LIMIT
    printExpression(200, 9)
