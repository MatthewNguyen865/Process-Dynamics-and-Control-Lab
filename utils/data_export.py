import csv
import os

def save_trajectory_to_csv(times: list[float], temperatures: list[float], filename: str) -> None:

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    if len(times) != len(temperatures):
        raise ValueError("times and temperatures must have the same length")
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["time", "temperature"])

        for t, temperature in zip(times, temperatures):
            writer.writerow([t, temperature])


def save_multi_trajectory_to_csv(times: list[float], trajectories: list[list[float]], labels: list[str], filename: str) -> None:

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    if len(trajectories) != len(labels):
        raise ValueError("trajectories and labels must have the same length")

    for trajectory in trajectories:
        if len(trajectory) != len(times):
            raise ValueError("all trajectories must have the same length as times")

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["time"] + labels)

        for i, time in enumerate(times):
            row = [time]

            for trajectory in trajectories:
                row.append(trajectory[i])

            writer.writerow(row)