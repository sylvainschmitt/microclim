# Raw data
Sylvain Schmitt -
Oct 9, 2025

All raw_data from different sources:

- guyaflux/: flux tower data from Damien Bonal pers. com.
- inventory/: inventory data and shapefile from Vincyane Badouard pers.
  com.
- macro/: ERA5-Land data from openmeteodata service and MeteoFrance data
  for French Guaian from government open data.
- micro/: Tomst ancillary and raw data from Vincyane Badouard pers. com.
- pedo/: pedology data from Vincyane Badouard pers. com.
- topo/: topography raster from Vincyane Badouard pers. com.
- veg/: lidar data from Vincyane Badouard pers. com.

``` r
fs::dir_tree()
```

    .
    ├── README.md
    ├── README.qmd
    ├── README.rmarkdown
    ├── guyaflux
    │   └── TourAFlux-2023-2024.xlsx
    ├── inventory
    │   ├── ALT
    │   │   ├── ALT.dbf
    │   │   ├── ALT.prj
    │   │   ├── ALT.shp
    │   │   └── ALT.shx
    │   ├── ALT_Paracou9ha_20250129_cleancord.csv
    │   └── Piquets_ALT_coordinates.csv
    ├── macro
    │   ├── MENSQ_973_1946-1949.csv.gz
    │   ├── MENSQ_973_latest-2024-2025.csv.gz
    │   ├── MENSQ_973_previous-1950-2023.csv.gz
    │   ├── MENSQ_988_1938-1949.csv.gz
    │   ├── MENSQ_988_latest-2024-2025.csv.gz
    │   ├── MENSQ_988_previous-1950-2023.csv.gz
    │   ├── era5.tsv
    │   ├── get_era.py
    │   ├── get_era.yml
    │   └── mensq_descriptif_champs_323.csv
    ├── micro
    │   ├── Nouragues
    │   │   ├── data_94244901_2024_02_22_0.csv
    │   │   ├── data_94244901_2024_06_20_0.csv
    │   │   ├── data_94244902_2024_02_22_0.csv
    │   │   ├── data_94244902_2024_06_20_0.csv
    │   │   ├── data_94244903_2024_02_22_0.csv
    │   │   ├── data_94244903_2024_06_20_0.csv
    │   │   ├── data_94244904_2024_02_22_0.csv
    │   │   ├── data_94244904_2024_06_20_0.csv
    │   │   ├── data_94244905_2024_02_22_0.csv
    │   │   ├── data_94244906_2024_02_22_0.csv
    │   │   ├── data_94244906_2024_06_20_0.csv
    │   │   ├── data_94244907_2024_02_22_0.csv
    │   │   ├── data_94244907_2024_06_20_0.csv
    │   │   ├── data_94244908_2024_02_22_0.csv
    │   │   ├── data_94244908_2024_06_20_0.csv
    │   │   ├── data_94244909_2024_02_22_0.csv
    │   │   ├── data_94244909_2024_06_20_0.csv
    │   │   ├── data_94244910_2024_02_22_0.csv
    │   │   ├── data_94244910_2024_06_20_0.csv
    │   │   ├── data_94244910_2024_06_20_1.csv
    │   │   ├── data_94244912_2024_02_22_0.csv
    │   │   ├── data_94244912_2024_06_20_0.csv
    │   │   ├── data_94244913_2024_02_22_0.csv
    │   │   ├── data_94244913_2024_06_20_0.csv
    │   │   ├── data_94244914_2024_02_22_0.csv
    │   │   ├── data_94244914_2024_06_20_0.csv
    │   │   ├── data_94244915_2024_02_22_0.csv
    │   │   ├── data_94244915_2024_06_20_0.csv
    │   │   ├── data_94244917_2024_02_22_0.csv
    │   │   ├── data_94244917_2024_06_20_0.csv
    │   │   ├── data_94244918_2024_02_22_0.csv
    │   │   ├── data_94244918_2024_06_20_0.csv
    │   │   ├── data_94244919_2024_02_22_0.csv
    │   │   ├── data_94244919_2024_06_20_0.csv
    │   │   ├── data_94244920_2024_02_22_0.csv
    │   │   ├── data_94244920_2024_06_20_0.csv
    │   │   ├── data_94244931_2024_06_20_0.csv
    │   │   └── data_94244932_2024_06_20_0.csv
    │   ├── Nouragues_Tomst_humidity_granulo_parameters.csv
    │   ├── Nouragues_test
    │   │   ├── data_94244901_2023_02_22_0.csv
    │   │   ├── data_94244902_2023_02_22_0.csv
    │   │   ├── data_94244903_2023_02_22_0.csv
    │   │   ├── data_94244904_2023_02_22_0.csv
    │   │   ├── data_94244905_2023_02_22_0.csv
    │   │   ├── data_94244906_2023_02_22_0.csv
    │   │   ├── data_94244907_2023_02_22_0.csv
    │   │   ├── data_94244908_2023_02_22_0.csv
    │   │   ├── data_94244909_2023_02_22_0.csv
    │   │   ├── data_94244910_2023_02_22_0.csv
    │   │   ├── data_94244911_2023_02_22_0.csv
    │   │   ├── data_94244912_2023_02_22_0.csv
    │   │   ├── data_94244913_2023_02_22_0.csv
    │   │   ├── data_94244914_2023_02_22_0.csv
    │   │   ├── data_94244915_2023_02_22_0.csv
    │   │   ├── data_94244916_2023_02_22_0.csv
    │   │   ├── data_94244917_2023_02_22_0.csv
    │   │   ├── data_94244918_2023_02_22_0.csv
    │   │   ├── data_94244919_2023_02_22_0.csv
    │   │   └── data_94244920_2023_02_22_0.csv
    │   ├── Paracou
    │   │   ├── data_94223161_2024_06_05_0.csv
    │   │   ├── data_94223162_2024_06_05_0.csv
    │   │   ├── data_94223163_2024_06_05_0.csv
    │   │   ├── data_94223164_2024_05_06_0.csv
    │   │   ├── data_94223164_2024_06_05_0.csv
    │   │   ├── data_94223164_2024_06_05_1.csv
    │   │   ├── data_94223165_2024_05_06_0.csv
    │   │   ├── data_94223165_2024_06_05_0.csv
    │   │   ├── data_94223166_2024_05_06_0.csv
    │   │   ├── data_94223167_2024_05_06_0.csv
    │   │   ├── data_94223168_2024_05_06_0.csv
    │   │   ├── data_94223169_2024_05_06_0.csv
    │   │   ├── data_94223170_2024_05_06_0.csv
    │   │   ├── data_94223171_2024_05_06_0.csv
    │   │   ├── data_94223172_2024_05_06_0.csv
    │   │   ├── data_94223173_2024_05_06_0.csv
    │   │   ├── data_94223174_2024_05_06_0.csv
    │   │   ├── data_94223175_2024_05_06_0.csv
    │   │   ├── data_94223176_2024_05_06_0.csv
    │   │   ├── data_94223177_2024_05_06_0.csv
    │   │   ├── data_94223178_2024_05_06_0.csv
    │   │   ├── data_94223179_2024_05_06_0.csv
    │   │   ├── data_94223180_2024_05_06_0.csv
    │   │   ├── data_94223181_2024_05_06_0.csv
    │   │   ├── data_94223182_2024_05_06_0.csv
    │   │   ├── data_94244921_2024_06_05_1.csv
    │   │   ├── data_94244922_2024_06_05_0.csv
    │   │   ├── data_94244923_2024_06_05_0.csv
    │   │   ├── data_94244924_2024_06_05_0.csv
    │   │   ├── data_94244925_2024_06_05_0.csv
    │   │   ├── data_94244926_2024_05_06_0.csv
    │   │   ├── data_94244926_2024_05_06_1.csv
    │   │   ├── data_94244927_2024_05_06_0.csv
    │   │   ├── data_94244928_2024_05_06_0.csv
    │   │   ├── data_94244929_2024_05_06_0.csv
    │   │   └── data_94244930_2024_05_06_0.csv
    │   ├── Paracou_Tomst_humidity_granulo_parameters.csv
    │   ├── Tomst sensors - Nouragues - Data.csv
    │   └── Tomst-HOBO sensors - Paracou - Data.csv
    ├── pedo
    │   └── Labo_data_binded.csv
    ├── topo
    │   ├── Paracou_ALT_TWI_5m.tif
    │   └── Paracou_ALT_mnt.tif
    └── veg
        ├── P16_2023_HighAlt_25ha_buffer_PadHLE_intensity1m_testnewEB.vox
        └── VOP_P16_25ha.txt
