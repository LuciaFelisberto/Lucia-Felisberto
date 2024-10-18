import pandas as pd
num_01 = pd.Series([10,20,30,50,40,60,80,70,90,100])
num_02 = pd.Series([100,20,30,50,40,60,80,70,90,10])
print(num_01 + num_02)
print(num_01 - num_02)
print(num_01 * num_02)
print(num_01 / num_02)