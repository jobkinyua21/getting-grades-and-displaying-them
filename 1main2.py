# making imports
import sys

import pandas as pd
from pandas import DataFrame

# getting list from user
data = [int(numbers) for numbers in input("list:").split(",")]

# converting list to data frame
df = DataFrame(data)

# calculations
y = "mean", df.mean(), "minimum", df.min(), "maximum", df.max()
sys.stdout.write(str(y))
