import pandas as pd
import numpy as np

# Set a random seed for reproducible results
np.random.seed(42)

# 1. Create a Pandas Series containing 10 random numbers (between 1 and 100)
random_data = np.random.randint(1, 101, size=10)
series = pd.Series(random_data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print("Original Pandas Series:")
print(series)
print("-" * 40)

# 2. Indexing Operations
print("Value at label 'c':", series['c'])
print("Values from label 'b' to 'e':\n", series['b:e'])
print("-" * 40)

# 3. Filtering Operations (filtering numbers greater than 50)
filtered_series = series[series > 50]
print("Filtered Series (Values > 50):\n", filtered_series)
print("-" * 40)

# 4. Statistical Operations
print(f"Mean: {series.mean()}")
print(f"Median: {series.median()}")
print(f"Minimum: {series.min()}")
print(f"Maximum: {series.max()}")