import math
import pandas as pd
a = pd.Series([2, 4, 6, 8])
b = pd.Series([1, 3, 5, 7])

result = sum((a - b)**2)**.5
print(result)
