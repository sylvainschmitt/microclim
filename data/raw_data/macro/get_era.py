# mamba env create -f get_era.yml 
# conda activate get-era
# python get_era.py

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)
url = "https://archive-api.open-meteo.com/v1/archive"

params = {
	"latitude": -3,
	"longitude": -55,
	"start_date": "2001-12-31",
	"end_date": "2012-01-01",
	"hourly": ["temperature_2m", "precipitation", "vapour_pressure_deficit", "wind_speed_10m", "terrestrial_radiation_instant"],
	"timezone": "auto",
	"models": "era5_land"
}
responses = openmeteo.weather_api(url, params=params)
response = responses[0]
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(1).ValuesAsNumpy()
hourly_vapour_pressure_deficit = hourly.Variables(2).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(3).ValuesAsNumpy()
hourly_terrestrial_radiation_instant = hourly.Variables(4).ValuesAsNumpy()
hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s"),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["precipitation"] = hourly_precipitation
hourly_data["vapour_pressure_deficit"] = hourly_vapour_pressure_deficit
hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
hourly_data["terrestrial_radiation_instant"] = hourly_terrestrial_radiation_instant
hourly_dataframe = pd.DataFrame(data = hourly_data)
hourly_dataframe.to_csv("era5_tapajos.csv")

