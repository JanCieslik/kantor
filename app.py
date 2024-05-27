from flask import Flask, render_template, request
import requests
import functions
app = Flask(__name__)

@app.route("/") #główna strona
def main():
    return render_template("main.html")
def submit1():
    return redirect(url_for('convert'))
def submit2():
    return redirect(url_for('medium_value'))
@app.route("/medium_value", methods = ['GET' ,'POST']) #strona ze srednia cena
def medium_value():
    currency = request.form.get('currency')
    date_from = request.form.get('dateFrom')
    date_to = request.form.get('dateTo')
    if currency and date_from and date_to:
        min_rate, max_rate, currency  = functions.get_hight_and_low_value(currency, date_from,date_to)
        return render_template('medium_value.html', currency=currency, min_rate = min_rate, max_rate=max_rate)
    return render_template("medium_value.html")
@app.route("/convert", methods = ['POST']) #strona po wysłaniu żądania wymiany
def convert():
    currency = request.form.get('currency') #pobiera wartosc currency z formularza
    amount = request.form.get('amount') #pobiera wartosc amount z formularza
    if currency and amount:
        rate = functions.get_exchange_rate(currency)
        if rate is not None:
            pln_value = float(amount) * rate
            functions.file_writing(rate, float(amount), currency) #Funkcja która zapisuje historie do pliku
            return render_template("exchange.html", pln_value=pln_value) #zwraca strone internetową z wyswietloną wartoscia
    return render_template("exchange.html")




if __name__ == "__main__":
    app.run(debug=True)

