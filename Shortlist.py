import pandas as pd
df = pd.read_csv("pythonspark.csv")
print(df)
df.sort_values("names")
