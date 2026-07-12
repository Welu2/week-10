import numpy as np
import ruptures as rpt

def detect_changes(series, model="rbf", penalty=10):
    """
    Detect structural change points in a time series.

    Parameters
    ----------
    series : pandas.Series or numpy.ndarray
        Input time series.
    model : str
        Ruptures cost model.
    penalty : int or float
        Penalty value controlling the number of change points.

    Returns
    -------
    list
        Indices of detected change points.
    """

    # Convert to numpy array
    signal = np.asarray(series)

    algo = rpt.Pelt(model=model)

    result = algo.fit(signal).predict(pen=penalty)

    return result