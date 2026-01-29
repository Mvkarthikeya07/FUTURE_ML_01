import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2019-01-01", end="2024-12-31", freq="D")

stores = range(1, 11)        # 10 stores
products = range(1, 21)     # 20 products

data = []

for date in dates:
    for store in stores:
        for product in products:
            base_demand = 20 + product * 2
            trend = (date.year - 2019) * 2
            weekly_season = 5 * np.sin(2 * np.pi * date.dayofweek / 7)
            yearly_season = 10 * np.sin(2 * np.pi * date.dayofyear / 365)

            promotion = np.random.choice([0, 1], p=[0.8, 0.2])
            promo_effect = promotion * np.random.randint(10, 30)

            noise = np.random.normal(0, 5)

            sales = max(
                int(base_demand + trend + weekly_season + yearly_season + promo_effect + noise),
                0
            )

            price = np.random.uniform(100, 500)

            data.append([
                date,
                store,
                product,
                f"Category_{product % 5}",
                round(price, 2),
                promotion,
                sales
            ])

df = pd.DataFrame(data, columns=[
    "date", "store_id", "product_id",
    "category", "price", "promotion", "sales"
])

df.to_csv("data/huge_sales_data.csv", index=False)

print("✅ Huge dataset generated:", df.shape)
