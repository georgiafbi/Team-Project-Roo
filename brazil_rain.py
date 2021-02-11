import pandas as pd
import matplotlib.pyplot as plt
# Dependencies
import requests
from pprint import pprint
import numpy as np
import gmaps
import json
import os
from scipy.stats import linregress
from datetime import datetime
import time

# Google developer API key
from config import g_key

rain_data = pd.read_csv("conventional_weather_stations_inmet_brazil_1961_2019.csv", sep=";")
#rain_data_1df=rain_data.iloc[0:4]
del rain_data["Unnamed: 19"]
rain_data["Data"]=pd.to_datetime(rain_data['Data'])
rain_data['Day'] = rain_data['Data'].dt.day
rain_data['Month'] = rain_data['Data'].dt.month
rain_data['Year'] = rain_data['Data'].dt.year
rain_data=rain_data.loc[rain_data["Year"] >1987].reset_index()
#print(rain_data.head())
#clean_rain_df=rain_data.groupby(["Estacao", "Year"])
rain_data = rain_data.rename(columns={"Estacao": "Station", "Data": "Date", "Hora":"Time","Precipitacao":"Precipitation","UmidadeRelativa":"Relative Humidity","PressaoAtmEstacao":"Weather Presure","PressaoAtmMar":"Sea Pressure","TempBulboSeco":"DryBulb Temp","TempBulboUmido":"WetBulb Temp","TempMaxima":"Maximum Temp","TempMinima":"Minimal Temp","DirecaoVento":"Wind Ventilation","Insolacao":"Isolation","Nebulosidade":"Cloudiness","Evaporacao Piche":"Tar Evaporation","Temp Comp Media": "Average Temp","Umidade Relativa Media":"Average Humidity","Velocidade do Vento Media":"Average Wind Speed"})
rain_data.to_csv("clean_weather_station_data.csv")
print(rain_data.head(5))