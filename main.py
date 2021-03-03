from flask import Flask, render_template, request, redirect
import requests
import csv

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
       return render_template("index.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


def update_exchange():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()

    json_data = data[0] #convert to dict

    convert = json_data['rates'] #get rates

    print(f"Convert type: {type(convert)}")
    print(f"convert {convert}")

    csv_columns = ['currency', 'code', 'bid', 'ask']
    csv_file = "data.csv"

    #save into data.csv file
    with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=";")
            writer.writeheader()
            for data in convert:
                writer.writerow(data)

# open csv file
csv_file = "data.csv"
with open(csv_file, 'r') as csvfile:

    # get number of columns
    for line in csvfile.readlines():
        array = line.split('\n')
        first_item = array[0]

    num_columns = len(array)
    csvfile.seek(0)

    reader = csv.reader(csvfile, delimiter=';')
    included_cols = [1]

    for row in reader:
        currency_codes = list(row[i] for i in included_cols)
        print(currency_codes)
