from collections import Counter
from fractions import Fraction
from functools import reduce
from numexpr import evaluate
from re import fullmatch, match as matching
import math

def main():
    pass


def arithmetic_operations(problems, show_answers=False):
    # Verify if the problems are a list of strings
    if not isinstance(problems, list) or not all(isinstance(problem, str) for problem in problems):
        return "Error: The problems must be a list of strings -> List[str]."

    # Initialize lists to hold the components of each problem
    first_numbers = []
    operators = []
    second_numbers = []

    # Regex pattern to match problems with or without spaces
    pattern = r'(\d+)\s*([+\-*x/÷])\s*(\d+)'
    problem_counter = 0
    # Parse and validate each problem
    for problem in problems:
        # Validate the operator
        if '+' not in problem and '-' not in problem and 'x' not in problem and '*' not in problem and '/' not in problem and '÷' not in problem:
            return "Error: Operator must be '+', '-', ('x' '*'), or ('÷' '/')."
        
        problem_counter += 1
        problem = problem.strip()        
        match = matching(pattern, problem.replace('*', 'x').replace('/', '÷'))
        
        if not match:
            return "Error: Each problem must be a string in the format 'number operator number'."

        first, operator, second = match.groups()
        first_numbers.append(first)
        operators.append(operator)
        second_numbers.append(second)

        # Validate that both operands are numeric
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

    # Prepare strings to hold each line of the arranged problems
    first_line = ''
    second_line = ''
    dashes = ''
    results = ''
    spacing = ' ' * 4  # Standard spacing between problems

    # Format each problem and assemble the lines
    for i in range(len(problems)):
        # Determine the width needed for each problem based on the longest number
        max_length = max(len(first_numbers[i]), len(second_numbers[i]))
        width = max_length + 3  # Additional space for the operator and a leading space

        # Perform the arithmetic operation
        if operators[i] == '+':
            result = int(first_numbers[i]) + int(second_numbers[i])
        elif operators[i] == '-':
            result = int(first_numbers[i]) - int(second_numbers[i])
        elif operators[i] == 'x':
            result = int(first_numbers[i]) * int(second_numbers[i])
        else:  # operators[i] == '÷'
            try:
                # Perform float division
                result = float(first_numbers[i]) / float(second_numbers[i])
                # Convert to int if there are no decimal places
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, width)
            except ZeroDivisionError:
                return 'Ǝ'

        result_str = str(result).rjust(width)

        # Build the formatted lines
        first_line += first_numbers[i].rjust(width)
        second_line += operators[i] + second_numbers[i].rjust(width - 1)
        dashes += '-' * width
        results += result_str

        # Add spacing between problems if it's not the last one
        if i < len(problems) - 1:
            first_line += spacing
            second_line += spacing
            dashes += spacing
            results += spacing
    if problem_counter == 0:
        return "List must cotain more than zero arguments!"
    # Return the arranged problems with or without the results based on show_answers
    if show_answers:
        return f"{first_line}\n{second_line}\n{dashes}\n{results}"
    
    return f"{first_line}\n{second_line}\n{dashes}\nTHE RESULTS ARE HIDDEN. TO SHOW THEM, PLEASE INPUT 'True' AS THE SECOND ARGUMENT."

# Example usage:
# print(mathsimplicity.arithmetic_arranger(["32+698", "3801-2", "45*43", "45 x 43" "123/49", "123 ÷ 49", ...], True))


def primes(*args):
    if argument_count(*args) == 0:
        return "Please enter at least one number to calculate its prime numbers"
    
    def validate_arguments(args):
        """Validate the input arguments and return a list of valid numbers and error messages."""
        numbers = []
        messages = []
        for argument in args:
            try:
                number = int(argument)
                if number <= 1:
                    messages.append(f"The value '{argument}' must be greater than 1!")
                else:
                    numbers.append(number)
            except Exception as e:
                messages.append(f"The value '{argument}' is not a valid positive integer. Please introduce only positive integer values.")
        return numbers, messages

    def prime_calculation(*args):
        """Calculate the prime factors of the given numbers."""
        # Validate the input arguments
        numbers, messages = validate_arguments(args)

        # List containing the first 100 prime numbers
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
            163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
            251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
            349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
            443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541
        ]

        results = {}
        for number in numbers:
            original_number = number
            divisible_primes = []
            
            # Calculate the prime factors of the number
            for prime in primes:
                while number % prime == 0 and number > 1:
                    divisible_primes.append(prime)
                    number //= prime
            
            # Count the frequency of each prime factor
            prime_counts = Counter(divisible_primes)
            if divisible_primes and number == 1:
                # Create the representation in product format
                product_representation = ' x '.join(f"{prime}^{count}" if count > 1 else f"{prime}" for prime, count in sorted(prime_counts.items()))
                result_message = f"The number {original_number} can be divided by the following prime numbers: {product_representation}"
            else:
                result_message = f"The number {original_number} cannot be completely divided by the first 100 prime numbers."

            # Store the result message
            results[original_number] = result_message

        # If there are no validation messages, use the results
        if not messages:
            messages = list(results.values())
        else:
            # Include the results with the error messages if there are validation issues
            messages.extend(results.values())
        
        return "\n".join(messages)

    return prime_calculation(*args)

