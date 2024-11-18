import pandas as pd

def output(label: str, value: float, data: dict):
    print(label, "=", value)
    if not label in data.keys(): data[label] = []
    data[label].append(value)

def toFrame(data: dict):
    return pd.DataFrame(data)