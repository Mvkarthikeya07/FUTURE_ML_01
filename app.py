from flask import Flask, render_template
from data_processing import load_and_prepare_data
from forecast import train_and_forecast

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    # Load & prepare data
    data = load_and_prepare_data('data/sales_data.csv')

    # Forecast + metrics
    forecast, rmse, mape = train_and_forecast(data, steps=6)

    # Historical data
    historical_labels = data.index.strftime('%Y-%m').tolist()
    historical_sales = data['sales'].tolist()

    # Forecast data
    forecast_labels = forecast.index.strftime('%Y-%m').tolist()
    forecast_sales = forecast.round(2).tolist()

    # ✅ Prepare FINAL chart arrays (NO logic in Jinja)
    chart_labels = historical_labels + forecast_labels
    chart_historical = historical_sales + [None] * len(forecast_sales)
    chart_forecast = [None] * len(historical_sales) + forecast_sales

    return render_template(
        'dashboard.html',
        chart_labels=chart_labels,
        chart_historical=chart_historical,
        chart_forecast=chart_forecast,
        rmse=rmse,
        mape=mape
    )


@app.route('/insights')
def insights():
    return render_template('insights.html')


if __name__ == '__main__':
    app.run(debug=True)
