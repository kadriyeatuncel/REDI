# requests library
import requests
city_name = input("Please enter the city")
api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"

# The response from the API
api_response = requests.get(url = api_url) # the function we use from requests

# Converts the response from the API to the dictionary
api_response_json = api_response.json() # 

# Parse the response to get the required information
#print(f'The response from the API: {api_response_json}')

all_results = api_response_json["results"]
#print(f'All the results: {all_results}')

city_result = all_results[0]
print(f'The first result: {city_result}')

city_population = city_result["population"]
city_name = city_result["name"]

print(f'The population of {city_name}: {city_population}')

print(f'The latitude in {city_name}: {city_result["latitude"]}')
print(f'The longitude in {city_name}: {city_result["longitude"]}')
print(f'The elevation in {city_name}: {city_result["elevation"]}')
import requests

# Dictionary with the weather codes from https://open-meteo.com
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain shower",
    81: "Moderate rain shower",
    82: "Violent rain shower",
    85: "Slight snow shower",
    86: "Heavy snow shower",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

def get_coordinates(city_name):
    """Returns the latitude, longitude and elevation of a city."""
    # Create the API call URL for geocoding
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
    # Send the request and get the response
    response = requests.get(url)
    data = response.json()
        
    # Check if the city was found in the results
    if "results" not in data:
        raise Exception("City not found.")
    
    # Extract coordinates and elevation
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]

    print(f'The latitude in {city_name}: {city_result["latitude"]}')
    print(f'The longitude in {city_name}: {city_result["longitude"]}')
    print(f'The elevation in {city_name}: {city_result["elevation"]}')
    return latitude, longitude, elevation


def get_weather(city_name):
    """Fetches the current weather description and temperature for a city."""
    try:
        # Step 1: Get coordinates using the helper function
        lat, lon, elev = get_coordinates(city_name)
        
        # Step 2: Create the Forecast API URL
        # We must include current_weather=true to get instantaneous data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&elevation={elev}&current_weather=true"
        
        # Step 3: Send the request and convert response to dictionary
        response = requests.get(weather_url)
        weather_data = response.json()
        
        # Step 4: Extract temperature and weather code from the response
        current = weather_data["current_weather"]
        temperature = current["temperature"]
        weather_code = current["weathercode"]
        
        # Step 5: Map the weather code to a string description
        weather_desc = WEATHER_CODES.get(weather_code, "Unknown weather")
        
        return weather_desc, temperature
        
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# --- Main Program Execution ---
if __name__ == "__main__":
    while True:
        # Ask the user for a city name
        user_input = input("Please enter the name of a city: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print("Exit")
            break
        
        # Call the weather function
        weather, temp = get_weather(user_input)
        
        # Print the result if no error occurred
        if weather is not None:
            print(f"The current weather in {user_input} is {weather} and the temperature is {temp}°C.")
import requests
import json  # Library to format and print JSON data nicely

# Dictionary with the weather codes from https://open-meteo.com
# These codes represent specific weather conditions returned by the API
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain shower",
    81: "Moderate rain shower",
    82: "Violent rain shower",
    85: "Slight snow shower",
    86: "Heavy snow shower",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

def get_coordinates(city_name):
    """
    Translates a city name into GPS coordinates (latitude, longitude, and elevation).
    Uses the Open-Meteo Geocoding API.
    """
    # Create the API URL for geocoding search
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
    # Send a GET request to the URL
    response = requests.get(url)
    data = response.json()
    
    # Check if the API returns no results, raise an error
    if "results" not in data:
        raise Exception(f"City '{city_name}' not found.")
    
    # Access the first search result [0] in the results list
    city_result = data["results"][0]
    
    # Extract the necessary location data
    latitude = city_result["latitude"]
    longitude = city_result["longitude"]
    elevation = city_result["elevation"]

    # Print coordinate details for the user
    print(f"\n--- Location Found ---")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Elevation: {elevation}m")
    
    return latitude, longitude, elevation

def get_weather(city_name):
    """
    Fetches the current weather and temperature for a given city.
    Combines the Geocoding API and the Forecast API.
    """
    try:
        # Step 1: Get GPS coordinates using the helper function
        lat, lon, elev = get_coordinates(city_name)
        
        # Step 2: Build the Forecast API URL using the coordinates
        # 'current_weather=true' is required to get live data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&elevation={elev}&current_weather=true"
        
        # Step 3: Fetch weather data and convert to a Python dictionary
        response = requests.get(weather_url)
        weather_data = response.json()
        
        # Step 4: Extract current weather values
        current = weather_data["current_weather"]
        temperature = current["temperature"]
        weather_code = current["weathercode"]
        
        # Step 5: Convert the numeric weather code into a readable description
        weather_desc = WEATHER_CODES.get(weather_code, "Unknown weather")
        
        return weather_desc, temperature
        
    except Exception as e:
        # If an error occurs (e.g., city not found), display the error message
        print(f"Error: {e}")
        return None, None

# --- Main Program Loop ---
if __name__ == "__main__":
    print("Welcome to the Weather App!")
    
    while True:
        # Ask for user input
        user_input = input("\nPlease enter a city name (or type 'exit' to quit): ")
        
        # Check if the user wants to stop the program
        if user_input.lower() == "exit":
            print("exit!")
            break
        
        # Call the get_weather function
        weather, temp = get_weather(user_input)
        
        # Display the final result to the user
        if weather is not None:
            print(f"\nRESULT: The current weather in {user_input} is {weather} and the temperature is {temp}°C.")