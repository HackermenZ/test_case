# import numpy as np
# import matplotlib.pyplot as plt

# # Constants
# n = 50  # Number of samples
# sampling_rate = 100  # Sampling rate (samples per second)
# wave_velocity = 8000  # Velocity in meters/second (e.g., P-wave)
# samples = np.arange(n)  # Sample indices

# # Function to generate signals
# def generate_signals(frequency=5):
#     noise_freqs = [15, 30, 45]
#     amplitudes = [0.5, 0.3, 0.1]
#     noise_freqs2 = [10, 20, 40]
#     amplitudes2 = [0.3, 0.2, 0.1]

#     dt = 1 / sampling_rate
#     time = samples * dt

#     # Original clean signal
#     original_signal = np.sin(2 * np.pi * frequency * time)

#     # Adding noise
#     noise_for_signal_A = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
#                              for noise_freq, amplitude in zip(noise_freqs, amplitudes))
#     noise_for_signal_B = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
#                              for noise_freq, amplitude in zip(noise_freqs2, amplitudes2))
#     signal_A = original_signal + noise_for_signal_A
#     noisy_signal_B = signal_A + noise_for_signal_B

#     # Applying random shift to signal B
#     shift_samples = np.random.randint(-n // 2, n // 2)
#     signal_B = np.roll(noisy_signal_B, shift_samples)

#     return signal_A, signal_B

# # Function to compute DFT
# def DFT(signal):
#     N = len(signal)
#     X = np.zeros(N, dtype=complex)
#     for k in range(N):
#         X[k] = sum(signal[n] * np.exp(-1j * 2 * np.pi * k * n / N) for n in range(N))
#     return X

# # Function to compute cross-correlation
# # def cross_correlation(signal_A, signal_B):
# #     X_A = DFT(signal_A)
# #     X_B = DFT(signal_B)
# #     cross_corr = np.real(np.fft.ifft(X_A * np.conj(X_B)))
# #     return cross_corr


# # Function to compute cross-correlation
# def cross_correlation(signal_A, signal_B):
#     X_A = DFT(signal_A)
#     X_B = DFT(signal_B)
#     X_corr = X_A * np.conj(X_B)  # Use conjugate multiplication in the frequency domain
#     cross_corr = np.real(IDFT(X_corr))  # Compute IDFT to get cross-correlation in the time domain
#     return cross_corr

# # Main function
# def main():
#     # Generate signals
#     signal_A, signal_B = generate_signals()

#     # Frequency spectra
#     X_A = DFT(signal_A)
#     X_B = DFT(signal_B)

#     # Cross-correlation
#     cross_corr = cross_correlation(signal_A, signal_B)

#     # Plot Signal A
#     plt.figure()
#     plt.stem(samples, signal_A, linefmt='b-', markerfmt='bo', basefmt=" ")
#     plt.title('Signal A (Station A)')
#     plt.xlabel('Sample Index')
#     plt.ylabel('Amplitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Frequency Spectrum of Signal A
#     plt.figure()
#     plt.stem(np.arange(len(X_A)), np.abs(X_A), linefmt='b-', markerfmt='bo', basefmt=" ")
#     plt.title('Frequency Spectrum of Signal A')
#     plt.xlabel('Frequency Index')
#     plt.ylabel('Magnitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Signal B
#     plt.figure()
#     plt.stem(samples, signal_B, linefmt='r-', markerfmt='ro', basefmt=" ")
#     plt.title('Signal B (Station B)')
#     plt.xlabel('Sample Index')
#     plt.ylabel('Amplitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Frequency Spectrum of Signal B
#     plt.figure()
#     plt.stem(np.arange(len(X_B)), np.abs(X_B), linefmt='r-', markerfmt='ro', basefmt=" ")
#     plt.title('Frequency Spectrum of Signal B')
#     plt.xlabel('Frequency Index')
#     plt.ylabel('Magnitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Cross-Correlation
#     plt.figure()
#     plt.stem(np.arange(len(cross_corr)), cross_corr, linefmt='g-', markerfmt='go', basefmt=" ")
#     plt.title('DFT-based Cross-Correlation')
#     plt.xlabel('Lag (samples)')
#     plt.ylabel('Correlation')
#     plt.grid(True)
#     plt.show()

# if __name__ == "__main__":
#     main()

# import numpy as np
# import matplotlib.pyplot as plt

# # Constants
# n = 50  # Number of samples
# sampling_rate = 100  # Sampling rate (samples per second)
# wave_velocity = 8000  # Velocity in meters/second (e.g., P-wave)
# samples = np.arange(n)  # Sample indices

