# mamba env create -f get_era.yml 
# conda activate get-era
# python get_era.py

import ee
import xarray as xr

# Paracou
ee.Initialize(project="ee-sylvainmschmitt", opt_url='https://earthengine-highvolume.googleapis.com')
ic = ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY").filter(ee.Filter.date('2023-01-01', '2025-01-02'))
pt = ee.Geometry.Point(-52.92486, 5.27877)
ds = xr.open_mfdataset([ic], 
                       engine='ee', 
                       projection=ic.first().select(0).projection(), 
                       geometry=pt,
                       fast_time_slicing=True)
ds['time'] = ds.time - 3*60*60*10**9
ds = ds[['temperature_2m']]
ds['tas'] = ds['temperature_2m'] - 273.15
ds_df = ds[['tas']].to_dataframe()
ds_df.to_csv("era5.tsv", sep="\t", index=True)

# Weather station Kourou CSG
ee.Initialize(project="ee-sylvainmschmitt", opt_url='https://earthengine-highvolume.googleapis.com')
ic = ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY").filter(ee.Filter.date('2020-01-01', '2026-01-01'))
pt = ee.Geometry.Point(-52.75, 5.25)
ds = xr.open_mfdataset([ic], 
                       engine='ee', 
                       projection=ic.first().select(0).projection(), 
                       geometry=pt,
                       fast_time_slicing=True)
ds['time'] = ds.time - 3*60*60*10**9
ds = ds[['temperature_2m']]
ds['tas'] = ds['temperature_2m'] - 273.15
ds_df = ds[['tas']].to_dataframe()
ds_df.to_csv("era5_station.tsv", sep="\t", index=True)
