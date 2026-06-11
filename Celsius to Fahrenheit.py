def cel_to_fa(num):
    return (num*9/5)+32

celsius = float(input("Enter temperature in Celsius:90"))
fahrenheit = cel_to_fa(celsius)
print(f"Temperature in Fahrenheit: {fahrenheit}")