# # Function to generate signals
# def generate_signals(frequency=5):
#     noise_freqs = [15, 30, 45]
#     amplitudes = [0.5, 0.3, 0.1]
#     noise_freqs2 = [10, 20, 40]
#     amplitudes2 = [0.3, 0.2, 0.1]

#     dt = 1 / sampling_rate
#     time = samples * dt

#     # Original clean signal
#     original_signal = np.sin(2 * np.pi * frequency * time)

#     # Adding noise
#     noise_for_signal_A = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
#                              for noise_freq, amplitude in zip(noise_freqs, amplitudes))
#     noise_for_signal_B = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
#                              for noise_freq, amplitude in zip(noise_freqs2, amplitudes2))
#     signal_A = original_signal + noise_for_signal_A
#     noisy_signal_B = signal_A + noise_for_signal_B

#     # Applying random shift to signal B
#     shift_samples = np.random.randint(-n // 2, n // 2)
#     signal_B = np.roll(noisy_signal_B, shift_samples)

#     return signal_A, signal_B, shift_samples

# # Function to compute DFT
# def DFT(signal):
#     N = len(signal)
#     X = np.zeros(N, dtype=complex)
#     for k in range(N):
#         X[k] = sum(signal[n] * np.exp(-1j * 2 * np.pi * k * n / N) for n in range(N))
#     return X

# # Function to compute IDFT
# def IDFT(X):
#     N = len(X)
#     x = np.zeros(N, dtype=complex)
#     for n in range(N):
#         x[n] = sum(X[k] * np.exp(1j * 2 * np.pi * k * n / N) for k in range(N)) / N
#     return x

# # Function to compute cross-correlation using DFT and IDFT
# def cross_correlation(signal_A, signal_B):
#     X_A = DFT(signal_A)
#     X_B = DFT(signal_B)
#     X_corr = X_A * np.conj(X_B)  # Use conjugate multiplication in the frequency domain
#     cross_corr = np.real(IDFT(X_corr))  # Compute IDFT to get cross-correlation in the time domain
#     return cross_corr

# # Function to calculate distance
# def calculate_distance(sample_lag, sampling_rate, wave_velocity):
#     time_lag = abs(sample_lag) / sampling_rate
#     distance = time_lag * wave_velocity
#     return distance

# # Main function
# def main():
#     # Generate signals
#     signal_A, signal_B, shift_samples = generate_signals()

#     # Frequency spectra
#     X_A = DFT(signal_A)
#     X_B = DFT(signal_B)

#     # Cross-correlation
#     cross_corr = cross_correlation(signal_A, signal_B)

#     # Find sample lag
#     sample_lag = np.argmax(np.fft.fftshift(cross_corr)) - (n // 2)

#     # Calculate distance
#     time_lag = abs(sample_lag) / sampling_rate
#     distance = time_lag * wave_velocity

#     # Print Results
#     print(f"Actual Shift: {shift_samples}")
#     print(f"Detected Sample Lag: {sample_lag}")
#     print(f"Estimated Distance: {distance:.2f} meters")

#     # Plot Signal A
#     plt.figure()
#     plt.stem(samples, signal_A, linefmt='b-', markerfmt='bo', basefmt=" ")
#     plt.title('Signal A (Station A)')
#     plt.xlabel('Sample Index')
#     plt.ylabel('Amplitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Frequency Spectrum of Signal A
#     plt.figure()
#     plt.stem(np.arange(len(X_A)), np.abs(X_A), linefmt='b-', markerfmt='bo', basefmt=" ")
#     plt.title('Frequency Spectrum of Signal A')
#     plt.xlabel('Frequency Index')
#     plt.ylabel('Magnitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Signal B
#     plt.figure()
#     plt.stem(samples, signal_B, linefmt='r-', markerfmt='ro', basefmt=" ")
#     plt.title('Signal B (Station B)')
#     plt.xlabel('Sample Index')
#     plt.ylabel('Amplitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Frequency Spectrum of Signal B
#     plt.figure()
#     plt.stem(np.arange(len(X_B)), np.abs(X_B), linefmt='r-', markerfmt='ro', basefmt=" ")
#     plt.title('Frequency Spectrum of Signal B')
#     plt.xlabel('Frequency Index')
#     plt.ylabel('Magnitude')
#     plt.grid(True)
#     plt.show()

#     # Plot Cross-Correlation
#     lag = np.arange(-n // 2, n // 2)  # Adjusted lag for -25 to 25
#     plt.figure()
#     plt.stem(lag, np.fft.fftshift(cross_corr), linefmt='g-', markerfmt='go', basefmt=" ")
#     plt.title('DFT-based Cross-Correlation')
#     plt.xlabel('Lag (samples)')
#     plt.ylabel('Correlation')
#     plt.grid(True)
#     plt.show()

