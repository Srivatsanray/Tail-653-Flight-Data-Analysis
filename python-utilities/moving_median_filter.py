def moving_median_filter(x, k):
    """Apply a moving median filter to the input signal x using a window of size k."""
    y = np.zeros_like(x)
    for i in range(len(x)):
        if i < k // 2 or i >= len(x) - k // 2:
            y[i] = x[i]
        else:
            y[i] = np.median(x[i - k // 2 : i + k // 2 + 1])
    return y
