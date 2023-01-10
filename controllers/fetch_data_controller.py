import requests

# Funkcja pobiera prognoze pogody na 5 kolejnych dni. Dane są w odstęoach co 3 godziny

API_KEY = "f0c404ce8de332d3bebb638afe1fa913"
KATOWICE_LATITUDE = 50.270908
KATOWICE_LONGITUDE = 19.039993
KELVIN = 273.15

def convert_temperature(temperature: float):
    return round(temperature - KELVIN, 2)

def fetch_weather_data(latitude: float, longitude: float, api_key: str):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}")
    forecast = response.json()
    transformed_forecast = []
    for daily_forecast in forecast['list']:
        date = daily_forecast["dt"]
        date_txt = daily_forecast["dt_txt"]
        main_info = daily_forecast["main"]
        temperature  = main_info["temp"]
        # date -> timestamp
        # date_text -> data w formie tekstowej
        # temperature -> temperatura w stopniach Celsjusza
        transformed_forecast.append({
            "date": date,
            "date_txt": date_txt,
            "temperature": convert_temperature(temperature)
        })

    return transformed_forecast
