#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 1, 2022
# This program asks the if they want to calculate the
# area of a trapezoid or the volume of a trapezoidal prism
# The program will then display the measurement to the user and
# display all the calculations they have done.
# This program can be ran multiple times (at user's request)


# This function calculates and returns the area of a trapezoid and adds units to it
def calculate_area_trapezoid(base1, base2, height, units):
    # Calculates the area
    area = round((base1 + base2) / 2 * height, 2)

    # Adds units to the area in string form
    area_string = str(area) + f"{units}^2"

    # Returns the area with units to main() as string
    return area_string


# This function calculates and returns the volume of a trapezoid and adds units to it
def calculate_volume_trapezoid(base1, base2, height, width, units):
    # Calculates the volume
    volume = round((base1 + base2) / 2 * height * width, 2)

    # Adds units to the volume in string form
    volume_string = str(volume) + f"{units}^3"

    # Returns the volume with units to main() as string
    return volume_string


def main():
    # Initialized Variables
    user_repeat = True
    dimensions_of_trapezoid = ""
    run_again = ""

    # List of the past calculations that the user have done in the life of the program
    past_calculations = []

    # List to check if the user wants to calculator for a 2D or 3D Trapezoid
    volume_or_area = ["2", "3"]

    # List for possible answers to repeat the program
    yes_or_no_repeat = ["y", "n"]

    # Repeats the program until otherwise told by user
    while user_repeat:
        # Resets run again variable
        run_again = ""

        # Displays to user if they want to calculate for a 2D or 3D trapezoid
        print("Is your trapezoid 2D or 3D?")

        # Resets the user input for number of dimensions (2D or 3D)
        dimensions_of_trapezoid = ""

        # Ensures that the user will input a valid input for what trapezoid they want
        while dimensions_of_trapezoid not in volume_or_area:
            # Asks user if their trapezoid is 2D or 3D
            dimensions_of_trapezoid = input(
                "Enter (2 for a regular trapezoid or 3 for a trapezoidal prism): "
            )

        # Checks for exceptions
        try:
            # Asks user for the first base
            user_base1 = float(input("\nEnter the value for the first base: "))

            # Asks user for the second base
            user_base2 = float(input("Enter the value for the second base: "))

            # Asks user for the height measurement
            user_height = float(input("Enter the height value: "))

            # IF the user wants to calculate for a 3D trapezoid
            if dimensions_of_trapezoid == "3":
                # Asks user for the width of the trapezoidal prism
                user_prism_width = float(
                    input("Enter the width of the trapezoidal prism: ")
                )

                # IF they did not input a positive number
                if user_prism_width <= 0:
                    print("You must enter positive numbers!\n")
                    continue

            # Checks if any of the measurements are negative
            if user_base1 <= 0 or user_base2 <= 0 or user_height <= 0:
                print("You must enter positive numbers!\n")

            # IF the user entered valid numbers
            else:
                # Asks user for the unit of measurements
                print("\nPlease try to input valid metric units.")
                unit_of_measurement = input(
                    "Enter the unit of measurement (ex. mm, cm, m, km): "
                ).lower()

                # FOR 2D trapezoids
                if dimensions_of_trapezoid == "2":
                    # Calls function to calculate the area of the trapezoid
                    trapezoid_area = calculate_area_trapezoid(
                        user_base1, user_base2, user_height, unit_of_measurement
                    )

                    # Adds the area to a list (to store past calculations)
                    past_calculations.append(trapezoid_area)

                    # Displays the area to the user
                    print(f"\nThe area of your trapezoid: {trapezoid_area}\n")

                # FOR 3D Trapezoidal Prism
                else:
                    # Calls function to calculate the volume of the trapezoidal prism
                    trapezoidal_prism_volume = calculate_volume_trapezoid(
                        user_base1,
                        user_base2,
                        user_height,
                        user_prism_width,
                        unit_of_measurement,
                    )

                    # Adds the volume to a list (to store past calculations)
                    past_calculations.append(trapezoidal_prism_volume)

                    # Displays the volume to the user
                    print(
                        f"\nThe volume of your trapezoidal prism: {trapezoidal_prism_volume}\n"
                    )

                # Asks user if they want to run the program again
                while run_again not in yes_or_no_repeat:
                    run_again = input(
                        "Do you want to run the program again (y/n): "
                    ).lower()

                # Displays all of the calculations the user has done
                print(
                    f"\nHere is a list of all of the past calculations of the trapezoid shapes done (Some people like keep track of these): \n {past_calculations}\n"
                )

                # IF the user wants to end the program
                if run_again == "n":
                    # Ends the program/loop
                    user_repeat = False

        # In the event of an exception
        except Exception:
            print("You must enter positive numbers! (Invalid Input, try again.)\n")


if __name__ == "__main__":
    main()
