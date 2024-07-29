from datetime import datetime, timedelta


def generate_dates(start_date, end_date):
    """Generate a list of dates between start_date and end_date."""
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    return date_list


def prompt_weather_data(dates):
    """Prompt user to enter weather data for each date."""
    weather_data = []
    for date in dates:
        print(f"\nEnter weather data for {date.strftime('%Y-%m-%d')}:")
        max_temp = float(input("Maximum Temperature (°C): "))
        min_temp = float(input("Minimum Temperature (°C): "))
        humidity = float(input("Humidity (%): "))
        weather_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'max_temp': max_temp,
            'min_temp': min_temp,
            'humidity': humidity
        })
    return weather_data


def find_highest_lowest_temperatures(weather_data):
    """Find the highest and lowest temperatures recorded."""
    max_temps = [entry['max_temp'] for entry in weather_data]
    min_temps = [entry['min_temp'] for entry in weather_data]
    highest_temp = max(max_temps)
    lowest_temp = min(min_temps)
    return highest_temp, lowest_temp


def count_days_above_30(weather_data):
    """Determine the number of days with temperatures above 30°C."""
    count = sum(1 for entry in weather_data if entry['max_temp'] > 30)
    return count


def compute_average_humidity(weather_data):
    """Compute the average humidity over the specified period."""
    total_humidity = sum(entry['humidity'] for entry in weather_data)
    average_humidity = total_humidity / len(weather_data)
    return average_humidity


def main():
    print("Weather Data Analysis for New York City")

    # Prompt user for start and end dates
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    if start_date > end_date:
        print("Error: Start date cannot be after end date.")
        return

    # Generate dates and prompt for weather data
    dates = generate_dates(start_date, end_date)
    weather_data = prompt_weather_data(dates)

    # Analyze the weather data
    highest_temp, lowest_temp = find_highest_lowest_temperatures(weather_data)
    days_above_30 = count_days_above_30(weather_data)
    average_humidity = compute_average_humidity(weather_data)

    # Print the results
    print(f"\nHighest Temperature Recorded: {highest_temp}°C")
    print(f"Lowest Temperature Recorded: {lowest_temp}°C")
    print(f"Number of Days with Temperatures Above 30°C: {days_above_30}")
    print(f"Average Humidity: {average_humidity:.2f}%")


if __name__ == "__main__":
    main()
