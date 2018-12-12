"""
These are my data analysis functions. Used to download and process Berkeley temperature time series.
"""

import numpy as np
import requests

def build_url(country):
    "Build a Berkeley Earth URL to download data"
    url = f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{country.lower()}-TAVG-Trend.txt'
    return url

def download_data(country, fname=None):
    "Donwload the data for the given country, load it and optionally save to a file"
    url = build_url(country)
    response = requests.get(url)
    if fname is not None:
        with open(fname, "w") as open_file:
            open_file.write(response.text)
    data = np.loadtxt(response.iter_lines(), comments="%")
    return data

def moving_average(data, window_size):
    "Calculate a moving average over 1D data using the given window size"
    average = np.full(data.size, np.nan)
    half_window = window_size // 2
    for i in range(half_window, data.size - half_window):
        average[i] = np.mean(data[i - half_window : i + half_window])
    return average
