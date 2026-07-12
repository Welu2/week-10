import matplotlib.pyplot as plt

def plot_prices(df):

    plt.figure(figsize=(14,5))

    plt.plot(df["Date"],df["Price"])

    plt.title("Brent Oil Prices")

    plt.xlabel("Date")

    plt.ylabel("USD")

    plt.show()