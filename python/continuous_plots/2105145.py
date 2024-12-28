import numpy as np
import matplotlib.pyplot as plt
class DiscreteSignal:
    def __init__(self,values=None):
        self.values=np.array(values,dtype=float) if values is not None else np.array([],dtype=float)
    
    def set_value_at_time(self,time,value):
        if time>=len(self.values) or time<0:
            extend_size=max(0,time+1-len(self.values))
            self.values=np.append(self.values,np.zeros(extend_size,dtype=float))
        self.values[time]=value
        
    def shift_signal(self,shift):
        shift=int(shift)
        if shift<0:
            return DiscreteSignal(np.append(np.zeros(-shift,dtype=float),self.values))
        elif shift>0:
            return DiscreteSignal(self.values[shift:])
        else:
            return DiscreteSignal(self.values.copy())
        
    def add(self,other):
        max_length=max(len(self.values),len(other.values))
        extended_self=np.append(self.values,np.zeros(max_length-len(self.values),dtype=float))
        extended_other=np.append(other.values,np.zeros(max_length-len(other.values),dtype=float))
        return DiscreteSignal(extended_self+extended_other)
    
    def multiply(self,other):
        max_length=max(len(self.values),len(other.values))
        extended_self=np.append(self.values,np.zeros(max_length-len(self.values),dtype=float))
        extended_other=np.append(other.values,np.zeros(max_length-len(other.values),dtype=float))
        return DiscreteSignal(extended_self*extended_other)
    
    def multiply_const_factor(self,scaler):
        return DiscreteSignal(self.values*scaler)
    
    def plot(self):
        plt.stem(range(len(self.values)), self.values)
        plt.title('Discrete Signal Plot')
        plt.xlabel('Time Index')
        plt.ylabel('Signal Value')
        plt.grid(True)
        plt.show()


class ContinuousSignal:
    def __init__(self,func):
        self.func=func
        
    def shift(self,shift):
        return ContinuousSignal(lambda t: self.func(t-shift))
    
    def add(self,other):
        return ContinuousSignal(lambda t: self.func(t)+other.func(t))
    def multiply(self,other):
        return ContinuousSignal(lambda t: self.func(t)*other.func(t))
    def multiply_const_factor(self,scaler):
        return ContinuousSignal(lambda t: self.func(t)*scaler)
    
    def plot(self,t_range):
        t = np.linspace(t_range[0], t_range[1], 400)
        plt.plot(t, self.func(t))
        plt.title('Continuous Signal Plot')
        plt.xlabel('Time')
        plt.ylabel('Signal Value')
        plt.grid(True)
        plt.show()
        
        
class LTIDiscrete:
    def __init__(self, impulse_response):
        self.impulse_response = impulse_response

    def linear_combination_of_impulses(self, input_signal):
        impulses = [input_signal.multiply_const_factor(input_signal.values[i]) if input_signal.values[i] != 0 else None for i in range(len(input_signal.values))]
        impulses = [imp for imp in impulses if imp is not None]
        coefficients = [input_signal.values[i] for i in range(len(input_signal.values)) if input_signal.values[i] != 0]
        return impulses, coefficients

    def output(self, input_signal):
        impulses, coefficients = self.linear_combination_of_impulses(input_signal)
        output_signal = DiscreteSignal()
        for imp, coeff in zip(impulses, coefficients):
            shifted_impulse_response = self.impulse_response.shift_signal(-int(coeff))
            output_signal = output_signal.add(shifted_impulse_response.multiply_const_factor(coeff))
        return output_signal

        
        
        
        
        
        
        
class LTIContinuous:
    def __init__(self,impulse_response):
        self.impulse_response=impulse_response
        
    def linear_combination_of_impulses(self,input_signal,delta):
        t_values=np.arange(-INF,INF,delta)
        impulses=[input_signal.multiply_const_factor(1/delta) if input_signal.func(t)!=0 else None for t in t_values]
        impulses=[imp for imp in impulses if imp is not None]
        coefficients=[input_signal.func(t) for t in t_values if input_signal.func(t)!=0]
        return impulses,coefficients
    
    
    def output_approx(self,input_signal,delta):
        impulses,coefficients=self.linear_combination_of_impulses(input_signal,delta)
        output_signal=ContinuousSignal(lambda t: 0)
        for imp,coeff in zip(impulses,coefficients):
            shifted_impulse_response = self.impulse_response.shift(-coeff)
            output_signal=output_signal.add(shifted_impulse_response.multiply_const_factor(coeff))
        return output_signal
    
    





