def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operation_input():
    while True:
        op = input("Enter the operation (1.add, 2.subtract, 3.multiply, 4.divide): ")
        if op in ['1', '2', '3', '4']:
            return op
        else:
            print("Invalid operation! Please enter 1, 2, 3, or 4.")





first_num =get_float_input("Enter the first number: ")
operation = get_operation_input()
second_num = get_float_input("Enter the second number: ") 

symbols = {
    '1': '+',
    '2': '-',
    '3': '*',
    '4': '/'
}

if operation == '1':
    result = first_num + second_num
elif operation == '2':
    result = first_num - second_num
elif operation == '3':
    result = first_num * second_num
elif operation == '4':
    if second_num != 0:
        result = first_num / second_num
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operation."

if isinstance(result, (int, float)):
    print(f"The result of {first_num} {symbols[operation]} {second_num} is: {result}")
else:
    print(result)