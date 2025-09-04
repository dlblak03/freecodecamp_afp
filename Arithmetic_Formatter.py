def arithmetic_arranger(problems, show_answers=False):
    # Check for too many problems
    problemCount = len(problems)
    if problemCount > 5:
        return "Error: Too many problems."

    # Loop through problems
    top = ""
    bottom = ""
    line = ""
    answer = ""
    for index, problem in enumerate(problems):
        # Split the problem into components
        components = problem.split()
        if len(components) != 3:
            return "Error: Each problem must contain two operands and one operator."

        operand1, operator, operand2 = components

        # Check for valid operators
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check for numeric operands
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check for operand length
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the result if needed
        result = ""
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
        else:
            result = ""
        
        # Determine the width for formatting
        width = max(len(operand1), len(operand2)) + 2

        # Format each part of the problem
        top += operand1.rjust(width) + ('    ' if index < problemCount - 1 else '')
        bottom += operator + ' ' + operand2.rjust(width - 2) + ('    ' if index < problemCount - 1 else '')
        line += ('-' * width) + ('    ' if index < problemCount - 1 else '')
        answer += (result.rjust(width) + ('    ' if index < problemCount - 1 else '')) if show_answers else ''
    
    return top + '\n' + bottom + '\n' + line + ('\n' + answer if show_answers else '')

print(f'{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')