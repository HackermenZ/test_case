import numpy as np
import matplotlib.pyplot as plt

# DFT Implementation
def DFT(x):
    n = len(x)
    X = np.zeros(n, dtype=complex)
    for k in range(n):
        X[k] = sum(x[j] * np.exp(-2j * np.pi * k * j / n) for j in range(n))
    return X

# IDFT Implementation
def IDFT(X):
    n = len(X)
    x = np.zeros(n, dtype=complex)
    for k in range(n):
        x[k] = sum(X[j] * np.exp(2j * np.pi * k * j / n) for j in range(n)) / n
    return x

# FFT Implementation
def FFT(x):
    n = len(x)
    if n <= 1:
        return x
    else:
        even = FFT(x[::2])
        odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(n) / n)
        return np.concatenate([even + factor[:n // 2] * odd, even - factor[n // 2:] * odd])

# IFFT Implementation
def IFFT(X):
    n = len(X)
    if n <= 1:
        return X
    else:
        even = IFFT(X[::2])
        odd = IFFT(X[1::2])
        factor = np.exp(2j * np.pi * np.arange(n) / n)
        return np.concatenate([even + factor[:n // 2] * odd, even - factor[n // 2:] * odd])

# Cross-Correlation using FFT
def cross_correlation(signal_A, signal_B):
    # Compute the cross-correlation of the two signals using FFT
    X_A = FFT(signal_A)
    X_B = FFT(signal_B)
    X_corr = X_A * np.conj(X_B)
    cross_corr = np.real(IFFT(X_corr))
    return cross_corr
iihc
# Detect the shift based on maximum correlation
def detect_shift(cross_corr, n):
    # Shifting the cross-correlation to match the peak at the center
    shifted_cross_corr = np.roll(cross_corr, n // 2)
    max_index = np.argmax(shifted_cross_corr)
    sample_lag = max_index - (n // 2)
    return sample_lag

# Reverse the shift in the image
def reverse_shift(image, horizontal_shift, vertical_shift):
    # Shift the image by the detected horizontal and vertical shifts
    realigned_image = np.roll(image, horizontal_shift, axis=1)  # Horizontal shift
    realigned_image = np.roll(realigned_image, vertical_shift, axis=0)  # Vertical shift
    return realigned_image

# Main Function
def main():
    # Load the images (make sure to replace these with actual image paths)
    image = plt.imread("image.png")  # Original image
    shifted_image = plt.imread("shifted_image.png")  # Shifted image
    
    # Ensure the images are grayscale (2D arrays)
    if len(image.shape) == 3:
        image = image[:, :, 0]  # Convert to grayscale (first channel)
    if len(shifted_image.shape) == 3:
        shifted_image = shifted_image[:, :, 0]  # Convert to grayscale (first channel)
    
    # Select a row and column from both images to detect horizontal and vertical shifts
    row_A = image[image.shape[0] // 2]  # Choose a central row for horizontal shift
    row_B = shifted_image[shifted_image.shape[0] // 2]
    column_A = image[:, image.shape[1] // 2]  # Choose a central column for vertical shift
    column_B = shifted_image[:, shifted_image.shape[1] // 2]
    
    # Compute cross-correlation for horizontal shift (row-wise)
    cross_corr_row = cross_correlation(row_A, row_B)
    horizontal_shift = detect_shift(cross_corr_row, len(row_A))
    
    # Compute cross-correlation for vertical shift (column-wise)
    cross_corr_column = cross_correlation(column_A, column_B)
    vertical_shift = detect_shift(cross_corr_column, len(column_A))
    
    # Reverse the detected shifts in the shifted image
    realigned_image = reverse_shift(shifted_image, horizontal_shift, vertical_shift)
    
    # Visualize the results
    plt.figure(figsize=(12, 8))

    # Original Image
    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Shifted Image
    plt.subplot(2, 3, 2)
    plt.imshow(shifted_image, cmap='gray')
    plt.title(f"Shifted Image")
    plt.axis('off')

    # Reversed Shifted Image
    plt.subplot(2, 3, 3)
    plt.imshow(realigned_image, cmap='gray')
    plt.title(f"Reversed Shifted Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
