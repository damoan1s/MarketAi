import pandas as pd
import matplotlib.pyplot as plt

def basic_plot():
    # 1. Load CSV
    df = pd.read_csv("../../../data/example_data/ohlcv_sample.csv")

    # 2. Plot Close Price
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label='Close Price')

    # 3. Title & Labels
    plt.title("MarketAI – Day 7 Basic Chart")
    plt.xlabel("Index")
    plt.ylabel("Price")
    plt.legend()

    # 4. Show
    plt.show()

if __name__ == "__main__":
    basic_plot()
