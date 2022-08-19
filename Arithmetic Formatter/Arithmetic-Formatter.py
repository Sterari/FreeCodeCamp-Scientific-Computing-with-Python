def arithmetic_arranger(prob, soln=False):
    # returns an error if the user inputs more than 5 problems
    if len(prob) > 5:
        return "Error: Too many problems."

    # returns an error if the user inputs a non-numerical operand
    for x in prob:
        x = x.split()
        try:
            x[0] = int(x[0])
            x[2] = int(x[2])
        except:
            return "Error: Numbers must only contain digits."

    sollist = []
    operandUP = []
    operandDOWN = []
    operators = []

    # creating 3 lists: 1 for upper operands, 1 for lower operands and 1 for operators
    for x in prob:
        x = x.split()
        operandUP = operandUP + [x[0]]
        operators = operators + [x[1]]
        operandDOWN = operandDOWN + [x[2]]

        # returning error if len of operand > 4
        if len(x[0]) > 4 or len(x[2]) > 4:
            return "Error: Numbers cannot be more than four digits."


        # calculating solutions to problems
        else:
            if x[1] == '+':
                y = int(x[0]) + int(x[2])
            elif x[1] == '-':
                y = int(x[0]) - int(x[2])

            # returning error if an operator is not a + or -
            else:
                return "Error: Operator must be '+' or '-'."

            sollist = sollist + [y]

    UPstr = str()
    DOWNstr = str()
    solstr = str()
    dashstr = str()

    # creating dash string
    for z in range(0, len(prob)):
        dashstr = dashstr + str((max(len(operandUP[z]), len(operandDOWN[z])) + 2) * "-" + 4 * " ")

    # converting dash string into dash list which will be used as a basis to format the strings of operands and solutions
    dashlist = list(dashstr.split())

    # creating formatted strings of upper and lower operands, as well as the solutions
    for a in range(0, len(prob)):
        solstr = solstr + (len(dashlist[a]) - len(str(sollist[a]))) * " " + str(sollist[a]) + 4 * " "
        UPstr = UPstr + (len(dashlist[a]) - len(operandUP[a])) * " " + operandUP[a] + 4 * " "
        if len(operandUP[a]) < len(operandDOWN[a]):
            DOWNstr = DOWNstr + operators[a] + " " + operandDOWN[a] + 4 * " "
        else:
            DOWNstr = DOWNstr + operators[a] + (len(operandUP[a]) - len(operandDOWN[a]) + 1) * " " + operandDOWN[
                a] + 4 * " "

    # creating string of arranged problems
    if soln == True:
        arranged_problems = UPstr.rstrip() + '\n' + DOWNstr.rstrip() + "\n" + dashstr.rstrip() + "\n" + solstr.rstrip()
    else:
        arranged_problems = UPstr.rstrip() + "\n" + DOWNstr.rstrip() + "\n" + dashstr.rstrip()

    return arranged_problems