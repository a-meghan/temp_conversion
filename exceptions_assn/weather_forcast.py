#TASK 1
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

try:
    temp = float(input("Please enter the temperature in Fahrenheit: "))
    celsius = convert_to_celsius(temp)
except ValueError:
    print("Invalid entry- please enter a valid number.")
else:
    print(f"{temp} dgrees fahrenheit is {celsius} celsius.")
finally:
    print("Thank you for using our temperature converter today!")
