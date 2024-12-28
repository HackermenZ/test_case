import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Step 1: Load the audio file
sample_rate, data = wavfile.read('buzzjc.wav')
data = data / np.max(np.abs(data))  # Normalize to -1 to 1

# If stereo, convert to mono by averaging channels
if len(data.shape) > 1:
    data = data.mean(axis=1)

# Plot the original audio signal in the time domain
plt.figure(figsize=(12, 4))
time = np.linspace(0, len(data) / sample_rate, num=len(data))
plt.plot(time, data)
plt.title("Original Audio Signal (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# Step 2: Define parameters for Fourier Transform
interval_step = 1  # Sampling interval step
data_sampled = data[::interval_step]
max_time = len(data_sampled) / (sample_rate / interval_step)
sampled_times = np.linspace(0, max_time, num=len(data_sampled))
max_freq = sample_rate / (2 * interval_step)
frequencies = np.linspace(0, max_freq,num=len(data_sampled))

# Fourier Transform function
def fourier_transform(signal, frequencies, sampled_times):
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)
    dt = sampled_times[1] - sampled_times[0]  # Calculate uniform time step

    for i, f in enumerate(frequencies):
        cosine_terms = np.cos(2 * np.pi * f * sampled_times)
        sine_terms = np.sin(2 * np.pi * f * sampled_times)
        # ft_result_real[i] = np.trapz(signal * cosine_terms, dx=dt)
        # ft_result_imag[i] = np.trapz(signal * sine_terms, sampled_times,dx=dt)
        ft_result_real[i] = np.trapz(signal * cosine_terms, dx=dt)
        ft_result_imag[i] = np.trapz(signal * sine_terms, dx=dt)

    return ft_result_real, ft_result_imag



# def fourier_transform(signal, frequencies, sampled_times):
#     num_freqs = len(frequencies)
#     ft_result_real = np.zeros(num_freqs)
#     ft_result_imag = np.zeros(num_freqs)
#
#     for i, f in enumerate(frequencies):
#         cosine_terms = np.cos(2 * np.pi * f * sampled_times)
#         sine_terms = np.sin(2 * np.pi * f * sampled_times)
#         ft_result_real[i] = np.trapezoid(signal * cosine_terms, sampled_times)
#         ft_result_imag[i] = np.trapezoid(signal * sine_terms, sampled_times)
#
#     return ft_result_real, ft_result_imag

# Apply Fourier Transform
ft_data = fourier_transform(data_sampled, frequencies, sampled_times)

# Plot the frequency spectrum
magnitude_spectrum = np.sqrt(ft_data[0]**2 + ft_data[1]**2)
plt.figure(figsize=(12, 6))
plt.plot(frequencies, magnitude_spectrum)
plt.title("Frequency Spectrum of the Audio Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

# Step 3: Identify and remove unwanted frequencies
filtered_ft_data = np.zeros_like(ft_data)

filtered_ft_data[0] = ft_data[0].copy()
filtered_ft_data[1] = ft_data[1].copy()

# Define a threshold to remove specific frequencies
threshold = 0.1 * np.max(magnitude_spectrum)  # Example threshold: 10% of max magnitude
# for i, magnitude in enumerate(magnitude_spectrum):
#     if magnitude > threshold and 500 < frequencies[i] < 1500:  # Adjust frequency range
#         filtered_ft_data[0][i] = 0
#         filtered_ft_data[1][i] = 0


filtered_ft_data[0][frequencies < 900] = 0  # Remove frequencies below 1000 Hz
filtered_ft_data[1][frequencies < 900] = 0



# Plot the filtered frequency spectrum
plt.figure(figsize=(12, 6))
filtered_magnitude_spectrum = np.sqrt(filtered_ft_data[0]**2 + filtered_ft_data[1]**2)
plt.plot(frequencies, filtered_magnitude_spectrum)
plt.title("Filtered Frequency Spectrum (Unwanted Frequencies Removed)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

# Step 4: Apply Inverse Fourier Transform
def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
    ft_real, ft_imag = ft_signal
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)
    df = frequencies[1] - frequencies[0]  # Calculate uniform frequency step

    for i, t in enumerate(sampled_times):
        # cosine_terms = np.trapz(ft_real*np.cos(2 * np.pi * frequencies * t),dx=df)
        # sine_terms = np.trapz(ft_imag*np.sin(2 * np.pi * frequencies * t),dx=df)
        # reconstructed_signal[i] = cosine_terms+sine_terms
        real_part = np.trapz(ft_real * np.cos(2 * np.pi * frequencies * t), dx=df)
        imag_part = np.trapz(ft_imag * np.sin(2 * np.pi * frequencies * t), dx=df)
        reconstructed_signal[i] = real_part + imag_part
    return reconstructed_signal



# def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
#     ft_real, ft_imag = ft_signal
#     n = len(sampled_times)
#     reconstructed_signal = np.zeros(n)
#
#     for i, t in enumerate(sampled_times):
#         cosine_terms = np.cos(2 * np.pi * frequencies * t)
#         sine_terms = np.sin(2 * np.pi * frequencies * t)
#         reconstructed_signal[i] = np.trapezoid(ft_real * cosine_terms + ft_imag * sine_terms, frequencies)
#
#     return reconstructed_signal


# Reconstruct the signal
filtered_data = inverse_fourier_transform(filtered_ft_data, frequencies, sampled_times)

# Plot the reconstructed (denoised) signal
plt.figure(figsize=(12, 4))
plt.plot(sampled_times, filtered_data.real)  # Take only the real part
plt.title("Reconstructed (Denoised) Audio Signal (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# Normalize and save the denoised audio
filtered_data_normalized = np.int16(filtered_data.real / np.max(np.abs(filtered_data.real)) * 32767)
wavfile.write('denoised_audio.wav', sample_rate, filtered_data_normalized)

print("Denoised audio saved as 'denoised_audio.wav'")