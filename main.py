# Function to generate Fibonacci Series
def fibonacci_generator(number):
    # Start the Fibonacci series with the first two numbers.
    fibonacci_list = [0, 1]

    # Add the last two numbers in the string to create the next number,
    # when -1 is the last number, and -2 is before the last number.
    while len(fibonacci_list) < number:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    # Returns the Fibonacci series in single-row vector form.
    return fibonacci_list[:number]


# Use Fibonacci generator function
number = int(input("Enter the number to generate Fibonacci Series = "))
fib = fibonacci_generator(number)

# Print Fibonacci Series
print(fib)
