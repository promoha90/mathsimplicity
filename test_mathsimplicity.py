from mathsimplicity import arithmetic_operations, primes, fraction_to_decimal, decimal_to_fraction, primes_in_range, greatest_common_divisor, least_common_multiple

"""ARITHMETIC OPERATIONS CALCULATION"""

def test_arithmetic_valid_operations_with_result_showing():
    assert arithmetic_operations(['3 + 5', '10 - 2', '6 x 7', '8 ÷ 2'], True) == (
        "   3       10       6       8\n"
        "+  5    -   2    x  7    ÷  2\n"
        "----    -----    ----    ----\n"
        "   8        8      42       4"
    )

    assert arithmetic_operations(['   3 + 5   ', '10 - 2', '6 * 7', '8 / 2'], True) == (
        "   3       10       6       8\n"
        "+  5    -   2    x  7    ÷  2\n"
        "----    -----    ----    ----\n"
        "   8        8      42       4"
    )

def test_arithmetic_valid_operations_with_result_not_showing():
    assert arithmetic_operations(['3 + 5', '10 - 2', '6 x 7', '8 ÷ 2']) == (
        "   3       10       6       8\n"
        "+  5    -   2    x  7    ÷  2\n"
        "----    -----    ----    ----\n"
        "THE RESULTS ARE HIDDEN. TO SHOW THEM, PLEASE INPUT 'True' AS THE SECOND ARGUMENT."
    )

def test_arithmetic_invalid_operations_list_mistake():
    assert arithmetic_operations('3 + 5') == 'Error: The problems must be a list of strings -> List[str].'

def test_arithmetic_invalid_operations_operator_mistake():
    assert arithmetic_operations(['3 & 5']) == "Error: Operator must be '+', '-', ('x' '*'), or ('÷' '/')."
    assert arithmetic_operations(['3 ^ 5']) == "Error: Operator must be '+', '-', ('x' '*'), or ('÷' '/')."

def test_arithmetic_invalid_operations_number_mistake():
    assert arithmetic_operations(['3 + a']) == "Error: Each problem must be a string in the format 'number operator number'."

def test_arithmetic_invalid_operations_empty_list_mistake():
    assert arithmetic_operations([], True) == 'List must cotain more than zero arguments!'

def test_arithmetic_invalid_operations_zero_division_mistake():
    assert arithmetic_operations(['5 ÷ 0']) == 'Ǝ'


"""PRIMES CALCULATION"""

def test_primes_valid_cases():
    expected = (
        "The number 2 can be divided by the following prime numbers: 2\n"
        "The number 3 can be divided by the following prime numbers: 3\n"
        "The number 4 can be divided by the following prime numbers: 2^2\n"
        "The number 6 can be divided by the following prime numbers: 2 x 3\n"
        "The number 9 can be divided by the following prime numbers: 3^2\n"
        "The number 15 can be divided by the following prime numbers: 3 x 5"
    )
    assert primes(2, 3, 4, 6, 9, 15) == expected

def test_primes_invalid_input():
    expected = (
        "The value '-5' must be greater than 1!\n"
        "The value 'abc' is not a valid positive integer. Please introduce only positive integer values.\n"
        "The value '1' must be greater than 1!"
    )
    assert primes(-5, 'abc', 1) == expected

def test_primes_invalid_input_with_valid_input():
    expected = (
        "The value '-5' must be greater than 1!\n"
        "The value 'abc' is not a valid positive integer. Please introduce only positive integer values.\n"
        "The value '1' must be greater than 1!\n"
        "The number 2 can be divided by the following prime numbers: 2\n"
        "The number 3 can be divided by the following prime numbers: 3\n"
        "The number 4 can be divided by the following prime numbers: 2^2\n"
        "The number 6 can be divided by the following prime numbers: 2 x 3\n"
        "The number 9 can be divided by the following prime numbers: 3^2\n"
        "The number 15 can be divided by the following prime numbers: 3 x 5"
    )
    assert primes(-5, 'abc', 1, 2, 3, 4, 6, 9, 15) == expected

def test_primes_empty():
    assert primes() == "Please enter at least one number to calculate its prime numbers"

def test_primes_large_prime():
    assert primes(541) == "The number 541 can be divided by the following prime numbers: 541"


"""PRIMES IN RANGE"""

def test_valid_range():
    assert primes_in_range(10, 50) == [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert primes_in_range(1, 10) == [2, 3, 5, 7]
    assert primes_in_range(2, 2) == [2]

def test_empty_range():
    assert primes_in_range(20, 19) == "Invalid range. Please provide a valid range with start <= end and start >= 0."
    assert primes_in_range(1, 1) == []

def test_negative_start():
    assert primes_in_range(-10, 10) == "Invalid range. Please provide a valid range with start <= end and start >= 0."
    assert primes_in_range(-5, -1) == "Invalid range. Please provide a valid range with start <= end and start >= 0."

def test_no_primes():
    assert primes_in_range(14, 16) == []

def test_large_range():
    assert primes_in_range(1, 100) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
        59, 61, 67, 71, 73, 79, 83, 89, 97
    ]

def test_only_one_prime():
    assert primes_in_range(29, 29) == [29]
    assert primes_in_range(50, 53) == [53]

def test_no_primes_below_two():
    assert primes_in_range(0, 1) == []


"""FRACTIONS TO DECIMALS"""

def test_valid_fractions():
    result = fraction_to_decimal("1/2", "3 ÷ 2", "10/3", "-4/2", "4/-2")
    expected = (
        "The result of '1/2' is 0.5\n"
        "The result of '3 ÷ 2' is 1.5\n"
        "The result of '10/3' is 3.3333\n"
        "The result of '-4/2' is -2.0\n"
        "The result of '4/-2' is -2.0"
    )
    assert result == expected

