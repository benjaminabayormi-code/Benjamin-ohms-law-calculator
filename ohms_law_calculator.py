"""
CTE123 – Introduction to Computer Programming
Project: Ohm's Law and Electrical Power Calculator
FULL NAME: Fade Benjamin Olajide
"""

calculation_history = []


def get_positive_number(prompt):
    """Get a valid positive number from the user."""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def check_power_rating(power):
    """Warn the user if calculated power exceeds the component rating."""
    rating = get_positive_number(
        "Enter the component's maximum power rating in watts (W): "
    )

    if power > rating:
        print("WARNING: Calculated power exceeds the component rating!")
    else:
        print("Calculated power is within the entered component rating.")

    calculation_history.append(f"Power: {power:.2f} W")


def calculate_voltage():
    current = get_positive_number("Enter current in amperes (A): ")
    resistance = get_positive_number("Enter resistance in ohms: ")
    voltage = current * resistance
    power = voltage * current

    print(f"\nVoltage = {voltage:.2f} V")
    print(f"Power = {power:.2f} W")
    calculation_history.append(f"Voltage: {voltage:.2f} V")
    check_power_rating(power)


def calculate_current():
    voltage = get_positive_number("Enter voltage in volts (V): ")
    resistance = get_positive_number("Enter resistance in ohms: ")
    current = voltage / resistance
    power = voltage * current

    print(f"\nCurrent = {current:.2f} A")
    print(f"Power = {power:.2f} W")
    calculation_history.append(f"Current: {current:.2f} A")
    check_power_rating(power)


def calculate_resistance():
    voltage = get_positive_number("Enter voltage in volts (V): ")
    current = get_positive_number("Enter current in amperes (A): ")
    resistance = voltage / current
    power = voltage * current

    print(f"\nResistance = {resistance:.2f} ohms")
    print(f"Power = {power:.2f} W")
    calculation_history.append(f"Resistance: {resistance:.2f} ohms")
    check_power_rating(power)


def calculate_power():
    print("\nChoose a power formula:")
    print("1. P = V x I")
    print("2. P = I squared x R")
    print("3. P = V squared / R")
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        voltage = get_positive_number("Enter voltage in volts (V): ")
        current = get_positive_number("Enter current in amperes (A): ")
        power = voltage * current
    elif choice == "2":
        current = get_positive_number("Enter current in amperes (A): ")
        resistance = get_positive_number("Enter resistance in ohms: ")
        power = (current ** 2) * resistance
    elif choice == "3":
        voltage = get_positive_number("Enter voltage in volts (V): ")
        resistance = get_positive_number("Enter resistance in ohms: ")
        power = (voltage ** 2) / resistance
    else:
        print("Invalid choice. Select 1, 2, or 3.")
        return

    print(f"\nElectrical Power = {power:.2f} W")
    check_power_rating(power)


def show_history():
    if len(calculation_history) == 0:
        print("\nNo calculations have been performed yet.")
    else:
        print("\n--- CALCULATION HISTORY ---")
        for count, result in enumerate(calculation_history, start=1):
            print(f"{count}. {result}")


def main():
    while True:
        print("\n===== OHM'S LAW AND ELECTRICAL POWER CALCULATOR =====")
        print("1. Calculate Voltage")
        print("2. Calculate Current")
        print("3. Calculate Resistance")
        print("4. Calculate Electrical Power")
        print("5. View Calculation History")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            calculate_voltage()
        elif choice == "2":
            calculate_current()
        elif choice == "3":
            calculate_resistance()
        elif choice == "4":
            calculate_power()
        elif choice == "5":
            show_history()
        elif choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
