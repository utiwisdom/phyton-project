def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes = []
    solutions = []

    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # Check if the operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if operands are more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the solution if show_answers is True
        if operator == "+":
            solution = str(int(operand1) + int(operand2))
        else:
            solution = str(int(operand1) - int(operand2))

        # Determine the width of the problem
        width = max(len(operand1), len(operand2)) + 2

        # Build the parts for the arranged problems
        first_line.append(operand1.rjust(width))
        second_line.append(operator + " " + operand2.rjust(width - 2))
        dashes.append("-" * width)
        solutions.append(solution.rjust(width))

    # Combine all parts into formatted strings with four spaces between problems
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes)
    )

    # Add solutions if show_answers is True
    if show_answers:
        arranged_problems += "\n" + "    ".join(solutions)

    return arranged_problems


# Test cases
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
