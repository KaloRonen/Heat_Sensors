import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


def get_sensor_data():
    dirpath = os.path.dirname(__file__)
    sensors_position_filepath = os.path.join(dirpath, 'sensors_data', 'sensors_position_data_file.txt')
    sensor_heat_data_filepath = os.path.join(dirpath, 'sensors_data', 'sensors_heat_data_file.txt')

    sensor_positions = pd.read_table(sensors_position_filepath, sep='\s+', header=None, names=["x", "y"])
    sensor_heat_data = pd.read_table(sensor_heat_data_filepath, sep='\s+', header=None)

    data = sensor_positions.join(sensor_heat_data)

    return data


def main():
    all_data = get_sensor_data()
    print(all_data.isnull().values.any())



if __name__ == 'main':
    main()


main()
