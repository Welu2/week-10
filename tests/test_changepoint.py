import numpy as np

from scripts.changepoint import detect_changes

def test_cp():

    x=np.concatenate([

        np.random.normal(1,1,100),

        np.random.normal(8,1,100)

    ])

    cp=detect_changes(x)

    assert len(cp)>0