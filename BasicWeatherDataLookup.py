# Mock weather data for various cities
weather_data = {
    "New York": {"temperature": 75, "condition": "Sunny"},
    "London": {"temperature": 60, "condition": "Cloudy"},
    "Tokyo": {"temperature": 80, "condition": "Rainy"},
    "Sydney": {"temperature": 70, "condition": "Partly Cloudy"},
}

# Function to get weather for a city, with a lambda for formatting error message
get_weather = lambda city: weather_data.get(city, None)

# Function to display weather using lambda for formatted display
display_weather = lambda city, data: print(
    f"Weather in {city}: {data['temperature']}°F, {data['condition']}"
) if data else print("City not found. Please try again.")

# Main program loop
while True:
    city = input("Enter a city name (or type 'exit' to quit): ").strip()
    
    if city.lower() == 'exit':
        print("Exiting the program.")
        break
    
    # Retrieve the weather data
    city_weather = get_weather(city)
    
    # Display weather data
    display_weather(city, city_weather)