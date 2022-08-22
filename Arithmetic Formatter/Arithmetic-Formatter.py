def arithmetic_arranger(problem_list, solution=False):

    # returns an error if the user inputs more than 5 problems
    if len(problem_list) > 5:
        return "Error: Too many problems."

    # returns an error if the user inputs a non-numerical operand
    for problem in problem_list:
        problem = problem.split()
        try:
            problem[0] = int(problem[0])
            problem[2] = int(problem[2])
        except:
            return "Error: Numbers must only contain digits."

    solution_list = []
    upper_operands = []
    lower_operands = []
    operators = []

    # creating 3 lists: 1 for upper operands, 1 for lower operands and 1 for operators
    for problem in problem_list:
        problem = problem.split()
        upper_operands += [problem[0]]
        operators += [problem[1]]
        lower_operands += [problem[2]]

        # returning error if len of operand > 4
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # calculating solutions to problems
        else:
            if problem[1] == "+":
                y = int(problem[0]) + int(problem[2])
            elif problem[1] == "-":
                y = int(problem[0]) - int(problem[2])

            # returning error if an operator is not a + or -
            else:
                return "Error: Operator must be '+' or '-'."

            solution_list += [y]

    upper_str = str()
    lower_str = str()
    solution_str = str()
    dash_str = str()

    # creating dash string
    for z in range(0, len(problem_list)):
        dash_str = dash_str + str(
            (max(len(upper_operands[z]), len(lower_operands[z])) + 2) * "-" + 4 * " "
        )

    # converting dash string into dash list which will be used as a basis to format the strings of operands and solutions
    dash_list = list(dash_str.split())

    # creating formatted strings of upper and lower operands, as well as the solutions
    for a in range(0, len(problem_list)):
        solution_str = (
            solution_str
            + (len(dash_list[a]) - len(str(solution_list[a]))) * " "
            + str(solution_list[a])
            + 4 * " "
        )
        upper_str = (
            upper_str
            + (len(dash_list[a]) - len(upper_operands[a])) * " "
            + upper_operands[a]
            + 4 * " "
        )
        if len(upper_operands[a]) < len(lower_operands[a]):
            lower_str = lower_str + operators[a] + " " + lower_operands[a] + 4 * " "
        else:
            lower_str = (
                lower_str
                + operators[a]
                + (len(upper_operands[a]) - len(lower_operands[a]) + 1) * " "
                + lower_operands[a]
                + 4 * " "
            )

    # creating string of arranged problems
    if solution is True:
        arranged_problems = (
            upper_str.rstrip()
            + "\n"
            + lower_str.rstrip()
            + "\n"
            + dash_str.rstrip()
            + "\n"
            + solution_str.rstrip()
        )
    else:
        arranged_problems = (
            upper_str.rstrip() + "\n" + lower_str.rstrip() + "\n" + dash_str.rstrip()
        )

    return arranged_problems