def test_invalid_fractions():
    result = fraction_to_decimal("2 + 2", "10*", "abc")
    expected = (
        "Invalid fraction or expression: '2 + 2'\n"
        "Invalid fraction or expression: '10*'\n"
        "Invalid fraction or expression: 'abc'"
    )
    assert result == expected

def test_edge_cases():
    result = fraction_to_decimal("0/1", "1/1", "999/1", "1/999")
    expected = (
        "The result of '0/1' is 0.0\n"
        "The result of '1/1' is 1.0\n"
        "The result of '999/1' is 999.0\n"
        "The result of '1/999' is 0.001"
    )
    assert result == expected

def test_mixed_valid_and_invalid():
    result = fraction_to_decimal("1/2", "abc", "3 ÷ 2", "10/3", "invalid")
    expected = (
        "The result of '1/2' is 0.5\n"
        "Invalid fraction or expression: 'abc'\n"
        "The result of '3 ÷ 2' is 1.5\n"
        "The result of '10/3' is 3.3333\n"
        "Invalid fraction or expression: 'invalid'"
    )
    assert result == expected

def test_error_in_evaluation():
    assert fraction_to_decimal("1/0").startswith("Error evaluating '1/0':")

def test_empty_evaluation():
    assert fraction_to_decimal() == "Please enter at least one number to fractionate"


"""DECIMALS TO FRACTIONS"""

def test_decimal_to_fraction_valid_cases():
    assert decimal_to_fraction("0.75") == "The decimal '0.75' is approximately '3/4' as a fraction."
    assert decimal_to_fraction("2.5") == "The decimal '2.5' is approximately '5/2' as a fraction."
    assert decimal_to_fraction("-1.25") == "The decimal '-1.25' is approximately '-5/4' as a fraction."

def test_decimal_to_fraction_invalid_cases():
    assert decimal_to_fraction("abc") == "The value 'abc' is not a valid decimal number. Please introduce only valid decimal values."
    assert decimal_to_fraction("1.23abc") == "The value '1.23abc' is not a valid decimal number. Please introduce only valid decimal values."

def test_decimal_to_fraction_multiple_inputs():
    result = decimal_to_fraction("0.75", "2.5", "abc", "-1.25")
    expected = (
        "The decimal '0.75' is approximately '3/4' as a fraction.\n"
        "The decimal '2.5' is approximately '5/2' as a fraction.\n"
        "The value 'abc' is not a valid decimal number. Please introduce only valid decimal values.\n"
        "The decimal '-1.25' is approximately '-5/4' as a fraction."
    )
    assert result == expected

def test_decimal_to_fraction_no_input():
    assert decimal_to_fraction() == "Please enter at least one number to convert to a fraction"

def test_decimal_to_fraction_large_values():
    assert decimal_to_fraction("123456.789") == "The decimal '123456.789' is approximately '123456789/1000' as a fraction."

def test_decimal_to_fraction_edge_cases():
    assert decimal_to_fraction("0.0") == "The decimal '0.0' is approximately '0' as a fraction."
    assert decimal_to_fraction("1.0") == "The decimal '1.0' is approximately '1' as a fraction."
    assert decimal_to_fraction("0.333333333333") == "The decimal '0.333333333333' is approximately '1/3' as a fraction."


"""GREATEST COMMON DIVISOR (GCD) AND LEAST COMMON MULTIPLE (LCM)"""

def test_greatest_common_divisor_basic():
    assert greatest_common_divisor(54, 24) == "The greatest common divisor of the provided numbers is: 6"
    assert greatest_common_divisor(48, 180) == "The greatest common divisor of the provided numbers is: 12"
    assert greatest_common_divisor(7, 3) == "The greatest common divisor of the provided numbers is: 1"

def test_least_common_multiple_basic():
    assert least_common_multiple(4, 5) == "The least common multiple of the provided numbers is: 20"
    assert least_common_multiple(7, 3) == "The least common multiple of the provided numbers is: 21"
    assert least_common_multiple(6, 8) == "The least common multiple of the provided numbers is: 24"

def test_greatest_common_divisor_with_multiple_numbers():
    assert greatest_common_divisor(5, 10, 15) == "The greatest common divisor of the provided numbers is: 5"
    assert greatest_common_divisor(12, -36) == "The greatest common divisor of the provided numbers is: 12"

def test_least_common_multiple_with_multiple_numbers():
    assert least_common_multiple(5, 10, 15) == "The least common multiple of the provided numbers is: 30"

def test_greatest_common_divisor_with_zero():
    assert greatest_common_divisor(0, 5) == "The greatest common divisor of the provided numbers is: 5"

def test_least_common_multiple_with_zero():
    assert least_common_multiple(0, 5) == "The least common multiple of the provided numbers is: 0"
    assert least_common_multiple(9, 0) == "The least common multiple of the provided numbers is: 0"

def test_greatest_common_divisor_with_negatives():
    assert greatest_common_divisor(-54, 24) == "The greatest common divisor of the provided numbers is: 6"

def test_least_common_multiple_with_negatives():
    assert least_common_multiple(-4, 5) == "The least common multiple of the provided numbers is: 20"

def test_greatest_common_divisor_error_cases():
    assert greatest_common_divisor() == "Please provide at least one number."
    assert greatest_common_divisor("12", 36) == "Invalid input. Please provide only integers or floats equivalent to integers."

def test_least_common_multiple_error_cases():
    assert least_common_multiple() == "Please provide at least one number."
    assert least_common_multiple("4", 5) == "Invalid input. Please provide only integers or floats equivalent to integers."
