import numpy as np
from numpy.fft import fft
import scipy.signal as sig
import matplotlib.pyplot as plt


def re_fft(x):
    if x.shape[0] % 2 != 0:
        raise ValueError("An even number of samples is necessary!")
    if np.iscomplexobj(x):
        raise ValueError("The input signal needs to be real-valued!")
        
    M = x.shape[0]//2
        
    # Convert real-valued input signal array x
    # into complex-valued signal aray y with half the size
    # EITHER: Perform splitting OR: USE numpy view
    y = x.view(dtype=np.complex128)  # REPLACE y =  # TODO
    
    # fft of complex input signal
    Y = fft(y)  # REPLACE Y =  # TODO
    
    # Calculate Y_1 and Y_2
    # Note: Y[M] does not exist!
    # Idea: (Y[1] + Y*[M-1])/2 needs to be calculated, but simple
    # reversing results in (Y[1] + Y*[M-2])/2 => append Y[M] = Y[0] to Y
    Y = np.append(Y, Y[0])  # REPLACE Y =  # TODO
    Y_1 = (Y + Y[::-1].conj())/2  # REPLACE Y_1 =  # TODO
    Y_2 = (Y - Y[::-1].conj())/2j  # REPLACE Y_2 =  # TODO
    
    # Complete first half of X
    X = Y_1 + np.exp(-1j*np.pi*np.r_[0:M+1]/M) * Y_2  # REPLACE X = # TODO
    
    # for second half: X[M] is already set right
    # through prev. appending operation
    
    # Now X[M+1] = X[N/2 + 1] = X[N - (N/2-1)] = X*[N/2-1] = X*[M - 1]
    # and so on until X[N-1] = X*[1]
    # thus: [X[M-1], ..., X[1]].conj() = X[M-1:0:-1].conj()
    # to be appended, because index set is interval [Begin, End)
    # M-1 is in it, but 0 is excluded
    X = np.append(X, np.flipud(X[1:M]).conj())  # REPLACE X =  # TODO
    
    return X


# create sine as a test signal
N  = 2**10;
f = 1000;
fs= 8000;
Ts = 1/fs;

t = np.r_[0:N*Ts:Ts]
x = np.sin((2*np.pi*f)*t)

plt.plot(t[t < 0.02]*1000, x[t < 0.02]);
plt.xlim((0, 20))
plt.grid(True)
plt.xlabel(r'$t\ /\ \mathrm{ms}$')
plt.title("First 20 ms of signal x(t)",
          fontsize=14);



X_test = re_fft(x)