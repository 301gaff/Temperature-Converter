def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("(C) Convert from Celsius to Fahrenheit")
    print("(F) Convert from Fahrenheit to Celsius")

    choice = input("Enter your choice (C/F): ").strip().upper()

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")
main()
