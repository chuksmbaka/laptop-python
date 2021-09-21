from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
##end of import 

sampleRate, data = wavfile.read("165150__rhythmpeople__rpeople-percussion4.wav")
print("Sound sample rate: ", sampleRate, "Hz")
print("Sound data: ", data) ##peint justt the data
dataLength = len(data) ##length of the whole data
print("Data length: ", dataLength, "Seconds")

##plot th raw data
##plt.plot(data)
##plt.show()

##try to plot the raw data as stem or discrete plot
#generate length of size dataLength 
discreteRange = (np.arange(0, 445621, 1)).tolist()
#print("Discrete data range: ", discreteRange)
print("discrete length: ", len(discreteRange))
print("discreteRange type: ", type(discreteRange))
#plt.stem(discreteRange, data, use_line_collection=False)
#plt.show()

##number of data points
N = 60

##zero padding
padding = [0] * N
#print("zero padding length: ", len(padding) )
#print("zero padding: ", padding)
#print("padding type: ", type(padding))


##cut out sections of data
data10 = data[:N].tolist() + padding
#data100 = data10 + padding
print("len data100: ", len(data10))
#print("data10: ", data10)
#print("data10 type: ", type(data10))

discreteRange10 = discreteRange[:N] + padding
print("len discret range: ", len(discreteRange10))
#print("sicret10: ", discreteRange10)
##plot cut out value
#plt.stem(discreteRange10, data10)
#plt.show()


##second signal
x = np.arange(0, N + len(padding), 1)
print("len x: ", len(x))
#y = np.exp(np.sin(x))
#plt.stem(discreteRange10, x)
#plt.show()

##rectangular window function
y = ([1] * N) + padding 
print("len y: ", len(y))

##convolution implementstion
M = N + len(padding)
output = [0] * M
for n in range(M):
    yy = [0] * M
    for m in range(len(yy)):
        yy[n] = yy[n] + data10[m] * y[n - m]
    output[n] = yy[n]


#print(output)
plt.stem(x, output)
plt.show()




