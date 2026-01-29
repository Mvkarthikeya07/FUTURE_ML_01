import pandas as pd

def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath)

    # Convert to datetime
    df['date'] = pd.to_datetime(df['date'])

    # 🔥 FIX: Aggregate duplicate dates (SUM for sales)
    df = df.groupby('date', as_index=False)['sales'].sum()

    # Set index
    df.set_index('date', inplace=True)

    # Set monthly frequency
    df = df.asfreq('MS')

    # Fill missing values (business-safe)
    df['sales'] = df['sales'].interpolate(method='linear')

    # Feature engineering
    df['month'] = df.index.month
    df['year'] = df.index.year

    return df
