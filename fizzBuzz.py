# Classic FizzBuzz program with User Input Written by Jessie Conn

def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Input validation loop
while True:
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        if start > end:
            print("Start must be less than or equal to end. Try again.\n")
            continue

        break  # valid input, exit loop

    except ValueError:
        print("Invalid input. Please enter whole numbers only.\n")

# Run the program
fizzbuzz(start, end)
