import numpy as np
import matplotlib.pyplot as plt

# Variance: The variance measures the deviation from the mean. It is the average
# value of the squared difference between observed values and the mean.


def my_variance(arr):
    my_mean = np.mean(arr)
    mean_diff = 0
    for a in arr:
        mean_diff = mean_diff + (a - my_mean)**2

    my_var = mean_diff/len(com_skills)
    return my_var
# standard deviation


def myStdDeviation(arr):
    return np.sqrt(my_variance(arr))


# data values
com_skills = np.array([40, 45, 23, 39, 39])
quant_skills = np.array([38, 41, 42, 48, 32])

# summation of elements of a data array


def arr_sum(arr):
    sum = 0
    #print("array length: ", len(com_skills))
    for a in arr:
        sum = sum + a
    return sum


my_mean = arr_sum(com_skills)/len(com_skills)
print("mean: ", my_mean)
print("inbuilt mean: ", np.mean(com_skills))  # arithmatic mean
print("mode: ", np.max(com_skills))  # mode of the data
print("median: ", np.median(com_skills))


# As we have seen, central tendency presents the middle value of a group of observations but
# does not provide the overall picture of an observation. Dispersion metrics measure the
# deviation in observations. The most popular dispersion metrics are range, interquartile
# range (IQR), variance, and standard deviation. These dispersion metrics value the
# variability in observations or the spread of observations.
# range.
com_range = np.max(com_skills) - np.min(com_skills)
print("Range: ", com_range)
print("my variance: ", my_variance(com_skills))
print("Numpy variance: ", np.var(com_skills))

# Standard deviation: This is the square root of the variance. Its unit is the same as
# for the original observations. This makes it easier for an analyst to evaluate the
# exact deviation from the mean. The lower value of standard deviation represents
# the lesser distance of observations from the mean; this means observations are
# less widely spread. The higher value of standard deviation represents a large
# distance of observations from the mean—that is, observations are widely spread.
print("standard deviation: ", myStdDeviation(com_skills))

# Covariance measures the relationship
# between a pair of variables. It shows the degree of change in the variables—that is, how the
# change in one variable affects the other variable. Its value ranges from -infinity to + infinity
print("Covariance: ", np.cov(com_skills, quant_skills))

# Correlation shows how variables are correlated with each other. Correlation offers a better
# understanding than covariance and is a normalized version of covariance. Correlation
# ranges from -1 to 1. A negative value represents the increase in one variable, causing a
# decrease in other variables or variables to move in the same direction. A positive value
# represents the increase in one variable, causing an increase in another variable, or a
# decrease in one variable causes decreases in another variable. A zero value means that there
# is no relationship between the variable or that variables are independent of each other.
print("correlation: ", np.correlate(com_skills, quant_skills, "full"))

plt.scatter(com_skills, quant_skills)
plt.show()
