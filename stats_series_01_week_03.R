# Snippet 1
data <- c(4, 8, 6, 5, 3, 2, 8, 9, 2, 5)

# Mean
mean <- mean(data)

# Median
median <- median(data)

# Mode
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
mode <- getmode(data)

# Snippet 2
# Range
data_range <- max(data) - min(data)

# Interquartile Range
IQR <- IQR(data)

# Variance
variance <- var(data)

# Standard Deviation
std_dev <- sd(data)

# Snippet 3
# Histogram
hist(data, breaks=5)

# Boxplot
boxplot(data)

# Snippet 4
# Generating normally distributed data
mu <- 0
sigma <- 0.1
normal_dist_data <- rnorm(1000, mean=mu, sd=sigma)

# Plotting the histogram of the data
hist(normal_dist_data, breaks=30)
