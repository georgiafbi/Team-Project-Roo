# Team_Roo

# Deforestation and Precipitation Data Analysis Program
Project 1

# Hypothesis
Ho: Deforestation in Brazil has no effect on the average yearly rainfall in the area of deforestation.

Ha: Deforestation in Brazil affects the average yearly rainfall in the area of deforestation.
======================================================================================================================
Part 1: Project Code and Instructions

python libraries used: the pandas, numpy, matplotlib, datetime, time, and pprint

Run each .ipynb in this order:

1. AmazonDeforestPy.ipynb: pulls data from a csv on deforestation data found at http://terrabrasilis.dpi.inpe.br/app/dashboard/deforestation/biomes/legal_amazon/rates 
and created a dataframe using pandas module. Data was cleaned using various pandas functions then saved this file (deforestation_per_year_data.csv) as .csv 
into new directory called useable_csv. Please download this data from the websource and add it to new directory called (csv_files) in order to run this program. 

2. WeatherStationsPy.ipynb: pulls data from a .csv on weather station data found at https://www.kaggle.com/saraivaufc/conventional-weather-stations-brazil. Here a .csv file (weather_stations_codes.csv) can be found. This data is cleaned using the pandas library and saved to a new .csv (station_and_state.csv) file in the directory useable_csv.
Please download this data from the websource and add it to new directory called (csv_files) in order to run this program. 

3. BrazilianRainPy.ipynb: pulls data from a .csv on conventional historical weather data for Brazil found at https://www.kaggle.com/saraivaufc/conventional-weather-stations-brazil. 
Here a .csv file (conventional_weather_stations_inmet_brazil_1961_2019.csv) can be found that is used in this program. This .csv file is cleaned using the pandas library and saved 
as useable .csv in the directory useable_csv. Please download this data from the websource and add it to new directory called (csv_files) in order to run this program. 

# Warning these .csv are large please .gitignore the directory csv_files when you create it. Do not push this to you github
-----------------------------------------------------------------------------------------------------------------------
Part 2: Project Code and Instructions

python libraries used: the pandas, numpy, matplotlib, datetime, time, and pprint libraries, scipy.stats

Run each .ipynb in this order:

1. Summary_graphs.ipynb: pulls .csv(s) (total_rainfall_by_year_by_state.csv, deforestation_per_year_data.csv) from useable_csv file directory to run further data cleaning with the pandas library. Uses the matplotlib and numpy libraries to generate data analysis plots on deforestation amount by brazilian state against the precipitation data from 1997 to 2019. These plots are saved to a new directory called charts_and_graphs.

2. Chitest.ipynb: pulls a .csv from the useable_csv directory called rainfall_data_97.csv to be used for a chi-test analysis. The chi-test is use to calculate the chi-square vaule, p-value, and critical value in order to determine if the observed precipitation quantities vs the expected precipitation quantities overtime (deforestation does not deminish precipitation in the areas of deforestation) are statistically significant. 


=======================================================================================================================

Conclusion: current data findings, we cannot confirm whether or not there is any correlation between rainfall and deforestation. 

========================================================================================================================
# Contact Information for information on the project and code

Slack: Glenn Craven: U01G7SZ9N74 (Member ID) , Alexis Kepano: U01GK4742P6 (Member ID), Destany Brown: U01FXMT59C6 (Member ID)