import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

high_sampling_rate = 100 # length of the data the column with high sampling rate has
t_high = np.linspace(0,1,high_sampling_rate) # Time data points for high sampling rate


low_sampling_rate = 10 # length of the data the column with low sampling rate has
t_low = np.linspace(0,1,low_sampling_rate) # Time data points for high sampling rate

f_interp = interp1d(t_low,OIT1,kind='linear') 
t_interp = np.linspace(0,1,high_sampling_rate)
y_intep = f_interp(t_interp) # Linear interpolation of the data

# Plotting all the three data
fig, ax = plt.subplots()
ax.plot(t_high, EGT1, label='High sampled data')
ax.plot(t_low, OIT1, 'o', label='Low sampled data')
ax.plot(t_interp, y_intep, label='Interpolated data')
ax.legend()
plt.show()
