# MathSimplicity

## Description

[MathSimplicity](mathsimplicity/mathsimplicity.py) is a Python package that provides various utilities for mathematical computations, including:

- Arithmetic operations.
- Prime factorization of numbers.
- Generation of prime numbers within a specified range.
- Conversion of fractions to decimals and vice versa.
- Calculation of Greatest Common Divisor (GCD) and Least Common Multiple (LCM).

## Why mathsimplicity?
The main motivation behind [mathsimplicity](mathsimplicity/mathsimplicity.py) is to provide an accessible tool for those who are taking their first steps in programming and mathematics. By offering intuitive and easy-to-use tools, my goal is to support students and enthusiasts on their way to understanding and applying basic mathematical concepts. This project aims to simplify learning and facilitate the process of solving everyday mathematical problems.

### Key Features
- Ease of Use: Functions designed to be simple and straightforward.
- Support for New Programmers: Clear documentation and practical examples to facilitate learning.
- Essential Mathematical Functions: Fundamental tools for solving common mathematical problems.

## 📢 Behind the Project

🔹 From Hello World to [![PyPI Downloads](https://static.pepy.tech/badge/mathsimplicity)](https://pepy.tech/projects/mathsimplicity) downloads on PyPI 🔹  
I shared the full story of how this library came to life in a personal post. If you're curious about the journey and motivation behind mathsimplicity, feel free to check it out:

👉 [Read the story on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7356304493904371712/)

📊 Live stats: [mathsimplicity on pepy.tech](https://pepy.tech/projects/mathsimplicity)

## Installation

You can install [`mathsimplicity`](mathsimplicity/mathsimplicity.py) via PyPI using pip. Simply run the following command:

```
pip install mathsimplicity
```

## Usage
Here's a quick overview of how to use the functionalities provided by the package.
### Arithmetic Operation
```
from mathsimplicity import arithmetic_operations

result1 = arithmetic_operations(["7+9", "7-9", "9/6", "9÷6", "8*9", "8x9"])
result2 = arithmetic_operations(["7+9", "7-9", "9/6", "9÷6", "8*9", "8x9"], True)

print(result1)
print(result2)
```
#### OUTPUT
```
   7       7       9       9       8       8
+  9    -  9    ÷  6    ÷  6    x  9    x  9
----    ----    ----    ----    ----    ----
THE RESULTS ARE HIDDEN. TO SHOW THEM, PLEASE INPUT 'True' AS THE SECOND ARGUMENT.
   7       7       9       9       8       8
+  9    -  9    ÷  6    ÷  6    x  9    x  9
----    ----    ----    ----    ----    ----
  16      -2     1.5     1.5      72      72
```

### Prime Factorization
```
from mathsimplicity import primes

result = primes(30, 56)
print(result)
```
#### OUTPUT
```
The number 30 can be divided by the following prime numbers: 2 x 3 x 5
The number 56 can be divided by the following prime numbers: 2^3 x 7
```

### Prime Numbers in Range
```
from mathsimplicity import primes_in_range

result = primes_in_range(10, 50)
print(result)

```
#### OUTPUT
```
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Fraction to Decimal Conversion
```
from mathsimplicity import fraction_to_decimal

result = fraction_to_decimal("1/2", "3/4", "5 ÷ 10")
print(result)
```
#### OUTPUT
```
The result of '1/2' is 0.5
The result of '3/4' is 0.75
The result of '5 ÷ 10' is 0.5
```

### Decimal to Fraction Conversion
```
from mathsimplicity import decimal_to_fraction

result = decimal_to_fraction("0.25", "0.5", "0.75")
print(result)
```
#### OUTPUT
```
The decimal '0.25' is approximately '1/4' as a fraction.
The decimal '0.5' is approximately '1/2' as a fraction.
The decimal '0.75' is approximately '3/4' as a fraction.
```

### Greatest Common Divisor (GCD)
```
from mathsimplicity import greatest_common_divisor

result = greatest_common_divisor(54, 24, 18)
print(result)
```
#### OUTPUT
- ```The greatest common divisor of the provided numbers is: 6```

### Least Common Multiple (LCM)
```
from mathsimplicity import least_common_multiple

result = least_common_multiple(4, 5, 6)
print(result)
```
#### OUTPUT
- ```The least common multiple of the provided numbers is: 60```

## Contributing
Contributions are not welcome!

## LICENSE
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
If you have any questions or feedback, feel free to contact me:

- Email: mohamedhireche74@gmail.com
- GitHub: promoha90
