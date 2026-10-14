
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Km to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "7":
            break
        elif choice in ["1", "2", "3", "4"]:
            a = float(input("First number: "))
            b = float(input("Second number: "))

            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                print("Result:", a / b if b != 0 else "Cannot divide by zero")

        elif choice == "5":
            km = float(input("Kilometers: "))
            print("Miles:", km * 0.621371)

        elif choice == "6":
            c = float(input("Celsius: "))
            print("Fahrenheit:", c * 9 / 5 + 32)
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid numbers")
