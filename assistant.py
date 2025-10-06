def calculator():
    x = float(input("What's X? "))
    y = float(input("What's Y? "))
    op = input("Enter operator (+, -, *, /): ")
   
    if op == "+":
        print("Result:", x + y)
    elif op == "-":
        print("Result:", x - y)
    elif op == "*":
        print("Result:", x * y)
    elif op == "/":
        if y != 0:
            print("Result:", x / y)
        else: 
            print("Can't divide by 0!")
    else:
        print("Invalid Operator")

    home_menu()  # go back to main menu


def text_reverse():
    sentence = input("Write a sentence: ")

    print(f"Characters (no spaces): {len(sentence.replace(' ', ''))}")
    print(f"Uppercase: {sentence.upper()}")
    print(f"Reversed: {sentence[::-1]}")

    string_menu()


def count_char():
    sentence = input("Write a sentence: ")
    sentence = sentence.replace(" ", "")
    print(f"Characters (no spaces): {len(sentence)}")

    string_menu()


def count_word():
    sentence = input("Write a sentence: ")
    print(f"Word count: {len(sentence.split())}")

    string_menu()


def age_ctg():
    age = int(input("Enter your age: "))

    if age < 13:
        print("You are a child.")
    elif 13 <= age <= 19:
        print("You are a teenager.")
    elif 20 <= age <= 64:
        print("You are an adult.")
    else:
        print("You are a senior.")

    home_menu()


def title_msg(title):
    print(f"""
    Meter to {title} Converter
    ---------------------------
    """)


def unit_converter():
    print("""
    Basic Unit Converter:
    ---------------------
    1. Type 1 for Meter --> Kilometer
    2. Type 2 for Meter --> Centimeter
    3. Type 3 for Meter --> Millimeter
    0. Back to Main Menu
    """)
    unit_choice = int(input("Select option: "))

    if unit_choice == 1:
        title_msg("Kilometer")
        a = int(input("Meters: "))
        print(f"{a} Meter = {a/1000} Kilometer")
        unit_converter()
    elif unit_choice == 2:
        title_msg("Centimeter")
        b = int(input("Meters: "))
        print(f"{b} Meter = {b*100} Centimeter")
        unit_converter()
    elif unit_choice == 3:
        title_msg("Millimeter")
        c = int(input("Meters: "))
        print(f"{c} Meter = {c*1000} Millimeter")
        unit_converter()
    elif unit_choice == 0:
        home_menu()
    else:
        print(f"--X-- Invalid input '{unit_choice}'")
        unit_converter()


def greet(name):
    print(f"Hi {name}, welcome to your personal assistant!")


def home_menu():
    print("""
    Basic Personal Assistant
    -------------------------
    1. Calculator
    2. String Tools
    3. Age Category Checker
    4. Unit Converter
    5. EXIT
    """)
    choice = int(input("Type your choice: "))

    if choice == 1:
        calculator()
    elif choice == 2:
        string_menu()
    elif choice == 3:
        age_ctg()
    elif choice == 4:
        unit_converter()
    elif choice == 5:
        print(f"Goodbye, {name}. See you later!")
    else:
        print("Invalid choice. Try again.")
        home_menu()


def string_menu():
    print("""
    Basic String Tools
    -------------------
    1. Reverse Text
    2. Count Characters
    3. Count Words
    0. Back to Main Menu
    """)
    str_choice = int(input("Type your choice: "))

    if str_choice == 1:
        text_reverse()
    elif str_choice == 2:
        count_char()
    elif str_choice == 3:
        count_word()
    elif str_choice == 0:
        home_menu()
    else:
        print("Invalid choice.")
        string_menu()


# ---------- Main Program ----------
name = input("Write your name: ")
greet(name)
home_menu()
