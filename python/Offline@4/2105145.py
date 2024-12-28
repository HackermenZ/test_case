import numpy as np
import matplotlib.pyplot as plt

#DFT
def DFT(x):
    n = len(x)
    X = np.zeros(n, dtype=complex)
    for k in range(n):
        X[k] = sum(x[j] * np.exp(-2j * np.pi * k * j / n) for j in range(n))
    return X

#IDFT
def IDFT(X):
    n = len(X)
    x = np.zeros(n, dtype=complex)
    for k in range(n):
        x[k] = sum(X[j] * np.exp(2j * np.pi * k * j / n) for j in range(n)) / n
    return x


#FFT
def FFT(x):
    n = len(x)
    if n <= 1:
        return x
    else:
        even = FFT(x[::2])
        odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(n) / n)
        return np.concatenate([even + factor[:n // 2] * odd, even - factor[n // 2:] * odd])


#IFFT
def IFFT(X):
    n = len(X)
    if n <= 1:
        return X
    else:
        even = IFFT(X[::2])
        odd = IFFT(X[1::2])
        factor = np.exp(2j * np.pi * np.arange(n) / n)
        return np.concatenate([even + factor[:n // 2] * odd, even - factor[n // 2:] * odd])



#Cross Corelation
# Cross-Correlation using FFT
def cross_correlation(signal_A, signal_B):
    # Compute the cross-correlation of the two signals using FFT
    X_A = FFT(signal_A)
    X_B = FFT(signal_B)
    X_corr = X_A * np.conj(X_B)
    cross_corr = np.real(IFFT(X_corr))
    return cross_corr

def detect_shift(cross_corr,n):
    shifted_cross_corr=np.roll(cross_corr,n//2)
    max_index=np.argmax(shifted_cross_corr)
    sample_lag=max_index-(n//2)
    return sample_lag


def reverse_shift(image,horizontal_shift,vertical_shift):
    realigned_image=np.roll(image,horizontal_shift,axis=1)
    realigned_image=np.roll(realigned_image,vertical_shift,axis=0)
    return realigned_image

def main():
    image = plt.imread("image.png")
    shifted_image=plt.imread("shifted_image.png")

    if len(image.shape)==3:
        image = image[:,:,0]

    if len(shifted_image.shape)==3:
        shifted_image=shifted_image[:,:,0]

    row_A=image[image.shape[0]//2]

    row_B=shifted_image[shifted_image.shape[0]//2]


    column_A=image[:,image.shape[1]//2]

    column_B=shifted_image[:,shifted_image.shape[1]//2]

    cross_corr_row=cross_correlation(row_A,row_B)

    horizontal_shift=detect_shift(cross_corr_row,len(row_A))

    cross_corr_column=cross_correlation(column_A,column_B)

    vertical_shift=detect_shift(cross_corr_column,len(column_A))

    realigned_image=reverse_shift(shifted_image,horizontal_shift,vertical_shift)
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

    #Reversed Shifted Image
    plt.subplot(2, 3, 3)
    plt.imshow(realigned_image, cmap='gray')
    plt.title("Reversed Shifted Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()









