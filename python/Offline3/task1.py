# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Define the interval and function
# # x_values = np.linspace(-5, 5, 1000)  # Define a broader range for sampling
# # y_values = np.where(np.abs(x_values) <= 2, x_values**2, 0)  # Parabolic Function y = x^2 within [-2, 2], 0 elsewhere

# # # Plot the original function
# # plt.figure(figsize=(12, 4))
# # plt.plot(x_values, y_values, label="Original y = x^2")
# # plt.title("Original Function (y = x^2)")
# # plt.xlabel("x")
# # plt.ylabel("y")
# # plt.legend()
# # plt.show()

# # # Define sampled times and frequency range
# # sampled_times = x_values
# # frequencies = np.linspace(-10, 10, 500)  # Experiment with a range of frequencies

# # # Fourier Transform
# # def fourier_transform(signal, frequencies, sampled_times):
# #     num_freqs = len(frequencies)
# #     ft_result_real = np.zeros(num_freqs)
# #     ft_result_imag = np.zeros(num_freqs)
    
# #     for i, f in enumerate(frequencies):
# #         cosine_terms = np.cos(2 * np.pi * f * sampled_times)
# #         sine_terms = np.sin(2 * np.pi * f * sampled_times)
# #         ft_result_real[i] = np.trapz(signal * cosine_terms, sampled_times)
# #         ft_result_imag[i] = np.trapz(signal * sine_terms, sampled_times)
    
# #     return ft_result_real, ft_result_imag

# # # Apply FT to the sampled data
# # ft_data = fourier_transform(y_values, frequencies, sampled_times)

# # # Plot the frequency spectrum
# # plt.figure(figsize=(12, 6))
# # plt.plot(frequencies, np.sqrt(ft_data[0]**2 + ft_data[1]**2))
# # plt.title("Frequency Spectrum of y = x^2")
# # plt.xlabel("Frequency (Hz)")
# # plt.ylabel("Magnitude")
# # plt.grid(True)
# # plt.show()

# # # Inverse Fourier Transform
# # def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
# #     ft_real, ft_imag = ft_signal
# #     n = len(sampled_times)
# #     reconstructed_signal = np.zeros(n)
    
# #     for i, t in enumerate(sampled_times):
# #         cosine_terms = np.cos(2 * np.pi * frequencies * t)
# #         sine_terms = np.sin(2 * np.pi * frequencies * t)
# #         reconstructed_signal[i] = np.trapz(ft_real * cosine_terms - ft_imag * sine_terms, frequencies)
    
# #     return reconstructed_signal

# # # Reconstruct the signal from the FT data
# # reconstructed_y_values = inverse_fourier_transform(ft_data, frequencies, sampled_times)

# # # Plot the original and reconstructed functions for comparison
# # plt.figure(figsize=(12, 4))
# # plt.plot(x_values, y_values, label="Original y = x^2", color="blue")
# # plt.plot(sampled_times, reconstructed_y_values, label="Reconstructed y = x^2", color="red", linestyle="--")
# # plt.title("Original vs Reconstructed Function (y = x^2)")
# # plt.xlabel("x")
# # plt.ylabel("y")
# # plt.legend()
# # plt.grid(True)
# # plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# # Define the interval and functions
# x_values = np.linspace(-2, 2, 400)
# parabolic = np.where(np.abs(x_values) <= 2, x_values**2, 0)
# triangular = np.where(np.abs(x_values) <= 2, 1 - np.abs(x_values) / 2, 0)
# sawtooth = np.where(np.abs(x_values) <= 2, x_values, 0)
# rectangular = np.where(np.abs(x_values) <= 2, 1, 0)

# # Define the sampled times and frequencies
# sampled_times = x_values
# frequencies = np.linspace(-10, 10, 400)

# # Fourier Transform 
# def fourier_transform(signal, frequencies, sampled_times):
#     num_freqs = len(frequencies)
#     ft_result_real = np.zeros(num_freqs)
#     ft_result_imag = np.zeros(num_freqs)
    
#     for i, freq in enumerate(frequencies):
#         integrand_real = signal * np.cos(2 * np.pi * freq * sampled_times)
#         integrand_imag = signal * np.sin(2 * np.pi * freq * sampled_times)
#         ft_result_real[i] = np.trapz(integrand_real, sampled_times)
#         ft_result_imag[i] = np.trapz(integrand_imag, sampled_times)
    
#     return ft_result_real, ft_result_imag

# # Inverse Fourier Transform 
# def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
#     n = len(sampled_times)
#     reconstructed_signal = np.zeros(n)
    
#     for i, t in enumerate(sampled_times):
#         integrand_real = ft_signal[0] * np.cos(2 * np.pi * frequencies * t) - ft_signal[1] * np.sin(2 * np.pi * frequencies * t)
#         reconstructed_signal[i] = np.trapz(integrand_real, frequencies)
    
#     return reconstructed_signal

# # Function to plot results
# def plot_results(x_values, y_values, frequencies, ft_data, reconstructed_y_values, title):
#     plt.figure(figsize=(12, 4))
#     plt.plot(x_values, y_values, label="Original", color="blue")
#     plt.title(f"Original Function ({title})")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.legend()
#     plt.show()

#     plt.figure(figsize=(12, 6))
#     plt.plot(frequencies, np.sqrt(ft_data[0]**2 + ft_data[1]**2))
#     plt.title(f"Frequency Spectrum of {title}")
#     plt.xlabel("Frequency (Hz)")
#     plt.ylabel("Magnitude")
#     plt.show()

#     plt.figure(figsize=(12, 4))
#     plt.plot(x_values, y_values, label="Original", color="blue")
#     plt.plot(sampled_times, reconstructed_y_values, label="Reconstructed", color="red", linestyle="--")
#     plt.title(f"Original vs Reconstructed Function ({title})")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.legend()
#     plt.show()

# # Apply FT and IFT to each function and plot results
# functions = [("Parabolic", parabolic), ("Triangular", triangular), ("Sawtooth", sawtooth), ("Rectangular", rectangular)]
# for title, y_values in functions:
#     ft_data = fourier_transform(y_values, frequencies, sampled_times)
#     reconstructed_y_values = inverse_fourier_transform(ft_data, frequencies, sampled_times)
#     plot_results(x_values, y_values, frequencies, ft_data, reconstructed_y_values, title)
import numpy as np
import matplotlib.pyplot as plt
import os

# Create a folder to save the plots
output_folder = "graphs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the functions
def parabolic_function(x):
    """Parabolic function y = x^2 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, x ** 2, 0)


def triangular_function(x):
    """Triangular wave with height 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, 1 - np.abs(x) / 2, 0)


def sawtooth_function(x):
    """Sawtooth wave with slope 1 within [-2, 2], 0 elsewhere."""
    return np.where(np.abs(x) <= 2, (x + 2) / 2, 0)


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


# Visualize each function and save plots
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
    plt.savefig(f"{output_folder}/{function_name}_original.png")
    plt.close()

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
    plt.savefig(f"{output_folder}/{function_name}_spectrum.png")
    plt.close()

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
    plt.savefig(f"{output_folder}/{function_name}_reconstructed.png")
    plt.close()


# Process and visualize each function
functions = [
    (parabolic_function, "Parabolic Function"),
    (triangular_function, "Triangular Function"),
    (sawtooth_function, "Sawtooth Function"),
    (rectangular_function, "Rectangular Function")
]

for func, name in functions:
    process_and_visualize(func, name)

print(f"All plots have been saved in the '{output_folder}' folder.")