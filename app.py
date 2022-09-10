
from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes


app = Flask(__name__)

app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"
# app.run(debug=True)
currency = {u'USD': 1, u'IDR': 13625.0, u'BGN': 1.7433, u'ILS': 3.8794, u'GBP': 0.68641, u'DKK': 6.6289, u'CAD': 1.3106, u'JPY': 110.36, u'HUF': 282.36, u'RON': 4.0162, u'MYR': 4.081, u'SEK': 8.3419, u'SGD': 1.3815, u'HKD': 7.7673, u'AUD': 1.3833, u'CHF': 0.99144,
            u'KRW': 1187.3, u'CNY': 6.5475, u'TRY': 2.9839, u'HRK': 6.6731, u'NZD': 1.4777, u'THB': 35.73, u'EUR': 0.89135, u'NOK': 8.3212, u'RUB': 66.774, u'INR': 67.473, u'MXN': 18.41, u'CZK': 24.089, u'BRL': 3.5473, u'PLN': 3.94, u'PHP': 46.775, u'ZAR': 15.747}


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/convert', methods=["GET", "POST"])
def check_convert():

    # need to pull dictionary from the api
    # dictname = [{'dict key': 'value'}]

    from_curr = request.args["from_curr"]
    to_curr = request.args["to_curr"]
    amount_from = request.args["amount_from"]
    c = CurrencyRates()
    conversion = ''
    cc = CurrencyCodes()

    if from_curr in currency:

        if to_curr in currency:

            if amount_from.isnumeric():

                all_curr = c.get_rates(str(from_curr))
                all_curr[from_curr] = int(amount_from)

                conversion = c.convert(
                    str(from_curr), str(to_curr), int(amount_from))
                rounded_conversion = round(conversion, 2)
                symbol = cc.get_symbol(to_curr)
            return render_template("convert.html", from_curr=from_curr, to_curr=to_curr, amount_from=amount_from, conversion=rounded_conversion, symbol=symbol)
        else:
            flash('invalid Currency or amount')
        return redirect("/")
    else:
        flash('invalid Currency or amount')
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