# if __name__ == "__main__":
#     main()




import numpy as np
import matplotlib.pyplot as plt

# Constants
n = 50  # Number of samples
sampling_rate = 100  # Sampling rate (samples per second)
wave_velocity = 8000  # Velocity in meters/second (e.g., P-wave)
samples = np.arange(n)  # Sample indices

# Function to generate signals
def generate_signals(frequency=5):
    noise_freqs = [15, 30, 45]
    amplitudes = [0.5, 0.3, 0.1]
    noise_freqs2 = [10, 20, 40]
    amplitudes2 = [0.3, 0.2, 0.1]

    dt = 1 / sampling_rate
    time = samples * dt

    # Original clean signal
    original_signal = np.sin(2 * np.pi * frequency * time)

    # Adding noise
    noise_for_signal_A = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
                             for noise_freq, amplitude in zip(noise_freqs, amplitudes))
    noise_for_signal_B = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
                             for noise_freq, amplitude in zip(noise_freqs2, amplitudes2))
    signal_A = original_signal + noise_for_signal_A
    noisy_signal_B = signal_A + noise_for_signal_B

    # Apply fixed right shift of 3 to Signal B
    signal_B = np.roll(noisy_signal_B, 3)

    return signal_A, signal_B

# Function to compute DFT
def DFT(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        X[k] = sum(signal[n] * np.exp(-1j * 2 * np.pi * k * n / N) for n in range(N))
    return X

# Function to compute IDFT
def IDFT(X):
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        x[n] = sum(X[k] * np.exp(1j * 2 * np.pi * k * n / N) for k in range(N)) / N
    return x

# Function to compute cross-correlation using DFT and IDFT
def cross_correlation(signal_A, signal_B):
    X_A = DFT(signal_A)
    X_B = DFT(signal_B)
    X_corr = X_A * np.conj(X_B)
    cross_corr = np.real(IDFT(X_corr))
    return cross_corr

# Function to calculate distance
def calculate_distance(sample_lag, sampling_rate, wave_velocity):
    time_lag = abs(sample_lag) / sampling_rate
    distance = time_lag * wave_velocity
    return distance

# Main function
def main():
    # Generate signals
    signal_A, signal_B = generate_signals()

    # Frequency spectra
    X_A = DFT(signal_A)
    X_B = DFT(signal_B)

    # Cross-correlation
    cross_corr = cross_correlation(signal_A, signal_B)
    cross_corr = np.roll(cross_corr,6)

    # Find sample lag manually
    shifted_cross_corr = np.roll(cross_corr, n // 2)  # Manually shift the cross-correlation result
    max_index = np.argmax(shifted_cross_corr)  # Find index of the maximum value
    sample_lag = max_index - (n // 2)  # Calculate the sample lag

    # Calculate distance
    distance = calculate_distance(sample_lag, sampling_rate, wave_velocity)

    # Print Results
    print(f"Detected Sample Lag: {sample_lag}")
    print(f"Estimated Distance: {distance:.2f} meters")
    print(f"wave velocity: {wave_velocity}")

    # Plot Signal A
    plt.figure()
    plt.stem(samples, signal_A, linefmt='b-', markerfmt='bo', basefmt=" ")
    plt.title('Signal A (Station A)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    # Plot Frequency Spectrum of Signal A
    plt.figure()
    plt.stem(np.arange(len(X_A)), np.abs(X_A), linefmt='b-', markerfmt='bo', basefmt=" ")
    plt.title('Frequency Spectrum of Signal A')
    plt.xlabel('Frequency Index')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

    # Plot Signal B
    plt.figure()
    plt.stem(samples, signal_B, linefmt='r-', markerfmt='ro', basefmt=" ")
    plt.title('Signal B (Station B)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    # Plot Frequency Spectrum of Signal B
    plt.figure()
    plt.stem(np.arange(len(X_B)), np.abs(X_B), linefmt='r-', markerfmt='ro', basefmt=" ")
    plt.title('Frequency Spectrum of Signal B')
    plt.xlabel('Frequency Index')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

    # Plot Cross-Correlation
    lag = np.arange(-n // 2, n // 2)  # Adjusted lag for -25 to 25
    plt.figure()
    plt.stem(lag, shifted_cross_corr, linefmt='g-', markerfmt='go', basefmt=" ")
    plt.title('DFT-based Cross-Correlation')
    plt.xlabel('Lag (samples)')
    plt.ylabel('Correlation')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
