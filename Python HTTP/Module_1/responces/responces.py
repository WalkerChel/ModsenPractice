import requests, os
from dotenv import load_dotenv

load_dotenv()

ApiKey: str = os.getenv("API_KEY")
City: str = "Minsk"


def main() -> None:

    lat, lon = getCoordinates(City, ApiKey)
    
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ApiKey}&units=metric'
    print(getCurrentWeather(url))


def getCurrentWeather(url: str) -> str:
    '''
    returns current weather info 
    '''

    res = requests.get(url)

    if (res.status_code != 200) or (res.json() == []):
        raise Exception("error getting weather info:\n", res.text)
        
    jr = res.json()

    description = jr.get("weather")[0].get("description")
    temp = jr.get("main").get("temp")
    country = jr.get("sys").get("country")

    # print(jr)

    weather = f"Tempreature: {temp} ℃; \nDescription: {description}; \nCountry: {country}: \nCity: {City}"

    return weather
        

def getCoordinates(city: str, apiKey: str):
    '''
    returns information about city
    '''

    res = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={apiKey}")
    
    if (res.status_code != 200) or (res.json() == []):
        raise Exception("error getting coordinates:", res.text)
        
    jr = res.json()

    # print(jr)

    lat = jr[0].get("lat")
    lon = jr[0].get("lon")

    return lat, lon
        


if __name__ == "__main__":
    main()