import numpy as np
import matplotlib.pyplot as plt

def unit_step(t):
    return np.where(t >= 0, 1, 0)

def input_signal(t, a):
    return np.exp(-a * t) * unit_step(t)

def impulse_response(t):
    return unit_step(t)

def theoretical_output(t, a):
    return (1 - np.exp(-a * t)) / a * unit_step(t)


INF=5
class DiscreteSignal:
    def __init__(self, values):
        self.values = np.array(values)
    
    def plot(self, title, ax=None, filename=None, show=True):
        if ax is None:
            fig, ax = plt.subplots()
        ax.stem(range(-5, len(self.values) - 5), self.values, basefmt=" ")
        ax.set_title(title)
        ax.set_xlabel('n (Time Index)')
        ax.set_ylabel('x[n]')
        ax.set_ylim([-0.1, 3.1])  # Adjust y-axis limits to match the scale of examples
        if filename:
            plt.savefig(filename)
        if show:
            plt.grid(True)
            plt.show()

def plot_impulses_with_coefficients(signal, coefficients):
    fig, axes = plt.subplots(3, 4, figsize=(18, 12))  # Grid size adjusted for 12 subplots
    axes = axes.flatten()
    combined_signal = np.zeros_like(signal)
    for i, coeff in enumerate(coefficients):
        impulse = np.zeros_like(signal)
        impulse[i] = coeff
        combined_signal += impulse
        axes[i].stem(range(-5, len(signal) - 5), impulse, basefmt=" ", linefmt='C0-', markerfmt='C0o')
        axes[i].set_title(f'$\delta[n - {i-5}]x[{coeff}]$')
        axes[i].set_xlabel('n (Time Index)')
        axes[i].set_ylabel('x[n]')
        axes[i].set_ylim([-0.1, 2.1])
    # Plot the sum of all impulses
    axes[-1].stem(range(-5, len(signal) - 5), combined_signal, basefmt=" ", linefmt='C0-', markerfmt='C0o')
    axes[-1].set_title('Sum of Impulses')
    axes[-1].set_xlabel('n (Time Index)')
    axes[-1].set_ylabel('x[n]')
    axes[-1].set_ylim([-0.1, 2.1])
    plt.tight_layout()
    plt.savefig('impulses_multiplied_by_coefficients.png')
    plt.grid(True)
    plt.show()




def plot_impulse_response():
    # Creating an impulse response with specific non-zero values
    impulse_values = np.zeros(11)  # assuming index range from -5 to 5
    impulse_values[5] = 1  # h[0]
    impulse_values[6] = 1  # h[1]
    impulse_values[7] = 1  # h[2]
    
    # Create an instance of DiscreteSignal for the impulse response
    impulse_response = DiscreteSignal(impulse_values)

    # Plot the impulse response as a separate figure
    impulse_response.plot('Impulse Response, INF = 5', filename='impulse_response.png', show=False)



# def plot_response_of_input_signal(input_signal, impulse_response):
#     fig, axes = plt.subplots(3, 4, figsize=(18, 12))  # Grid size adjusted for 12 subplots
#     axes = axes.flatten()

#     # Create shifted and scaled versions of the impulse response
#     for i in range(-5, 6):  # Covering shifts from -5 to 5
#         shifted_impulse = np.roll(impulse_response.values, i)
#         scaled_impulse = shifted_impulse * (input_signal.values[i+5] if (i+5) >= 0 and (i+5) < len(input_signal.values) else 0)
#         axes[i+5].stem(range(len(scaled_impulse)), scaled_impulse, basefmt=" ")
#         axes[i+5].set_title(f'h[n-({i})] * x[{i}]')
#         axes[i+5].set_xlabel('n (Time Index)')
#         axes[i+5].set_ylabel('x[n]')
#         axes[i+5].set_ylim([-0.1, 3.1])

#     # Calculate the overall output by summing all scaled impulses
#     output_signal = np.zeros_like(input_signal.values)
#     for i in range(-5, 6):
#         shifted_impulse = np.roll(impulse_response.values, i)
#         output_signal += shifted_impulse * (input_signal.values[i+5] if (i+5) >= 0 and (i+5) < len(input_signal.values) else 0)

#     # Plot the output signal
#     axes[-1].stem(range(len(output_signal)), output_signal, basefmt=" ")
#     axes[-1].set_title('Output = Sum')
#     axes[-1].set_xlabel('n (Time Index)')
#     axes[-1].set_ylabel('x[n]')
#     axes[-1].set_ylim([-0.1, 3.1])

