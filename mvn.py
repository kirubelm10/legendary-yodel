import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
df = pd.read_csv('medical_examination.csv')


# height_meter=(df['height']/100)**2
# BMI=df['weight'] / height_meter
# df['overweight'] = ( BMI > 25).astype(int)
#print(df.head(4))

u=pd.Series(10,12,13,14,15,16,7)
v=pd.Series(1,2,3,4,5,6,7)
cd=([u]/[v] > 5).astype(int)
print(cd)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

print(df.head(4))
