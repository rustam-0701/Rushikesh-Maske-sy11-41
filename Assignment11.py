# Ten Random Numbers in Pandas Series

import numpy as np
import pandas as pd

# Set seed for same random numbers every time
np.random.seed(42)

# Generate 10 random numbers from 1 to 100
data = np.random.randint(1, 101, 10)

# Convert the numbers into Pandas Series
s = pd.Series(data)

# Display the Series
print(s)