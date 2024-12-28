import numpy as np
import matplotlib.pyplot as plt


def parabolic_function(x):
    """Parabolic function y = x^2 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, x**2, 0)


def triangular_function(x):
    """Triangular wave with height 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, 1 - np.abs(x) / 2, 0)


def sawtooth_function(x):
    """Sawtooth wave with slope 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, (x + 2) / 2, 0)


def rectangular_function(x):
    """Rectangular pulse with height 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, 1, 0)


# Define the interval and function and generate appropriate x values and y values
x_values = np.linspace(-10, 10,num=1000)
y_values = np.where((x_values >= -2) & (x_values <= 2), x_values**2, 0)

# Plot the original function
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original y = x^2")
plt.title("Original Function (y = x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# Define the sampled times and frequencies
sampled_times = x_values
frequencies = 

# Fourier Transform 
def fourier_transform(signal, frequencies, sampled_times):
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)
    
    # Store the fourier transform results for each frequency. Handle the real and imaginary parts separately
    # use trapezoidal integration to calculate the real and imaginary parts of the FT
    for i,f in enumerate(frequencies):
        cosine_terms = np.cos(2 * np.pi * f * sampled_times)
        sine_terms = np.sin(2 * np.pi * f * sampled_times)
        ft_result_real[i] = np.trapz(signal * cosine_terms, sampled_times)
        ft_result_imag[i] = np.trapz(signal * sine_terms, sampled_times)

    return ft_result_real, ft_result_imag

# Apply FT to the sampled data
ft_data = fourier_transform(y_values, frequencies, sampled_times)
#  plot the FT data
plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.sqrt(ft_data[0]**2 + ft_data[1]**2))
plt.title("Frequency Spectrum of y = x^2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()


# Inverse Fourier Transform 
def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)
    # Reconstruct the signal by summing over all frequencies for each time in sampled_times.
    # use trapezoidal integration to calculate the real part
    # You have to return only the real part of the reconstructed signal
    for i, t in enumerate(sampled_times):
        cosine_terms = np.cos(2 * np.pi * frequencies * t)
        sine_terms = np.sin(2 * np.pi * frequencies * t)
        reconstructed_signal[i] = np.trapz(ft_signal[0] * cosine_terms - ft_signal[1] * sine_terms, frequencies)
    
    return reconstructed_signal

# Reconstruct the signal from the FT data
reconstructed_y_values = inverse_fourier_transform(ft_data, frequencies, sampled_times)
# Plot the original and reconstructed functions for comparison
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original y = x^2", color="blue")
plt.plot(sampled_times, reconstructed_y_values, label="Reconstructed y = x^2", color="red", linestyle="--")
plt.title("Original vs Reconstructed Function (y = x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