#     plt.tight_layout()
#     plt.savefig('output_signal.png')
#     plt.grid(True)
#     plt.show()


def plot_response_of_input_signal(input_signal, impulse_response):
    fig, axes = plt.subplots(3, 4, figsize=(18, 12))
    axes = axes.flatten()
    for i in range(-5, 6):
        shifted_impulse = np.roll(impulse_response.values, i + 5)  # shift by i + 5 to center the impulses around zero index
        scaled_impulse = shifted_impulse * (input_signal.values[i+5] if (i+5) >= 0 and (i+5) < len(input_signal.values) else 0)
        indices = range(-5, len(scaled_impulse) - 5)
        axes[i+5].stem(indices, scaled_impulse, basefmt=" ")
        axes[i+5].set_title(f'h[n-({i})] * x[{i}]')
        axes[i+5].set_xlabel('n (Time Index)')
        axes[i+5].set_ylabel('x[n]')
        axes[i+5].set_ylim([-0.1, 3.1])
        axes[i+5].set_xlim([-5, 5])

    # Sum all scaled impulses for the output
    output_signal = np.sum([np.roll(impulse_response.values * input_signal.values[i+5], i + 5) 
                            for i in range(-5, 6) if (i+5) < len(input_signal.values)], axis=0)
    axes[-1].stem(indices, output_signal, basefmt=" ")
    axes[-1].set_title('Output = Sum')
    axes[-1].set_xlabel('n (Time Index)')
    axes[-1].set_ylabel('x[n]')
    axes[-1].set_ylim([-0.1, max(output_signal) + 0.1])
    axes[-1].set_xlim([-5, 5])

    plt.tight_layout()
    plt.savefig('output_signal.png')
    plt.show()

def main():
    # Impulse response and input signal
    impulse_response = DiscreteSignal([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    input_signal = DiscreteSignal([0, 0, 0, 0, 0, 0.5, 2, 0, 0, 0, 0])

    # Plot input signal as a separate figure
    input_signal.plot('Input Discrete Signal, INF = 5', filename='input_signal.png', show=False)

    # Coefficients for plotting (only two nonzero values)
    coefficients = [0] * 11
    coefficients[5] = 0.5  # delta[n-0]*x[0]
    coefficients[6] = 2    # delta[n-1]*x[1]

    # Plot impulses multiplied by coefficients as another separate image
    plot_impulses_with_coefficients(input_signal.values, coefficients)
    
    
    plot_impulse_response()

    # Plot the response of the input signal to the impulse response
    plot_response_of_input_signal(input_signal, impulse_response)

if __name__ == '__main__':
    main()


def main():
    a = 1  # Decay rate for the input signal
    t = np.linspace(-1, 5, 1000)  # Time vector from -1 to 5 seconds
    
    x_t = input_signal(t, a)
    h_t = impulse_response(t)
    y_t = theoretical_output(t, a)
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, x_t, label='Input $x(t) = e^{-at}u(t)$')
    plt.title('Input Signal')
    plt.xlabel('Time (t)')
    plt.ylabel('$x(t)$')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, h_t, label='Impulse Response $h(t) = u(t)$')
    plt.title('Impulse Response')
    plt.xlabel('Time (t)')
    plt.ylabel('$h(t)$')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, y_t, label='Output $y(t) = \\frac{1}{a}(1 - e^{-at})u(t)$')
    plt.title('Output Signal')
    plt.xlabel('Time (t)')
    plt.ylabel('$y(t)$')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
    
    
    
     # Impulse response and input signal
    impulse_response = DiscreteSignal([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    input_signal = DiscreteSignal([0, 0, 0, 0, 0, 0.5, 2, 0, 0, 0, 0])

    # Plot input signal as a separate figure
    input_signal.plot('Input Discrete Signal, INF = 5', filename='input_signal.png', show=False)

    # Coefficients for plotting (only two nonzero values)
    coefficients = [0] * 11
    coefficients[5] = 0.5  # delta[n-0]*x[0]
    coefficients[6] = 2    # delta[n-1]*x[1]

    # Plot impulses multiplied by coefficients as another separate image
    plot_impulses_with_coefficients(input_signal.values, coefficients)
    
    
    plot_impulse_response()

    # Plot the response of the input signal to the impulse response
    plot_response_of_input_signal(input_signal, impulse_response)


if __name__ == "__main__":
    main()

