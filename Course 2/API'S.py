import requests
from colorama import Fore
try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=35.652832&lon=139.839478&appid=2124f2c4071738e8fe379383ee9a57ba")
except:
    print("You don't have access to the internet!")

response_json = response.json()
temp = response_json["main"]["temp"]
temp_max = response_json["main"]["temp_max"]
temp_min = response_json["main"]["temp_min"]




class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}8&appid=2124f2c4071738e8fe379383ee9a57ba")
        except:
            print("You don't have access to the internet!")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_max = self.response_json["main"]["temp_max"]
        self.temp_min = self.response_json["main"]["temp_min"]

    def temp_print(self):
        print(Fore.LIGHTBLUE_EX + f"Currently {self.temp} degrees in {self.name}")
        print(Fore.RED + f"Highest temperature today in {self.name}: {self.temp_max}")
        print(Fore.GREEN + f"Lowest temperature today in {self.name}: {self.temp_min}")
mycity = City("Tokyo", 35.652832, 139.839478)
mycity.temp_print()
vacation_city = City("Portland", 45.5152, -122.6784)
vacation_city.temp_print()

print(vacation_city.response_json)

print(Fore.WHITE)