# Example usage:
# print(primes(12, 18, ...))


def primes_in_range(start, end):
    """Generate a list of prime numbers in the range [start, end] using the Sieve of Eratosthenes."""
    if start > end or start < 0:
        return "Invalid range. Please provide a valid range with start <= end and start >= 0."

    if end < 2:
        return []  # No primes below 2
    
    # Create a boolean array "sieve" and initialize all entries as True
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    
    # Implement the Sieve of Eratosthenes
    for num in range(2, int(end**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False
    
    # Collect all prime numbers in the range [start, end]
    return [num for num in range(start, end + 1) if sieve[num]]

# Example usage:
# print(primes_in_range(2, 90))


def fraction_to_decimal(*args):
    if len(args) == 0:
        return "Please enter at least one number to fractionate"
    
    # Verifica que todos los argumentos sean cadenas de texto
    if not all(isinstance(arg, str) for arg in args):
        return "Error: All inputs must be strings."

    def is_valid_expression(expression):
        """Check if the input expression contains only valid characters for a fraction."""
        return bool(fullmatch(r'[0-9\s÷/()+\-]*', expression)) and any(char in expression for char in ['/', '÷'])

    """Validate and process input expressions to compute their results."""
    results = []
    
    for argument in args:
        # Validate the input
        if not is_valid_expression(argument):
            results.append(f"Invalid fraction or expression: '{argument}'")
            continue
        
        # Replace non-standard division symbols
        expression = argument.replace('÷', '/')
        
        try:
            # Evaluate the expression safely and round the result
            result = round(evaluate(expression).item(), len(expression))
            results.append(f"The result of '{argument}' is {result}")
        except Exception as e:
            results.append(f"Error evaluating '{argument}': {e}")
    
    return "\n".join(results)

# Example usage:
# print(fraction_to_decimal("2÷8", "3/9", ...))


def decimal_to_fraction(*args):
    if len(args) == 0:
        return "Please enter at least one number to convert to a fraction"
    
    # Verifica que todos los argumentos sean cadenas de texto
    if not all(isinstance(arg, str) for arg in args):
        return "Error: All inputs must be strings."

    messages = []
    for argument in args:
        try:
            # Convert the argument to a float
            number = float(argument)
            
            # Convert the float to a fraction
            fraction = Fraction(number).limit_denominator()
            
            # Append the result message
            messages.append(f"The decimal '{number}' is approximately '{fraction}' as a fraction.")
        except ValueError:
            # Handle invalid inputs
            messages.append(f"The value '{argument}' is not a valid decimal number. Please introduce only valid decimal values.")
        
    return "\n".join(messages)

# Example usage:
# print(decimal_to_fraction(0.25, 0.3333, ...))


def greatest_common_divisor(*args):
    """Calculate the Greatest Common Divisor (GCD) of multiple numbers."""
    if not args:
        return "Please provide at least one number."

    # Validate that all numbers are integers or floats equivalent to integers
    if not validate_integers(*args):
        return "Invalid input. Please provide only integers or floats equivalent to integers."

    # Convert all float arguments that are equivalent to integers to int
    integers = [int(arg) for arg in args]

    def gcd(a, b):
        """Calculate the GCD of two numbers."""
        return math.gcd(a, b)

    try:
        # Reduce the list of integers using the gcd function
        result = reduce(gcd, integers)
        return f"The greatest common divisor of the provided numbers is: {result}"
    except TypeError:
        return "Invalid input. Please provide only integers."

def least_common_multiple(*args):
    """Calculate the Least Common Multiple (LCM) of multiple numbers."""
    if not args:
        return "Please provide at least one number."

    # Validate that all numbers are integers or floats equivalent to integers
    if not validate_integers(*args):
        return "Invalid input. Please provide only integers or floats equivalent to integers."

    # Convert all float arguments that are equivalent to integers to int
    integers = [int(arg) for arg in args]

    def lcm(a, b):
        """Calculate the LCM of two numbers."""
        return abs(a * b) // math.gcd(a, b)

    try:
        # Reduce the list of integers using the lcm function
        result = reduce(lcm, integers)
        return f"The least common multiple of the provided numbers is: {result}"
    except TypeError:
        return "Invalid input. Please provide only integers."

# Example usage:
# print(greatest_common_divisor(40, 89, ...))
# print(least_common_multiple(12, 15.0, ...))


def argument_count(*args):
    return len(args)

def validate_integers(*args):
    """Validate that all arguments are integers or floats equivalent to integers."""
    for arg in args:
        if not isinstance(arg, (int, float)) or not arg.is_integer():
            return False
    return True

if __name__ == "__main__":
    main()