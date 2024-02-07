import requests
import time
import pandas as pd
import os

def extract(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def transform(data):
    transformed_data = data['records']
    return transformed_data

def load(data, file_name):
    df = pd.DataFrame(data)
    print(df)
    if os.path.exists(file_name):
        df.to_csv(file_name, mode='a', header=False, index=False)
    else:
        df.to_csv(file_name, mode='w', header=True, index=False)

def main():
    api_url = "https://api.energidataservice.dk/dataset/CO2Emis?limit=5"
    while True:
        data = extract(api_url)
        if data:
            transformed_data = transform(data)
            load(transformed_data, 'data.csv')
        else:
            print("Fejl ved datahentning")
        time.sleep(5)

if __name__ == "__main__":
    main()
