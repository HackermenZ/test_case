# import numpy as np
# import matplotlib.pyplot as plt

# x_values = np.linspace(-10,10,1000)


# #y_values = 2*np.sin(14*np.pi*x_values)-np.sin(2*np.pi*x_values)(4*np.sin(2*np.pi*x_values)*np.sin(14*np.pi*x_values)-1)

# def function_t(x):
#     return 2*np.sin(14*np.pi*x)-np.sin(2*np.pi*x)(4*np.sin(2*np.pi*x)*np.sin(14*np.pi*x)-1)

# # plt.figure(figsize=(12,8))
# # plt.plot(x_values,y_values,label="Original Function")
# # plt.xlabel("x")
# # plt.ylabel("y")
# # plt.legend()
# # plt.show()



# def fourier_transform(signal, frequencies, sampled_times):
#     num_freqs = len(frequencies)
#     ft_result_real = np.zeros(num_freqs)
#     ft_result_imag = np.zeros(num_freqs)

#     for i, f in enumerate(frequencies):
#         cosine_terms = np.cos(2 * np.pi * f * sampled_times)
#         sine_terms = np.sin(2 * np.pi * f * sampled_times)
#         ft_result_real[i] = np.trapz(signal * cosine_terms, sampled_times)
#         ft_result_imag[i] = np.trapz(signal * sine_terms, sampled_times)

#     return ft_result_real, ft_result_imag



# def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
#     ft_real, ft_imag = ft_signal
#     n = len(sampled_times)
#     reconstructed_signal = np.zeros(n)

#     for i, t in enumerate(sampled_times):
#         cosine_terms = np.cos(2 * np.pi * frequencies * t)
#         sine_terms = np.sin(2 * np.pi * frequencies * t)
#         reconstructed_signal[i] = np.trapz(ft_real * cosine_terms + ft_imag * sine_terms, frequencies)

#     return reconstructed_signal



# def process_and_visualize(function, function_name):
#     # Define x values and evaluate the function
#     x_values = np.linspace(-10, 10, num=1000)
#     y_values = function(x_values)

#     # Plot the original function
#     plt.figure(figsize=(12, 4))
#     plt.plot(x_values, y_values, label=f"Original {function_name}")
#     plt.title(f"Original Function ({function_name})")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.legend()
#     plt.grid()
#     plt.show()

#     # Define sampled times and frequency range
#     sampled_times = x_values
#     frequencies = np.linspace(-1, 1, num=500)  # Adjust frequency range as needed

#     # Apply Fourier Transform
#     ft_data = fourier_transform(y_values, frequencies, sampled_times)

#     # Plot the frequency spectrum
#     plt.figure(figsize=(12, 6))
#     plt.plot(frequencies, np.sqrt(ft_data[0] ** 2 + ft_data[1] ** 2))
#     plt.title(f"Frequency Spectrum ({function_name})")
#     plt.xlabel("Frequency (Hz)")
#     plt.ylabel("Magnitude")
#     plt.grid()
#     plt.show()

#     # Reconstruct the signal using Inverse Fourier Transform
#     reconstructed_y_values = inverse_fourier_transform(ft_data, frequencies, sampled_times)

#     # Plot the original and reconstructed functions for comparison
#     plt.figure(figsize=(12, 4))
#     plt.plot(x_values, y_values, label=f"Original {function_name}", color="blue")
#     plt.plot(sampled_times, reconstructed_y_values, label=f"Reconstructed {function_name}", color="red", linestyle="--")
#     plt.title(f"Original vs Reconstructed Function ({function_name})")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.legend()
#     plt.grid()
#     plt.show()

# functions = [
#     (function_t, "Original Function"),
# ]

# for func, name in functions:
#     process_and_visualize(func, name)


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the original function f(t)
def function_t(x):
    return 2 * np.sin(14 * np.pi * x) - np.sin(2 * np.pi * x) * (4 * np.sin(2 * np.pi * x) * np.sin(14 * np.pi * x) - 1)

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

# Process and visualize
def process_and_visualize(function, function_name):
    # Define x values and evaluate the function
    x_values = np.linspace(-1, 1, num=1000)
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
    frequencies = np.linspace(-20, 20, num=500)  # Frequency range for Fourier Transform

    # Apply Fourier Transform
    ft_data = fourier_transform(y_values, frequencies, sampled_times)

    # Plot the frequency spectrum
    magnitude = np.sqrt(ft_data[0] ** 2 + ft_data[1] ** 2)
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, magnitude)
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

# Apply the process to the given function
process_and_visualize(function_t, "Function f(t)")