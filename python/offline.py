# # import numpy as np
# # import matplotlib.pyplot as plt
# # class DiscreteSignal:
# #     def __init__(self,INF):
# #         self.INF = INF
# #         self.values=np.zeros(2*INF+1)
# #     def set_value_at_time(self,time,value):
# #         if -self.INF<=time<=self.INF:
# #             self.values[time+self.INF]=value
# #         else:
# #             raise ValueError("Index out of range")
        
# #     def shift_signal(self,shift):
# #         shifted_signal=DiscreteSignal(self.INF)
# #         for i in range(-self.INF,self.INF):
# #             shifted_index=i-shift
# #             if -self.INF<=shifted_index<=self.INF:
# #                 shifted_signal.set_value_at_time(i,self.values[shifted_index+self.INF])
# #             return shifted_signal
    
# #     def add(self,other):
# #         if self.INF!=other.INF:
# #             raise ValueError("INF values do not match")
# #         new_signal=DiscreteSignal(self.INF)
# #         new_signal.values=self.values+other.values
# #         return new_signal
# #     def multiply(self,other):
# #         if self.INF!=other.INF:
# #             raise ValueError("INF values do not match")
# #         new_signal=DiscreteSignal(self.INF)
# #         new_signal.values=self.values*other.values
# #         return new_signal
    
# #     def multiply_const_factor(self,scaler):
# #         new_signal=DiscreteSignal(self.INF)
# #         new_signal.values=self.values*scaler
# #         return new_signal
    
# #     def plot(self):
# #         time = np.arange(-self.INF, self.INF+1)
# #         plt.stem(time, self.values)
# #         plt.xlabel('Time index (n)')
# #         plt.ylabel('Signal value')
# #         plt.title('Discrete Signal')
# #         plt.grid(True)
# #         plt.show()
        
    
# #     # Example usage:
# # if __name__ == "__main__":
# #     # Create a discrete signal with a range of -5 to 5
# #     signal = DiscreteSignal(INF=5)
    
# #     # Set some signal values
# #     signal.set_value_at_time(0, 1)
# #     signal.set_value_at_time(1, 2)
# #     signal.set_value_at_time(2, 3)
    
# #     # Plot the signal
# #     signal.plot()

# #     # Shift the signal
# #     shifted_signal = signal.shift_signal(1)
# #     shifted_signal.plot()

# #     # Add two signals
# #     signal2 = DiscreteSignal(INF=5)
# #     signal2.set_value_at_time(0, 2)
# #     signal2.set_value_at_time(1, -1)
# #     sum_signal = signal.add(signal2)
# #     sum_signal.plot()

# #     # Multiply two signals
# #     product_signal = signal.multiply(signal2)
# #     product_signal.plot()

# #     # Multiply the signal by a constant factor
# #     scaled_signal = signal.multiply_const_factor(0.5)
# #     scaled_signal.plot()
    
# import numpy as np
# import matplotlib.pyplot as plt
# class DiscreteSignal:
#     def __init__(self,INF):
#         self.INF = INF
#         self.values=np.zeros(2*INF+1)
#     def set_value_at_time(self,time,value):
#         if -self.INF<=time<=self.INF:
#             self.values[time+self.INF]=value
#         else:
#             raise ValueError("Index out of range")
        
#     def shift_signal(self,shift):
#         shifted_signal=DiscreteSignal(self.INF)
#         for i in range(-self.INF,self.INF):
#             shifted_index=i-shift
#             if -self.INF<=shifted_index<=self.INF:
#                 shifted_signal.set_value_at_time(i,self.values[shifted_index+self.INF])
#             return shifted_signal
    
#     def add(self,other):
#         if self.INF!=other.INF:
#             raise ValueError("INF values do not match")
#         new_signal=DiscreteSignal(self.INF)
#         new_signal.values=self.values+other.values
#         return new_signal
#     def multiply(self,other):
#         if self.INF!=other.INF:
#             raise ValueError("INF values do not match")
#         new_signal=DiscreteSignal(self.INF)
#         new_signal.values=self.values*other.values
#         return new_signal
    
#     def multiply_const_factor(self,scaler):
#         new_signal=DiscreteSignal(self.INF)
#         new_signal.values=self.values*scaler
#         return new_signal
    
