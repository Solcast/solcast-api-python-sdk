import csv
import json
import requests
#import certifi
#import ssl
#from urllib.request import urlopen

#context = ssl.create_default_context(cafile=certifi.where())

def get_api_response(latitude, longitude, duration, startdate):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    url = f'https://api.solcast.com.au/data/historic/radiation_and_weather?latitude={latitude}&longitude={longitude}&duration={duration}&format=json&time_zone=utc&output_parameters=ghi,snow_soiling_rooftop&hours=24&period=PT60M&start={startdate}T00:00:00.000Z&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            print("JSON data received:", data)
            return data
        except ValueError as e:
            print("Failed to parse JSON:", e)
            print("Response content:", response.text)
            return None
    elif response.status_code == 404:
        print("Error 404: Not Found")
        return None
    else:
        print(f"Server returned status code {response.status_code}")
        print("Response content:", response.json())
        return None

def process_csv(csv_file):
    data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            latitude = row['latitude']
            longitude = row['longitude']
            duration = row['duration']
            startdate = row['startdate']
            api_response = get_api_response(latitude, longitude, duration, startdate)
            if api_response:
                data.append(api_response)
    return data

def save_to_json(data, json_file):
    with open(json_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def main():
    csv_file = r'./location_data.csv'
    json_file = r'./output.json'
    data = process_csv(csv_file)
    save_to_json(data, json_file)
    print("JSON file created successfully.")

if __name__ == "__main__":
    main()
