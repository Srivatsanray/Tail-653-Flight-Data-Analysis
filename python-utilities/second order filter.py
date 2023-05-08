from scipy import signal
# Create a low-pass filter with a cutoff frequency of 100 Hz
b, a = signal.butter(2, 2. /4, 'low', fs=25)

# Apply the filter to the signal
y_ALTR = signal.lfilter(b, a, y)
