import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('energy_use_in_the_UK.csv',delimiter = ';')

df = pd.DataFrame(data)
# df = pd.DataFrame(data)

# print(df)

df['timestamp'] = pd.to_datetime(df[' timestamp'] , format = "%Y-%m-%d %H:%M:%S")
# df = df.set_index(' timestamp')
df['y'] = df['timestamp'].dt.year
df['m'] = df['timestamp'].dt.month
df['d'] = df['timestamp'].dt.day
# df['q'] = df['timestamp'].dt.quarter


pc =pd.DataFrame(df[' coal'],df['y'],df['m'],df['d'])

print(pc)


# coal = pc.groupby(['y','m','d']).sum()

# print(df['d'])

# year = df.groupby(['y','m','d']).sum()
#
# year.plot()
# plt.show()
#
# coal.plot()
# plt.show()























#
