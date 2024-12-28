 elif function_type == "sawtooth":
            # Sawtooth wave: linearly increasing from -1 to 1 over the period
            return 2 * (x / (2 * np.pi) - np.floor(0.5 + x / (2 * np.pi)))
    
        elif function_type == "triangle":
            # Triangle wave: periodic line with slope +1 and -1 alternately
            return np.abs(2 * (x / (2 * np.pi) - np.floor(0.5 + x / (2 * np.pi)))) * 2 - 1
    