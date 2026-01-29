import matplotlib
matplotlib.use("Agg")  # IMPORTANT FIX

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

def train_and_forecast(data, steps=6):
    model = ARIMA(data['sales'], order=(1, 1, 1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=steps)

    fitted_values = model_fit.fittedvalues
    actual = data['sales'].iloc[1:]
    predicted = fitted_values.iloc[1:]

    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100

    return forecast, round(rmse, 2), round(mape, 2)
