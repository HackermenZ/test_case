import numpy as np
import matplotlib.pyplot as plt


# Define the functions
def parabolic_function(x):
    """Parabolic function y = x^2 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, x ** 2, 0)


def triangular_function(x):
    """Triangular wave with height 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, 1 - np.abs(x) / 2, 0)


def sawtooth_function(x):
    """Sawtooth wave with slope 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, (x + 2) , 0)


def rectangular_function(x):
    """Rectangular pulse with height 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, 1, 0)


# Fourier Transform
def fourier_transform(signal, frequencies, sampled_times):
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)

    for i, f in enumerate(frequencies):
        cosine_terms = np.cos(2 * np.pi * f * sampled_times)
        sine_terms = np.sin(2 * np.pi * f * sampled_times)
        ft_result_real[i] = np.trapz(signal * cosine_terms, sampled_times)
        ft_result_imag[i] = np.trapz(signal * sine_terms, sampled_times)

    return ft_result_real, ft_result_imag


# Inverse Fourier Transform
def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
    ft_real, ft_imag = ft_signal
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)

    for i, t in enumerate(sampled_times):
        cosine_terms = np.cos(2 * np.pi * frequencies * t)
        sine_terms = np.sin(2 * np.pi * frequencies * t)
        reconstructed_signal[i] = np.trapz(ft_real * cosine_terms + ft_imag * sine_terms, frequencies)

    return reconstructed_signal


# Visualize each function
def process_and_visualize(function, function_name):
    # Define x values and evaluate the function
    x_values = np.linspace(-10, 10, num=1000)
    y_values = function(x_values)

    # Plot the original function
    plt.figure(figsize=(12, 4))
    plt.plot(x_values, y_values, label=f"Original {function_name}")
    plt.title(f"Original Function ({function_name})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

    # Define sampled times and frequency range
    sampled_times = x_values
    frequencies = np.linspace(-1, 1, num=500)  # Adjust frequency range as needed

    # Apply Fourier Transform
    ft_data = fourier_transform(y_values, frequencies, sampled_times)

    # Plot the frequency spectrum
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, np.sqrt(ft_data[0] ** 2 + ft_data[1] ** 2))
    plt.title(f"Frequency Spectrum ({function_name})")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()

    # Reconstruct the signal using Inverse Fourier Transform
    reconstructed_y_values = inverse_fourier_transform(ft_data, frequencies, sampled_times)

    # Plot the original and reconstructed functions for comparison
    plt.figure(figsize=(12, 4))
    plt.plot(x_values, y_values, label=f"Original {function_name}", color="blue")
    plt.plot(sampled_times, reconstructed_y_values, label=f"Reconstructed {function_name}", color="red", linestyle="--")
    plt.title(f"Original vs Reconstructed Function ({function_name})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


# Process and visualize each function
functions = [
    (parabolic_function, "Parabolic Function"),
    (triangular_function, "Triangular Function"),
    (sawtooth_function, "Sawtooth Function"),
    (rectangular_function, "Rectangular Function")
]

for func, name in functions:
    process_and_visualize(func, name)