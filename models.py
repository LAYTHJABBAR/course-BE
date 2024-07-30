from datetime import datetime
import pandas as pd

def normalize_data(url):
    df = pd.read_csv(url)
    records = df.to_dict(orient='records')
    return records
