"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



while True:
    user_answer = input("> ")
    answer = user_answer.split()
    print(answer)
 
# tokens = input_string.split(' ')   # => ['pow', '3', '5']
    if answer[0] == "+":
        total = add(float(answer[1]), float(answer[2]))
        print(total)
    
    elif answer[0] == "-":
        total = subtract(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "*":
        total = multiply(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "/":
        total = divide(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "square":
        total = square(float(answer[1]))       
        print(total)

    elif answer[0] == "cube":
        total = cube(float(answer[1]))       
        print(total)

    elif answer[0] == "pow":
        total = power(float(answer[1]), float(answer[2]))       
        print(total)

    elif answer[0] == "mod":
        total = mod(float(answer[1]), float(answer[2]))       
        print(total)


# Replace this with your code
