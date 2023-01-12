from controllers.fetch_data_controller import fetch_weather_data, KATOWICE_LATITUDE, KATOWICE_LONGITUDE, API_KEY
from controllers.save_data_controller import SaveDataController

if __name__ == '__main__':
    forecast = fetch_weather_data(KATOWICE_LATITUDE, KATOWICE_LONGITUDE, API_KEY)

    save_data_controller = SaveDataController("weather.xlsx")
    save_data_controller.save_base_statistics(forecast)
    save_data_controller.save_chart()
    save_data_controller.save_changes()