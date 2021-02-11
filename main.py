import requests
import csv


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

print(type(data))
json_data = data[0]
print(type(json_data))
print(json_data)

print("\n -------------------------- \n")

convert = json_data['rates']

print(f"Convert type: {type(convert)}")
print(f"convert {convert}")

columns_names = ['currency', 'code', 'bid', 'ask']

with open('data.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(columns_names)
    write.writerows(convert)