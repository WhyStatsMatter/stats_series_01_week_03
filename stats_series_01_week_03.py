# Snippet 1
import statistics

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

# Mean
mean = statistics.mean(data)

# Median
median = statistics.median(data)

# Mode
mode = statistics.mode(data)

# Snippet 2
# Range
data_range = max(data) - min(data)

# Interquartile Range
from scipy import stats
IQR = stats.iqr(data)

# Variance
variance = statistics.variance(data)

# Standard Deviation
std_dev = statistics.stdev(data)

# Snippet 3
# Histogram
import matplotlib.pyplot as plt
plt.hist(data, bins=5)
plt.show()

# Boxplot
plt.boxplot(data)
plt.show()

# Snippet 4
# Generating normally distributed data
mu, sigma = 0, 0.1
normal_dist_data = np.random.normal(mu, sigma, 1000)

# Plotting the histogram of the data
plt.hist(normal_dist_data, bins=30)
plt.show()
