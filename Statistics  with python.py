##using matplotlib in statistics with 1D Data 
          
                               # mean and plot them 

import matplotlib.pyplot as plt
import math
data = [1,3,5,11,7,8,4,13,9,10,10]
data2 = [12,34,1,3,5,6,34,76,2,5,6]
def mean(d):   # function to get the mean of any data 
    sum=0
    for i in d:
        sum=sum+i
    return sum/len(d)
m = mean(data)

                          # calculating variance and standard deviation 
def sd(d):
    m = mean(d)
    variance = 0
    for i in d:
        variance += (i-m)**2 /(len(d))
    return   math.sqrt(variance)

