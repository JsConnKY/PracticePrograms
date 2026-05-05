# Program name: Coordinate Directions
# Programmer: Jessie Conn
# Description: Collects directional inputs and calculates final Cartesian coordinates.
# Written for practicing creating Lists while reading through "Automate the Boring Stuff Workbook",
# by Al Swigert

def get_end_coordinates(directions):
    x = 0
    y = 0

    for d in directions:
        if d == 'N':
            y += 1
        elif d == 'S':
            y -= 1
        elif d == 'E':
            x += 1
        elif d == 'W':
            x -= 1

    return [x, y]


def main():
    directions = []

    print("Enter directions (N, S, E, W). Press Enter to finish.\n")

    while True:
        user_input = input("Direction: ").strip().upper()

        if user_input == "":
            break
        elif user_input in ['N', 'S', 'E', 'W']:
            directions.append(user_input)
        else:
            print("Invalid input. Please enter N, S, E, or W.\n")

    result = get_end_coordinates(directions)

    print("\nFinal coordinates:", result)


# Run the program
main()
