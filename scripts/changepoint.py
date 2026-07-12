import ruptures as rpt

def detect_changes(series):

    algo = rpt.Pelt(model="rbf")

    result = algo.fit(series.values).predict(pen=10)

    return result