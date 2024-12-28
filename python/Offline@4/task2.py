import numpy as np
import matplotlib.pyplot as plt

import time

#DFT implememtation

def DFT(x):
    n=len(x)
    X=np.zeros(n,dtype=complex)
    for k in range(n):
        X[k]= sum(x[j]*np.exp(-2j*k*j/n) for j in range(n))
    return X


#IDFT implementation

def IDFT(x):
    n=len(x)
    X=np.zeros(n,dtype=complex)
    for k in range(n):
        X[k]= sum(x[j]*np.exp(2j*np.pi*k*j/n) for j in range(n)) / n
        
    return X


#FFT imple1mentation

def FFT(x):
    n=len(x)
    if n<=1:
        return x
    else:
        #splitting the signal into even and odd parts
        even = FFT(x[::2])
        odd = FFT(x[1::2])
        
        factor = np.exp(-2j*np.pi*np.arange(n)/n)
        
        return np.concatenate([even+factor[:n//2]*odd,even-factor[n//2:]*odd])
    
    
    
    
#IFFT implementation

def IFFT(x):
    n=len(x)
    if n<=1:
        return x
    else:
        #splitting the signal into even and odd parts
        even = IFFT(x[::2])
        odd = IFFT(x[1::2])
        
        factor = np.exp(2j*np.pi*np.arange(n)/n)
        
        return np.concatenate([even+factor[:n//2]*odd,even-factor[n//2:]*odd])
    
    
    
    
#runtime calculation

def measure_runtime(func,x,iterations=10):
    runtimes=[]
    
    for _ in range(iterations):
        start_time=time.perf_counter()
        func(x)
        end_time=time.perf_counter()
        runtimes.append(end_time-start_time)
        
    return np.mean(runtimes)

input_sizes=[2**k for k in range(2,9)]
dft_times,fft_times,idft_times,ifft_times=[],[],[],[]


#generate random signal to measure runtime
for n in input_sizes:
    signal=np.random.random(n)
    
    #measure the runtime for DFT and FFT
    dft_times.append(measure_runtime(DFT,signal))
    fft_times.append(measure_runtime(FFT,signal))
    
    freq_dft=DFT(signal)
    freq_fft=FFT(signal)
    
    #measure the runtime for IDFT and IFFT
    idft_times.append(measure_runtime(IDFT,freq_dft))
    
    ifft_times.append(measure_runtime(IFFT,freq_fft))
    
    #plot the runtime
    
plt.plot(input_sizes, dft_times, 'o-', label='DFT', color='blue')
plt.plot(input_sizes, fft_times, 'o-', label='FFT', color='orange')
plt.plot(input_sizes, idft_times, 'o-', label='IDFT', color='green')
plt.plot(input_sizes, ifft_times, 'o-', label='IFFT', color='red')

plt.xlabel('Input Size (n)')
plt.ylabel('Average Runtime (seconds)')
plt.title('Runtime Comparison of DFT/FFT and IDFT/IFFT (Manual Implementation)')
plt.legend()
plt.grid(True)
plt.show()

     