from statsmodels.tsa.stattools import adfuller
from scipy.stats import linregress

def adf_test(series):

    result = adfuller(series)

    return {
        "ADF Statistic":result[0],
        "p-value":result[1]
    }



def trend(series):

    x=range(len(series))

    slope,_,_,_,_=linregress(x,series)

    return slope

def rolling_volatility(series):

    return series.rolling(30).std()