#     def plot(self):
#         time = np.arange(-self.INF, self.INF+1)
#         plt.stem(time, self.values)
#         plt.xlabel('Time index (n)')
#         plt.ylabel('Signal value')
#         plt.title('Discrete Signal')
#         plt.grid(True)
#         plt.show()
        

# class ContinuousSignal:
#     def __init__(self,func):
#         self.func=func
    
#     def shift(self,shift):
#         return ContinuousSignal(lambda t:self.func(t-shift))
    
#     def add(self,other):
#         return ContinuousSignal(lambda t:self.func(t)+other.func(t))
    
#     def multiply(self,other):
#         return ContinuousSignal(lambda t:self.func(t)*other.func(t))
    
#     def multiply_const_factor(self,scaler):
#         return ContinuousSignal(lambda t:self.func(t)*scaler)
    
#     def plot(self,t_range=(-10,10),numpoints=1000,title="Continuous Signal"):
#         t = np.linspace(t_range[0], t_range[1], numpoints)
#         y_values = self.func(t)
#         plt.plot(t, y_values)
#         plt.xlabel('Time (t)')
#         plt.ylabel('Signal x(t)')
#         plt.title(title)
#         plt.grid(True)
#         plt.show()
        



# class LTI_Discrete:
#     def __init__(self, impulse_response):
#         """
#         Initializes the LTI Discrete system with a given impulse response.
        
#         :param impulse_response: An instance of DiscreteSignal representing the system's impulse response.
#         """
#         self.impulse_response = impulse_response

#     def linear_combination_of_impulses(self, input_signal):
#         """
#         Decomposes the input signal into a linear combination of unit impulses.
        
#         :param input_signal: The input discrete signal.
#         :return: The unit impulses and their coefficients.
#         """
#         impulses = []
#         coefficients = []
#         for i, value in enumerate(input_signal.values):
#             if value != 0:
#                 impulses.append(i)
#                 coefficients.append(value)
#         return impulses, coefficients

#     def output(self, input_signal):
#         """
#         Finds the output of the LTI system using its impulse response and input signal.
        
#         :param input_signal: The input discrete signal.
#         :return: The output discrete signal.
#         """
#         impulses, coefficients = self.linear_combination_of_impulses(input_signal)
#         output_signal = np.zeros_like(input_signal.values)
#         for i, coeff in zip(impulses, coefficients):
#             shifted_impulse_response = np.roll(self.impulse_response.values, i)
#             output_signal += coeff * shifted_impulse_response
#         return output_signal




# class LTI_Continuous:
#     def __init__(self, impulse_response):
#         """
#         Initializes the LTI Continuous system with a given continuous-time impulse response.
        
#         :param impulse_response: An instance of ContinuousSignal representing the system's impulse response.
#         """
#         self.impulse_response = impulse_response

#     def linear_combination_of_impulses(self, input_signal, delta):
#         """
#         Decomposes the input continuous signal into a linear combination of impulses of width delta.
        
#         :param input_signal: The input continuous signal.
#         :param delta: The width of each impulse.
#         :return: The impulses and their coefficients.
#         """
#         t_values = np.arange(-10, 10, delta)  # Sample time values
#         impulses = np.zeros_like(t_values)
#         for i, t in enumerate(t_values):
#             impulses[i] = input_signal.func(t) * delta
#         return t_values, impulses

#     def output_approx(self, input_signal, delta):
#         """
#         Approximates the output of the system by first decomposing the input, then using the impulse response.
        
#         :param input_signal: The input continuous signal.
#         :param delta: The width of the impulses.
#         :return: The approximated output continuous signal.
#         """
#         t_values, impulses = self.linear_combination_of_impulses(input_signal, delta)
#         output_signal = np.zeros_like(t_values)
#         for i, impulse in enumerate(impulses):
#             shifted_impulse_response = self.impulse_response.func(t_values - t_values[i])
#             output_signal += impulse * shifted_impulse_response
#         return output_signal
    
    


# def main():
#     # Discrete Portion
#     impulse_response_discrete = np.array([0, 1, 0.5, 0])  # Example impulse response
#     input_signal_discrete = np.array([0, 1, 0, 2])  # Example input signal

