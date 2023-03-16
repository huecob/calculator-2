"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:

   #len(answer) >= 2 and answer[0] == "square" and answer[0] == "cube":
    user_answer = input("> ")
    answer = user_answer.split()
    
 
# tokens = input_string.split(' ')   # => ['pow', '3', '5']
    if answer[0] == "+" and answer[1].isnumeric() and answer[2].isnumeric():
        total = add(float(answer[1]), float(answer[2]))
        print(total)
    
    elif answer[0] == "-" and answer[1].isnumeric() and answer[2].isnumeric():
        total = subtract(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "*" and answer[1].isnumeric() and answer[2].isnumeric():
        total = multiply(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "/" and answer[1].isnumeric() and answer[2].isnumeric():
        total = divide(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "square" and answer[1].isnumeric():
        total = square(float(answer[1]))       
        print(total)

    elif answer[0] == "cube" and answer[1].isnumeric():
        total = cube(float(answer[1]))       
        print(total)

    elif answer[0] == "pow" and answer[1].isnumeric() and answer[2].isnumeric():
        total = power(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "mod" and answer[1].isnumeric() and answer[2].isnumeric():
        total = mod(float(answer[1]), float(answer[2]))       
        print(total)

    else:
        print("Please enter a valid response!")


# Replace this with your code
