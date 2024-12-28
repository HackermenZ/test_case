# # import numpy as np
# # import matplotlib.pyplot as plt
# # import time

# # # Function to generate random discrete signals
# # def generate_random_signal(n):
# #     return np.random.rand(n)

# # # Function to compute DFT
# # def DFT(signal):
# #     N = len(signal)
# #     X = np.zeros(N, dtype=complex)
# #     for k in range(N):
# #         X[k] = sum(signal[n] * np.exp(-1j * 2 * np.pi * k * n / N) for n in range(N))
# #     return X

# # # Function to compute IDFT
# # def IDFT(X):
# #     N = len(X)
# #     x = np.zeros(N, dtype=complex)
# #     for n in range(N):
# #         x[n] = sum(X[k] * np.exp(1j * 2 * np.pi * k * n / N) for k in range(N)) / N
# #     return x

# # # Function to compute FFT using Cooley-Tukey Algorithm
# # def FFT(signal):
# #     N = len(signal)
# #     if N <= 1:
# #         return signal
# #     even = FFT(signal[::2])
# #     odd = FFT(signal[1::2])
# #     terms = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
# #     return np.concatenate([even + terms, even - terms])

# # # Function to compute IFFT using FFT
# # def IFFT(X):
# #     N = len(X)
# #     X_conj = np.conj(X)
# #     x = FFT(X_conj)
# #     return np.conj(x) / N

# # # Function to measure runtime of a function
# # def measure_runtime(func, *args, runs=10):
# #     runtimes = []
# #     for _ in range(runs):
# #         start_time = time.time()
# #         func(*args)
# #         runtimes.append(time.time() - start_time)
# #     return np.mean(runtimes)

# # # Main function
# # def main():
# #     # Input sizes (powers of 2)
# #     input_sizes = [2**k for k in range(2, 8)]  # n = 4, 8, 16, ..., 128
# #     dft_times = []
# #     idft_times = []
# #     fft_times = []
# #     ifft_times = []

# #     for n in input_sizes:
# #         signal = generate_random_signal(n)

# #         # Measure runtimes for DFT and IDFT
# #         dft_time = measure_runtime(DFT, signal)
# #         idft_time = measure_runtime(IDFT, DFT(signal))
# #         dft_times.append(dft_time)
# #         idft_times.append(idft_time)

# #         # Measure runtimes for FFT and IFFT
# #         fft_time = measure_runtime(FFT, signal)
# #         ifft_time = measure_runtime(IFFT, FFT(signal))
# #         fft_times.append(fft_time)
# #         ifft_times.append(ifft_time)

# #     # Plot runtime comparison
# #     plt.figure(figsize=(10, 6))
# #     plt.plot(input_sizes, dft_times, 'o-', label='DFT', color='blue')
# #     plt.plot(input_sizes, fft_times, 'o-', label='FFT', color='orange')
# #     plt.plot(input_sizes, idft_times, 'o-', label='IDFT', color='green')
# #     plt.plot(input_sizes, ifft_times, 'o-', label='IFFT', color='red')
# #     plt.xlabel('Input Size (n)')
# #     plt.ylabel('Average Runtime (seconds)')
# #     plt.title('Runtime Comparison of DFT/FFT and IDFT/IFFT')
# #     plt.legend()
# #     plt.grid(True)
# #     plt.show()

# # if __name__ == "__main__":
# #     main()
# import numpy as np
# import matplotlib.pyplot as plt
# import time

# def dft(x):
#     """Compute the Discrete Fourier Transform (DFT) of a 1D array."""
#     N = len(x)
#     X = np.zeros(N, dtype=complex)
#     for k in range(N):
#         for n in range(N):
#             X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
#     return X

# def idft(X):
#     """Compute the Inverse Discrete Fourier Transform (IDFT) of a 1D array."""
#     N = len(X)
#     x = np.zeros(N, dtype=complex)
#     for n in range(N):
#         for k in range(N):
#             x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
#     return x / N

# def fft(x):
#     """Compute the Fast Fourier Transform (FFT) using the Cooley-Tukey algorithm."""
#     N = len(x)
#     if N <= 1:
#         return x
#     even = fft(x[::2])
#     odd = fft(x[1::2])
#     T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
#     return np.concatenate([even + T, even - T])

# def ifft(X):
#     """Compute the Inverse FFT."""
#     N = len(X)
#     if N <= 1:
#         return X
#     even = ifft(X[::2])
#     odd = ifft(X[1::2])
#     T = [np.exp(2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
#     return (np.concatenate([even + T, even - T]) / 2)

# # Input sizes
# sizes = [2**i for i in range(2, 8)]  # 4, 8, 16, 32, 64, 128
# dft_times, fft_times = [], []
# idft_times, ifft_times = [], []

# # Generate random signals and measure runtimes
# for N in sizes:
#     x = np.random.rand(N)
    
#     # Measure DFT
#     start = time.time()
#     for _ in range(10):
#         dft(x)
#     dft_times.append((time.time() - start) / 10)
    
#     # Measure IDFT
#     X = dft(x)
#     start = time.time()
#     for _ in range(10):
#         idft(X)
#     idft_times.append((time.time() - start) / 10)
    
#     # Measure FFT
#     start = time.time()
#     for _ in range(10):
#         fft(x)
#     fft_times.append((time.time() - start) / 10)
    
#     # Measure IFFT
#     X = fft(x)
#     start = time.time()
#     for _ in range(10):
#         ifft(X)
#     ifft_times.append((time.time() - start) / 10)