#     # Create LTI Discrete System
#     lti_discrete = LTI_Discrete(impulse_response_discrete)
#     output_signal_discrete = lti_discrete.output(input_signal_discrete)

#     # Plot Discrete Impulse Response and Output
#     plt.subplot(2, 1, 1)
#     plt.stem(impulse_response_discrete)
#     plt.title("Discrete Impulse Response")

#     plt.subplot(2, 1, 2)
#     plt.stem(output_signal_discrete)
#     plt.title("Discrete Output Signal")

#     plt.show()

#     # Continuous Portion
#     impulse_response_continuous = ContinuousSignal(lambda t: np.exp(-t) * (t >= 0))  # Example impulse response
#     input_signal_continuous = ContinuousSignal(lambda t: np.sin(t) * (t >= 0))  # Example input signal

#     # Create LTI Continuous System
#     lti_continuous = LTI_Continuous(impulse_response_continuous)
#     output_signal_continuous = lti_continuous.output_approx(input_signal_continuous, delta=0.01)

#     # Plot Continuous Impulse Response and Output
#     t_range = np.linspace(-10, 10, 1000)
#     plt.subplot(2, 1, 1)
#     plt.plot(t_range, impulse_response_continuous.func(t_range))
#     plt.title("Continuous Impulse Response")

#     plt.subplot(2, 1, 2)
#     plt.plot(t_range, output_signal_continuous)
#     plt.title("Continuous Output Signal")

#     plt.show()

# if __name__ == "__main__":
#     main()
    
    
    
    
    
import numpy as np
import matplotlib.pyplot as plt

class DiscreteSignal:
    def __init__(self, INF):
        self.INF = INF
        self.values = np.zeros(2 * INF + 1)
        
    def set_value_at_time(self, time, value):
        if -self.INF <= time <= self.INF:
            self.values[time + self.INF] = value
        else:
            raise ValueError("Index out of range")
        
    def shift_signal(self, shift):
        shifted_signal = DiscreteSignal(self.INF)
        for i in range(-self.INF, self.INF + 1):
            shifted_index = i - shift
            if -self.INF <= shifted_index <= self.INF:
                shifted_signal.set_value_at_time(i, self.values[shifted_index + self.INF])
        return shifted_signal
    
    def add(self, other):
        if self.INF != other.INF:
            raise ValueError("INF values do not match")
        new_signal = DiscreteSignal(self.INF)
        new_signal.values = self.values + other.values
        return new_signal
    
    def multiply(self, other):
        if self.INF != other.INF:
            raise ValueError("INF values do not match")
        new_signal = DiscreteSignal(self.INF)
        new_signal.values = self.values * other.values
        return new_signal
    
    def multiply_const_factor(self, scaler):
        new_signal = DiscreteSignal(self.INF)
        new_signal.values = self.values * scaler
        return new_signal
    
    def plot(self):
        time = np.arange(-self.INF, self.INF + 1)
        plt.stem(time, self.values)
        plt.xlabel('Time index (n)')
        plt.ylabel('Signal value')
        plt.title('Discrete Signal')
        plt.grid(True)
        plt.show()


class ContinuousSignal:
    def __init__(self, func):
        self.func = func
    
    def shift(self, shift):
        return ContinuousSignal(lambda t: self.func(t - shift))
    
    def add(self, other):
        return ContinuousSignal(lambda t: self.func(t) + other.func(t))
    
    def multiply(self, other):
        return ContinuousSignal(lambda t: self.func(t) * other.func(t))
    
    def multiply_const_factor(self, scaler):
        return ContinuousSignal(lambda t: self.func(t) * scaler)
    
    def plot(self, t_range=(-10, 10), numpoints=1000, title="Continuous Signal"):
        t = np.linspace(t_range[0], t_range[1], numpoints)
        y_values = self.func(t)
        plt.plot(t, y_values)
        plt.xlabel('Time (t)')
        plt.ylabel('Signal x(t)')
        plt.title(title)
        plt.grid(True)
        plt.show()


