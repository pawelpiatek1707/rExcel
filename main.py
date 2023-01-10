from controllers.fetch_data_controller import fetch_weather_data, KATOWICE_LATITUDE, KATOWICE_LONGITUDE, API_KEY


forecast = fetch_weather_data(KATOWICE_LATITUDE, KATOWICE_LONGITUDE, API_KEY)

print(forecast)