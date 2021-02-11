import requests
import csv


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

json_data = data[0] #convert to dict

convert = json_data['rates'] #get rates

print(f"Convert type: {type(convert)}")
print(f"convert {convert}")

csv_columns = ['currency', 'code', 'bid', 'ask']

csv_file = "data.csv"

with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in convert:
            writer.writerow(data)