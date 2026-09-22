def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperature: {fahrenheit}°F")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Tempedef celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperature: {fahrenheit}°F")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Temperature: {celsius}°C")


print("TEMPERATURE CONVERTER")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice: ")

if choice == "1":
    celsius_to_fahrenheit()

elif choice == "2":
    fahrenheit_to_celsius()

else:
    print("Invalid choice!")rature: {celsius}°C")


print("TEMPERATURE CONVERTER")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice: ")

if choice == "1":
    celsius_to_fahrenheit()

elif choice == "2":
    fahrenheit_to_celsius()

else:
    print("Invalid choice!")