print("PLEASE ENTER FIVE NUMBERS")
def value_checker (input):
    try:
        inputs_user = int(input)
        return inputs_user
    except ValueError:
        try:
            inputs_user = float(input)
            return inputs_user
        except ValueError:
            print("This is not a number.")
num1 = input('First: ')
num2 = input('Second: ')
num3 = input('Third: ')
num4 = input('Fourth: ')
num5 = input('Fifth: ')
value_checker(num1)
value_checker(num2)
value_checker(num3)
value_checker(num4)
value_checker(num5)

new_list =  [value_checker(num1), value_checker(num2), value_checker(num3), value_checker(num4), value_checker(num5)]
float_only = [digit for digit in new_list if (type(digit)is float)]
print(float_only)