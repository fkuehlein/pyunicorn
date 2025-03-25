import numpy as np
from numpy.typing import NDArray

class SlidingWindow():
    """
    A class to facilitate the sliding window analysis of timeseries

    # simple usecase

    example_slider = SlidingWindow(x, window_size=50, overlap=5)

    for i in range(example_slider.n_windows):
        example_slider.results[0, i] = RecurrenceNetwork(
            example_slider.window(i), recurrence_rate=0.05, silence_level=3
            ).determinism()

    plt.plot(example_slider.results[0,:])
    """
    def __init__(
            self,
            timeseries: NDArray,
            window_size: int,
            overlap: int,
            min_t: int = 0,
            max_t: int = -1,
            timings: NDArray = None,
            n_measures: int = 1
        ):
        """
        Initializes the sliding window object with the given parameters

        INPUT: timeseries - numpy array of the time series
               window_size - size of the window
               overlap - overlap between windows
               min_t - minimum time index to start sliding window
               max_t - maximum time index to stop sliding window
        """
        self.timeseries = timeseries
        self.window_size = window_size
        self.overlap = overlap
        if timings is not None:
            self.min_t = min(timings)
        else:
            self.min_t = min_t
        if timings is not None:
            self.max_t = max(timings)
        elif max_t == -1:
            self.max_t = len(self.timeseries)
        else:
            self.max_t = max_t
        self.timings = timings
        self.n_measures = n_measures

        # create array of windows
        self.win = np.arange(self.min_t, self.max_t - self.window_size, self.overlap)
        
        # calculate number of windows
        self.n_windows = len(self.win)

        # calculate window center
        self.window_center = np.zeros(self.n_windows, dtype=int)
        for i in range(self.n_windows):
            y = self.window_indices(i)
            if self.timings is not None:
                self.window_center[i] = (max(self.timings[y]) + min(self.timings[y]))/2
            else:
                self.window_center[i] = (max(y) + min(y))/2

        # create array for results
        self.results = np.zeros((self.n_measures, self.n_windows))

    def window_indices(self, i_win: int):
        """
        Returns indices of given window

        INPUT: i_win - index of the window to return
        """
        t_left = self.win[i_win]

        if self.timings is not None:
            y = np.where((self.timings > t_left) & (self.timings < t_left + self.window_size))[0]
        else:
            y = np.arange(t_left, t_left + self.window_size)

        return y

    def window(self, i_win: int):
        """
        Returns the windowed timeseries for the given index.

        INPUT: i_win - index of the window to return
        """
        return self.timeseries[self.window_indices(i_win)]

    def timing(self, i_win: int):
        """
        Returns the windowed timings for the given index.

        INPUT: i_win - index of the window to return
        """
        return self.timings[self.window_indices(i_win)]
