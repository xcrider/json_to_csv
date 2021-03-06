from flask import Flask, render_template, request, redirect
import requests
import csv

app = Flask(__name__)




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

    num_columns = len(array)
    csvfile.seek(0)

    reader = csv.reader(csvfile, delimiter=';')

    currency_codes = {row[1]: row[3] for row in reader}


@app.route('/index', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        return render_template("index.html", currency_codes=list(currency_codes.keys())[1:])
    elif request.method == 'POST':
        print(request.form)
        value = int(request.form.get('value'))
        exchange_value  = float(currency_codes[request.form.get('currency')])
        currency = request.form.get('currency')
        print(f'Exchange value = {exchange_value}')
        exchange_amount_r = round(value * exchange_value, 2)
        # exchange_amount_r = round(exchange_amount, 2)
        print(exchange_amount_r)
        return render_template("/index.html", currency_codes=list(currency_codes.keys())[1:], total_pln=exchange_amount_r, value=value, exchange_rate=exchange_value,currency =currency   )
