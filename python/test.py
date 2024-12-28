import numpy as np
import matplotlib.pyplot as plt

class FourierSeries:
    def __init__(self, func, L, terms=10):
        self.func = func
        self.L = L
        self.terms = terms

    def calculate_a0(self, N=1000):
        x = np.linspace(-self.L, self.L, N)
        y = self.func(x)
        return np.trapezoid(y, x) / (2 * self.L)

    def calculate_an(self, n, N=1000):
        x = np.linspace(-self.L, self.L, N)
        y = self.func(x) * np.cos(n * np.pi * x / self.L)
        return np.trapezoid(y, x) / self.L

    def calculate_bn(self, n, N=1000):
        x = np.linspace(-self.L, self.L, N)
        y = self.func(x) * np.sin(n * np.pi * x / self.L)
        return np.trapezoid(y, x) / self.L

    def approximate(self, x):
        a0 = self.calculate_a0()
        approximation = a0 / 2
        for n in range(1, self.terms + 1):
            an = self.calculate_an(n)
            bn = self.calculate_bn(n)
            approximation += an * np.cos(n * np.pi * x / self.L) + bn * np.sin(n * np.pi * x / self.L)
        return approximation

    def plot(self):
        x = np.linspace(-self.L, self.L, 1000)
        original = self.func(x)
        approximation = self.approximate(x)
        plt.figure(figsize=(10, 6))
        plt.plot(x, original, label='Original Function', color="blue")
        plt.plot(x, approximation, label=f'Fourier Series Approximation with (N={self.terms})', linestyle='--', color="red")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Fourier Series Approximation Example')
        plt.legend()
        plt.grid(True)
        plt.show()

def target_function(x, function_type="square"):
    if function_type == "square":
        return np.sign(np.sin(x))
    elif function_type == "sawtooth":
        return sawtooth_wave(x, 1, np.pi, 10)  # Adjust parameters as needed
    elif function_type == "triangle":
        return triangular_wave(x, 1, np.pi, 10)  # Adjust parameters as needed
    elif function_type == "sine":
        return np.sin(x)
    elif function_type == "cosine":
        return np.cos(x)
    else:
        raise ValueError("Function type not found")

def sawtooth_wave(x, A, T, terms):
    omega = 2 * np.pi / T
    approximation = A / 2
    approximation -= A / np.pi * sum((-1)**(n + 1) / n * np.sin(n * omega * x) for n in range(1, terms + 1))
    return approximation

def triangular_wave(x, A, T, terms):
    omega = 2 * np.pi / T
    approximation = A / 2
    approximation -= (4 * A / np.pi**2) * sum((1 / (2 * n - 1)**2) * np.cos((2*n - 1) * omega * x) * (-1)**(n + 1) for n in range(1, terms + 1))
    return approximation

if __name__ == '__main__':
    L = np.pi
    terms = 10
    for function_type in ["square", "sawtooth", "triangle", "sine", "cosine"]:
        print(f"Plotting Fourier series for {function_type} wave:")
        fourier_series = FourierSeries(lambda x: target_function(x, function_type=function_type), L, terms)
        fourier_series.plot()
