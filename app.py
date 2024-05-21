from flask import Flask, render_template, request
import requests
import writing
app = Flask(__name__)

@app.route("/") #główna strona
def main():
    return render_template("index.html")


@app.route("/convert", methods = ['POST']) #strona po wysłaniu żądania wymiany
def convert():
    currency = request.form.get('currency') #pobiera wartosc currency z formularza
    amount = request.form.get('amount') #pobiera wartosc amount z formularza
    if currency and amount:
        rate = writing.get_exchange_rate(currency)
        if rate is not None:
            pln_value = float(amount) * rate
            writing.file_writing(rate, float(amount), currency) #Funkcja która zapisuje historie do pliku
            return render_template("index.html", pln_value=pln_value) #zwraca strone internetową z wyswietloną wartoscia
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)

