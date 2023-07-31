from statistics import mean
import pandas as pd
import numpy as np

def cor(x, y):
    return sum( (x - mean(x)) * (y - mean(y)) ) / ( sum((x - mean(x))**2) * sum((y - mean(y))**2) ) 

#df = pd.DataFrame(np.random.randint(1, 100, 16).reshape(4, 4), columns=list('efgh'), index=list('abcd'))
#print(df)
#print('Finding corr:')
#print(np.abs(df.corr()))


#print(np.random.randint(1, 100, 8).reshape((4, 2)))
#exit(0)
df = pd.DataFrame(np.random.randint(1, 100, 8).reshape((4, 2)), columns=list('ef'))
print('pandas corr\n', df.corr())
print('my corr', cor(df['e'], df['f']))
print('numpy corr', np.corrcoef(df['e'], df['f']))