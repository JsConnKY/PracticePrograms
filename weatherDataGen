# Practice project from CH 7: DICTIONARIES AND STRUCTURING DATA,
# "Automate the Boring Stuff Workbook" by Al Swigert
# Program by Jessie Conn
# Generates 100 random weather data dictionaries and stores them in a list.
# Then calculates and prints the average temperature from that list.

import random


# Function to generate one weather dictionary
def get_random_weather_data():
    temp = random.uniform(-50, 50)

    weather = {
        "temp": temp,
        "feels_like": random.uniform(temp - 10, temp + 10),
        "humidity": random.randint(0, 100),
        "pressure": random.randint(990, 1010)
    }

    return weather


# Function to calculate average temperature
def get_average_temperature(weather_data):
    total = 0

    for entry in weather_data:
        total += entry["temp"]

    average = total / len(weather_data)
    return average


# Main program
def main():
    weather_list = []

    # Generate 100 weather dictionaries
    for i in range(100):
        weather_list.append(get_random_weather_data())

    # Print the list
    print("Weather Data:\n")
    print(weather_list)

    # Calculate and print average temperature
    avg_temp = get_average_temperature(weather_list)
    print("\nAverage Temperature:", avg_temp)


# Run the program
if __name__ == "__main__":
    main()
