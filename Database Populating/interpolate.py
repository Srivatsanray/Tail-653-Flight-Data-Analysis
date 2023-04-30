import numpy as np
from scipy.interpolate import interp1d


def interpolate(high_sampling_rate, y_low):

    # length of the data the column with low sampling rate has
    low_sampling_rate = len(y_low)
    # Time data points for low sampling rate
    t_low = np.linspace(0, 1, low_sampling_rate)

    f_interp = interp1d(t_low, y_low, kind='linear')
    # Time data points for low sampling rate
    t_interp = np.linspace(0, 1, high_sampling_rate)
    y_interp = f_interp(t_interp)

    return y_interp.flatten().tolist() # returns 2D array
