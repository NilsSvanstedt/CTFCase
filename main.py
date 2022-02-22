import requests  # HTTP library for easier HTTP requests
import config  # file with API key
from geopy.geocoders import Nominatim

# set API key using config file to prevent abuse
api_key = config.api_key

user_agent = input("Enter your username: ")
# Connection to nominatim api for getting coordinates
geolocator = Nominatim(user_agent=f"{user_agent}")


def getweather(city_name):
    # get coordinates from city name
    location = geolocator.geocode(city_name)

    # set siteurl (current weather data api)
    try:
        return f'https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&units=Metric&appid={api_key}'
    except AttributeError:
        print("Incorrect city input. Try again.")
        return 'error'


# set the header
headers = {'Accept': 'application/vnd.github.v3+json'}

# Input from user
print("Type 0 to quit.")
while 1 == 1:
    city_name = input("Enter city name for weather data: ")
    if city_name != '0':
        if not city_name.isalpha():
            print("Input should solely consist of letters. Try again.")
            continue
        # call API and save response
        url = getweather(city_name)
        if url != 'error':
            response = requests.get(url, headers=headers)
            response_json = response.json()
            print(
                f"Temperature: {response_json['main']['temp']} Celsius \nPressure: {response_json['main']['pressure']} kPa ")
            print(f"Description: {response_json['weather'][0]['description']}")
    else:
        quit()