class LTI_Discrete:
    def __init__(self, impulse_response):
        """
        Initializes the LTI Discrete system with a given impulse response.
        """
        self.impulse_response = impulse_response

    def linear_combination_of_impulses(self, input_signal):
        """
        Decomposes the input signal into a linear combination of unit impulses.
        """
        impulses = []
        coefficients = []
        for i, value in enumerate(input_signal.values):
            if value != 0:
                impulses.append(i)
                coefficients.append(value)
        return impulses, coefficients

    def output(self, input_signal):
        """
        Finds the output of the LTI system using its impulse response and input signal.
        """
        impulses, coefficients = self.linear_combination_of_impulses(input_signal)
        output_signal = np.zeros_like(input_signal.values)
        for i, coeff in zip(impulses, coefficients):
            shifted_impulse_response = np.roll(self.impulse_response.values, i - self.impulse_response.INF)
            output_signal += coeff * shifted_impulse_response
        return output_signal


class LTI_Continuous:
    def __init__(self, impulse_response):
        """
        Initializes the LTI Continuous system with a given continuous-time impulse response.
        """
        self.impulse_response = impulse_response

    def linear_combination_of_impulses(self, input_signal, delta):
        """
        Decomposes the input continuous signal into a linear combination of impulses of width delta.
        """
        t_values = np.arange(-10, 10, delta)  # Sample time values
        impulses = np.zeros_like(t_values)
        for i, t in enumerate(t_values):
            impulses[i] = input_signal.func(t) * delta
        return t_values, impulses

    def output_approx(self, input_signal, delta):
        """
        Approximates the output of the system by first decomposing the input, then using the impulse response.
        """
        t_values, impulses = self.linear_combination_of_impulses(input_signal, delta)
        output_signal = np.zeros_like(t_values)
        for i, impulse in enumerate(impulses):
            shifted_impulse_response = self.impulse_response.func(t_values - t_values[i])
            output_signal += impulse * shifted_impulse_response
        return output_signal


# def main():
#     # Discrete Portion
#     INF = 5
#     impulse_response_discrete = DiscreteSignal(INF)
#     impulse_response_discrete.set_value_at_time(0, 1)
#     impulse_response_discrete.set_value_at_time(1, 0.5)
    
#     input_signal_discrete = DiscreteSignal(INF)
#     input_signal_discrete.set_value_at_time(0, 1)
#     input_signal_discrete.set_value_at_time(3, 2)

#     # Create LTI Discrete System
#     lti_discrete = LTI_Discrete(impulse_response_discrete)
#     output_signal_discrete = lti_discrete.output(input_signal_discrete)

#     # Plot Discrete Impulse Response and Output
#     plt.subplot(2, 1, 1)
#     impulse_response_discrete.plot()

#     plt.subplot(2, 1, 2)
#     time = np.arange(-INF, INF + 1)
#     plt.stem(time, output_signal_discrete)
#     plt.title("Discrete Output Signal")

#     plt.show()

#     # Continuous Portion
#     impulse_response_continuous = ContinuousSignal(lambda t: np.exp(-t) * (t >= 0))  # Example impulse response
#     input_signal_continuous = ContinuousSignal(lambda t: np.sin(t) * (t >= 0))  # Example input signal

#     # Create LTI Continuous System
#     lti_continuous = LTI_Continuous(impulse_response_continuous)
#     output_signal_continuous = lti_continuous.output_approx(input_signal_continuous, delta=0.01)

#     # Plot Continuous Impulse Response and Output
#     t_range = np.linspace(-10, 10, 1000)
#     plt.subplot(2, 1, 1)
#     impulse_response_continuous.plot(t_range=(0, 10), title="Continuous Impulse Response")

#     plt.subplot(2, 1, 2)
#     plt.plot(t_range, output_signal_continuous)
#     plt.title("Continuous Output Signal")

#     plt.show()

# if __name__ == "__main__":
#     main()
    
    
    
    
    
import numpy as np
import matplotlib.pyplot as plt

