#!/usr/bin/python
from flask import Flask, render_template
import rrdtool
from chart_temp import updateTempCharts
from chart_humidity import updateHumidityCharts
from chart_pressure import updatePressureCharts
from chart_current import updateCurrentCharts

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def main():
    return render_template('home.html')

@app.route("/temperatura")
def temperatura():
    updateTempCharts()
    return render_template('temperature.html')


@app.route("/humedad")
def humedad():
    updateHumidityCharts();
    return render_template('humidity.html')

@app.route("/presion")
def presion():
    updatePressureCharts()
    return render_template('pressure.html')

@app.route("/potencia")
def potencia():
    updateCurrentCharts()
    return render_template('current.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
