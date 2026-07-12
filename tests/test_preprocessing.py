from scripts.preprocessing import clean_data
import pandas as pd

def test_clean():

    df=pd.DataFrame({
        "Date":["2020-01-01"],
        "Price":[50]
    })

    clean=clean_data(df)

    assert len(clean)==1