def main():
    # === Discrete Portion === #
    INF = 5

    # Step 1: Create a discrete LTI system with the impulse response from Figure 3
    impulse_response_discrete = DiscreteSignal(INF)
    impulse_response_discrete.set_value_at_time(0, 1)  # Delta function impulse
    impulse_response_discrete.set_value_at_time(1, 0.5)  # Some decay in the impulse response

    # Step 2: Create a discrete input signal similar to Figure 1
    input_signal_discrete = DiscreteSignal(INF)
    input_signal_discrete.set_value_at_time(0, 2)
    input_signal_discrete.set_value_at_time(1, -1)
    input_signal_discrete.set_value_at_time(2, 3)
    input_signal_discrete.set_value_at_time(3, 1)

    # Step 3: Create LTI Discrete System and plot the impulses multiplied by their coefficients (Figure 1 and Figure 2)
    lti_discrete = LTI_Discrete(impulse_response_discrete)
    impulses, coefficients = lti_discrete.linear_combination_of_impulses(input_signal_discrete)

    # Plot the input signal and the impulses
    plt.figure(figsize=(10, 6))

    # Input discrete signal (Figure 1)
    plt.subplot(2, 1, 1)
    plt.stem(np.arange(-INF, INF + 1), input_signal_discrete.values, linefmt='b-', markerfmt='bo', basefmt="r-")
    plt.title('Input Discrete Signal (Figure 1)')
    
    # Impulses multiplied by coefficients (Figure 2)
    plt.subplot(2, 1, 2)
    plt.stem(np.arange(-INF, INF + 1), coefficients, linefmt='g-', markerfmt='go', basefmt="r-")
    plt.title('Returned Impulses multiplied by respective coefficients (Figure 2)')
    
    plt.tight_layout()
    plt.show()

    # Step 4: Call the output method and plot the output signal (Figure 3 and Figure 4)
    output_signal_discrete = lti_discrete.output(input_signal_discrete)

    plt.figure(figsize=(10, 6))

    # Impulse response (Figure 3)
    plt.subplot(2, 1, 1)
    plt.stem(np.arange(-INF, INF + 1), impulse_response_discrete.values, linefmt='b-', markerfmt='bo', basefmt="r-")
    plt.title('Impulse Response (Figure 3)')
    
    # Output discrete signal (Figure 4)
    plt.subplot(2, 1, 2)
    plt.stem(np.arange(-INF, INF + 1), output_signal_discrete, linefmt='g-', markerfmt='go', basefmt="r-")
    plt.title('Output Discrete Signal (Figure 4)')
    
    plt.tight_layout()
    plt.show()

    # === Continuous Portion === #
    # Step 5: Create continuous LTI system and input signal matching Figure 5
    impulse_response_continuous = ContinuousSignal(lambda t: np.exp(-t) * (t >= 0))  # Decaying exponential impulse response
    input_signal_continuous = ContinuousSignal(lambda t: np.sin(t) * (t >= 0))  # Sine wave input for positive t

    lti_continuous = LTI_Continuous(impulse_response_continuous)
    
    # Step 6: Decompose input signal into impulses and plot reconstruction with varying delta (Figure 6 and Figure 7)
    delta_values = [0.5, 0.1, 0.01]
    for delta in delta_values:
        t_values, impulses = lti_continuous.linear_combination_of_impulses(input_signal_continuous, delta)
        output_signal_continuous = lti_continuous.output_approx(input_signal_continuous, delta)
        
        plt.figure(figsize=(10, 6))
        
        plt.subplot(2, 1, 1)
        plt.plot(t_values, impulses, 'b-', label=f"Delta = {delta}")
        plt.title('Returned impulses multiplied by their coefficients (Figure 6)')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(t_values, output_signal_continuous, 'g-', label=f"Reconstructed Signal with Delta = {delta}")
        plt.title('Reconstruction of input signal with varying delta (Figure 7)')
        plt.legend()

        plt.tight_layout()
        plt.show()

    # Step 7: Call output approx method and plot the result (Figure 8 and Figure 9)
    delta_final = 0.01
    output_signal_final = lti_continuous.output_approx(input_signal_continuous, delta_final)

    plt.figure(figsize=(10, 6))

    # Continuous impulse response (Figure 8)
    t_range = np.linspace(0, 10, 1000)
    plt.subplot(2, 1, 1)
    plt.plot(t_range, impulse_response_continuous.func(t_range), 'b-', label="Impulse Response")
    plt.title('Continuous Impulse Response (Figure 8)')
    plt.legend()

    # Final output approximation (Figure 9)
    plt.subplot(2, 1, 2)
    plt.plot(t_range, output_signal_final, 'g-', label=f"Output Approximation with Delta = {delta_final}")
    plt.title('Approximate output signal (Figure 9)')
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()