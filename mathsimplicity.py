from collections import Counter
from fractions import Fraction
from functools import reduce
from numexpr import evaluate
from re import fullmatch
import math

def main():
    pass


def primes(*args):
    if argument_count(*args) == 0:
        return "Please enter atleast one number to calculate its prime numbers"
    
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



def fraction_to_decimal(*args):
    if argument_count(*args) == 0:
        return "Please enter atleast one number to fractionate"
    
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


def decimal_to_fraction(*args):
    if len(args) == 0:
        return "Please enter at least one number to convert to a fraction"
    
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

def greatest_common_divisor(*args):
    """Calculate the Greatest Common Divisor (GCD) of multiple numbers."""
    if not args:
        return "Please provide at least one number."

    def gcd(a, b):
        return math.gcd(a, b)

    try:
        result = reduce(gcd, args)
        return f"The greatest common divisor of the provided numbers is: {result}"
    except TypeError:
        return "Invalid input. Please provide only integers."

def least_common_multiple(*args):
    """Calculate the Least Common Multiple (LCM) of multiple numbers."""
    if not args:
        return "Please provide at least one number."

    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    try:
        result = reduce(lcm, args)
        return f"The least common multiple of the provided numbers is: {result}"
    except TypeError:
        return "Invalid input. Please provide only integers."


def argument_count(*args):
    return len(args)
 

if __name__ == "__main__":
    main()