import os
import re
# Task 2: Historical Weather Data Compiler

# Problem Statement:
# Compile and analyze historical weather data from multiple files 
# (weather_2020.txt, weather_2021.txt, etc.). 
# Each file contains daily temperature data. 
# Calculate the average temperature for each year and identify the year with the highest average.

# - Dataset Example:
# File: weather_2020.txt
# 2020-01-01,5°C
# 2020-01-15,6°C
# 2020-02-05,4°C
# 2020-02-20,7°C
# 2020-03-10,8°C
# 2020-03-25,9°C
# 2020-04-05,12°C
# 2020-04-20,14°C
# 2020-05-05,17°C
# 2020-05-20,19°C
# 2020-06-05,22°C
# 2020-06-20,25°C
# 2020-07-05,28°C
# 2020-07-20,30°C
# 2020-08-05,32°C
# 2020-08-20,31°C
# 2020-09-05,27°C
# 2020-09-20,24°C
# 2020-10-05,19°C
# 2020-10-20,16°C
# 2020-11-05,11°C
# 2020-11-20,9°C
# 2020-12-05,6°C
# 2020-12-20,4°C
# File: weather_2021.txt
# 2021-01-01,3°C
# 2021-01-15,4°C
# 2021-02-05,6°C
# 2021-02-20,8°C
# 2021-03-10,10°C
# 2021-03-25,11°C
# 2021-04-05,14°C
# 2021-04-20,16°C
# 2021-05-05,19°C
# 2021-05-20,21°C
# 2021-06-05,24°C
# 2021-06-20,27°C
# 2021-07-05,30°C
# 2021-07-20,32°C
# 2021-08-05,33°C
# 2021-08-20,31°C
# 2021-09-05,28°C
# 2021-09-20,26°C
# 2021-10-05,21°C
# 2021-10-20,18°C
# 2021-11-05,13°C
# 2021-11-20,10°C
# 2021-12-05,7°C
# 2021-12-20,5°C
# Code Example:
def extract_temperature_data(file):
    # Extract temperature data from the file
    temperatures = []
    with open(file, 'r') as f:
        for line in f:
            # Split line at the comma
            parts = line.split(',')
            if len(parts) > 1:  # Ensure there is a part after the comma
                # Take the part after the comma, remove "°C", and convert to int
                temperature_str = parts[1].replace('°C', '').replace('Â', '').strip()
                try:
                    temperature = int(temperature_str)
                    temperatures.append(temperature)
                except ValueError:
                    # Handle the case where conversion to int fails
                    print(f"Warning: Could not convert '{temperature_str}' to an integer.")
    return temperatures


def compile_weather_data(data_files):
    # Aggregate temperatures in file and calculate the yearly average
    yearly_averages = {}
    highest_average = 0
    highest_year = None
    for file in data_files:
        year = re.search(r'\d{4}', file).group()
        if year not in yearly_averages:
            yearly_averages[year] = []
        with open(file, 'r') as f:
            data = f.readlines()
            temperatures = extract_temperature_data(file)
            yearly_averages[year].extend(temperatures)
    for year, temps in yearly_averages.items():
        average_temp = sum(temps) / len(temps)
        print(f"Year: {year}, Average Temperature: {average_temp:.2f}°C")
        if average_temp > highest_average:
            highest_average = average_temp
            highest_year = year
    print(f"The year with the highest average temperature is {highest_year} with {highest_average:.2f}°C.")


    


data_files = ["weather_2020.txt", "weather_2021.txt", "weather_2022.txt"]
compile_weather_data(data_files)   



# Expected Outcome:
# An aggregated view of average temperatures for each year and identification of the year 
# with the highest average temperature, showcasing data aggregation and analysis skills.