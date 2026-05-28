import csv
import os

def save_trajectory_to_csv(times, temperatures, filename):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["time", "temperature"])

        for time, temperature in zip(times, temperatures):
            writer.writerow([time, temperature])