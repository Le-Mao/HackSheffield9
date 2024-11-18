import pandas as pd
import numpy as np



def create_graphs():
# Create a fake DataFrame with random data
    np.random.seed(42)
    iterations = np.arange(1, 101)
    random_walk = np.cumsum(np.random.randn(100)) + 50  # Random walk around 50

    df = pd.DataFrame({
        'Iteration': iterations,
        'Value': random_walk
    })

    sine_wave = 20 * np.sin(iterations / 10) + np.random.randn(100) * 2 + 50  # Sine wave with noise around 50

    df2 = pd.DataFrame({
        'Iteration': iterations,
        'Value': sine_wave
    })

    exp_growth = 10 * np.log1p(iterations) + np.random.randn(100) * 3  # Exponential growth with noise

    df3 = pd.DataFrame({
        'Iteration': iterations,
        'Value': exp_growth
    })
    return df, df2, df3