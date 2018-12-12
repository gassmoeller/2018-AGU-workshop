import numpy as np

from .data_analysis import moving_average

def test_moving_average():
    avg = moving_average(np.ones(10),4)
    assert np.any(np.isnan(avg))
    assert np.allclose(avg[3],1.0)
    return