# # Plotting
# plt.figure(figsize=(10, 5))
# plt.plot(sizes, dft_times, 'o-', label="DFT")
# plt.plot(sizes, fft_times, 'o-', label="FFT")
# plt.plot(sizes, idft_times, 'o-', label="IDFT")
# plt.plot(sizes, ifft_times, 'o-', label="IFFT")
# plt.xlabel("Input Size (n)")
# plt.ylabel("Average Runtime (seconds)")
# plt.title("Runtime Comparison of DFT/FFT and IDFT/IFFT")
# plt.legend()
# plt.grid()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import time

# # DFT Implementation
# def dft(x):
#     n = len(x)
#     X = np.zeros(n, dtype=complex)
#     for k in range(n):
#         for j in range(n):
#             X[k] += x[j] * np.exp(-2j * np.pi * k * j / n)
#     return X

# # IDFT Implementation
# def idft(X):
#     n = len(X)
#     x = np.zeros(n, dtype=complex)
#     for k in range(n):
#         for j in range(n):
#             x[k] += X[j] * np.exp(2j * np.pi * k * j / n)
#     return x / n

# # FFT and IFFT using numpy
# def fft(x):
#     return np.fft.fft(x)

# def ifft(X):
#     return np.fft.ifft(X)

# # Function to measure runtime
# def measure_runtime(func, x, iterations=10):
#     runtimes = []
#     for _ in range(iterations):
#         start_time = time.perf_counter()
#         func(x)
#         end_time = time.perf_counter()
#         runtimes.append(end_time - start_time)
#     return np.mean(runtimes)

# # Input sizes (powers of 2)
# input_sizes = [2**k for k in range(2, 8)]  # From 4 to 128
# dft_times = []
# fft_times = []
# idft_times = []
# ifft_times = []

# # Generate random signals and measure runtimes
# for n in input_sizes:
#     signal = np.random.random(n)  # Random discrete signal
    
#     dft_times.append(measure_runtime(dft, signal))
#     fft_times.append(measure_runtime(fft, signal))
    
#     freq_dft = dft(signal)
#     freq_fft = fft(signal)
    
#     idft_times.append(measure_runtime(idft, freq_dft))
#     ifft_times.append(measure_runtime(ifft, freq_fft))

# # Plotting the results
# plt.figure(figsize=(10, 6))
# plt.plot(input_sizes, dft_times, label="DFT", marker='o')
# plt.plot(input_sizes, fft_times, label="FFT", marker='o')
# plt.plot(input_sizes, idft_times, label="IDFT", marker='o')
# plt.plot(input_sizes, ifft_times, label="IFFT", marker='o')

# plt.title("Runtime Comparison of DFT/FFT and IDFT/IFFT")
# plt.xlabel("Input Size (n)")
# plt.ylabel("Average Runtime (seconds)")
# plt.legend()
# plt.grid(True)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import time

# DFT Implementation (brute force)
def dft(x):
    n = len(x)
    X = np.zeros(n, dtype=complex)
    for k in range(n):
        for j in range(n):
            X[k] += x[j] * np.exp(-2j * np.pi * k * j / n)
    return X

# IDFT Implementation (brute force)
def idft(X):
    n = len(X)
    x = np.zeros(n, dtype=complex)
    for k in range(n):
        for j in range(n):
            x[k] += X[j] * np.exp(2j * np.pi * k * j / n)
    return x / n

# FFT Implementation (Cooley-Tukey recursive FFT)
def fft(x):
    n = len(x)
    if n <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(n) / n)
    return np.concatenate([even + factor[:n//2] * odd, even + factor[n//2:] * odd])

# IFFT Implementation (Inverse FFT using the same Cooley-Tukey algorithm)
def ifft(X):
    n = len(X)
    if n <= 1:
        return X
    even = ifft(X[0::2])
    odd = ifft(X[1::2])
    factor = np.exp(2j * np.pi * np.arange(n) / n)
    return np.concatenate([even + factor[:n//2] * odd, even + factor[n//2:] * odd]) / n

# Function to measure runtime
def measure_runtime(func, x, iterations=10):
    runtimes = []
    for _ in range(iterations):
        start_time = time.perf_counter()
        func(x)
        end_time = time.perf_counter()
        runtimes.append(end_time - start_time)
    return np.mean(runtimes)

# Input sizes (powers of 2)
input_sizes = [2**k for k in range(2, 8)]  # From 4 to 128
dft_times = []
fft_times = []
idft_times = []
ifft_times = []

# Generate random signals and measure runtimes
for n in input_sizes:
    signal = np.random.random(n)  # Random discrete signal
    
    # Measure runtime of DFT and FFT
    dft_times.append(measure_runtime(dft, signal))
    fft_times.append(measure_runtime(fft, signal))
    
    # Apply DFT and FFT to get frequency-domain signals
    freq_dft = dft(signal)
    freq_fft = fft(signal)
    
    # Measure runtime of IDFT and IFFT
    idft_times.append(measure_runtime(idft, freq_dft))
    ifft_times.append(measure_runtime(ifft, freq_fft))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, dft_times, label="DFT", marker='o', linestyle='-', color='b')
plt.plot(input_sizes, fft_times, label="FFT", marker='o', linestyle='-', color='g')
plt.plot(input_sizes, idft_times, label="IDFT", marker='o', linestyle='-', color='r')
plt.plot(input_sizes, ifft_times, label="IFFT", marker='o', linestyle='-', color='purple')

plt.title("Runtime Comparison of DFT/FFT and IDFT/IFFT (Manual Implementation)")
plt.xlabel("Input Size (n)")
plt.ylabel("Average Runtime (seconds)")
plt.legend()
plt.grid(True)
plt.show()
